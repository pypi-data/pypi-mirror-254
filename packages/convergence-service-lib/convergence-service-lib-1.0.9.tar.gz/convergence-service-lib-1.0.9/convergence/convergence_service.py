import abc
import argparse
import os
import sys
from typing import List

import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from convergence.internal.observability.service_stdout_redirection import ConsoleFileDualWriter
from convergence.internal.services.authentication_service import AuthenticationMicroService
from convergence.internal.services.infrastructure_service import InfrastructureMicroService
from convergence.internal.utils.service_configuration_loader import load_service_configuration
from convergence.metadata.service_authority import ServiceAuthorityDeclaration
import convergence.constants as constants
from starlette.middleware.cors import CORSMiddleware

from convergence.security.access_control_layer import AccessControlLayer
from convergence.security.authorization_filter import AuthorizationMiddleware
from convergence.validations.gateway_header_validation_filter import GatewayHeaderValidationMiddleware
from convergence.validations.input_validation_filter import InputValidationMiddleware


def create_cli_argument_parser():
    parser = argparse.ArgumentParser(description='Convergence Service')

    parser.add_argument('--profile',
                        required=False,
                        type=str,
                        help='Specify a profile to override the values in the default one.')

    return parser


def get_override_profile_file_path(args):
    if args.profile is not None:
        return f'./configurations/application-{args.profile}.yaml'

    env_profile = os.environ.get("CONVERGENCE_SERVICE_PROFILE")
    if env_profile is not None:
        return f'./configurations/application-{env_profile}.yaml'

    return None


class ServiceState:
    def __init__(self):
        self.status = 'initializing'


class ConvergenceEndpointInfo:
    def __init__(self, url, method, authorization, exposed_through_gateway):
        self.url = url
        self.method = method
        self.authorization = authorization
        self.exposed_through_gateway = exposed_through_gateway


def pad(value, length):
    return value + ''.join([' '] * (length - len(value)))


class ConvergenceService(abc.ABC):
    _instance = None
    __endpoints_info: List[ConvergenceEndpointInfo] = []

    def __init__(self, default_config_path=None, profile_config_path=None):
        if ConvergenceService._instance is not None:
            raise ValueError('There can only be one instance/extension of ConvergenceService.')

        ConvergenceService._instance = self
        self._configuration = load_service_configuration(default_config_path, profile_config_path)
        self.service_state = ServiceState()
        self._db_migration_module = 'db_migrations'

        kwargs = {}
        mode = self.get_configuration('application.mode')
        if mode == 'production':
            kwargs['openapi_url'] = None
        self.app = FastAPI(**kwargs)
        self.acl = AccessControlLayer()

    @staticmethod
    def instance():
        return ConvergenceService._instance

    def include_router(self, router):
        self.app.include_router(router)

    def start(self):
        info = self.get_service_info()
        print('Launching service with info:')
        print(f'   Name: {info.SERVICE_NAME}')
        print(f'   Version: {info.SERVICE_VERSION}')
        print(f'   Hash: {info.SERVICE_VERSION_HASH}')
        print('', flush=True)

        uvicorn.run(self.app, host="0.0.0.0", port=self.get_configuration('server.port'))
        if self.get_configuration('observability.enable_stout_redirection'):
            sys.stdout.flush()

    def get_configuration(self, path, default_value=None):
        try:
            components = path.split('.')
            result = self._configuration

            for c in components:
                result = result[c]

            return result
        except BaseException as e:  # noqa
            if default_value is None:
                raise e
            return default_value

    def initialize(self):
        self.__initialize_redirect_log_to_file()
        self.__print_figlet()
        self.__print_server_port()

        if self.__is_database_enabled():
            self.service_state.status = 'initializing_db'
            self.__initialize_orm()
            self.__migrate_database()
            self.service_state.status = 'db_initialized'
        else:
            print('Service is configured to disable database initialization.')

        self.__save_service_authority()
        self.service_state.status = 'initializing_service'
        self.__initialize_cors()
        self.__initialize_service_filters()
        self.service_state.status = 'healthy'

    def __is_database_enabled(self):
        result = True

        try:
            disable = self.get_configuration('database.disable')
            return not disable
        except:
            pass

        return result

    def __initialize_orm(self):
        import convergence.database_orm as orm
        db_type = self.get_configuration('database.type')
        if db_type == 'postgres':
            user = self.get_configuration('database.username')
            password = self.get_configuration('database.password')
            host = self.get_configuration('database.host')
            db = self.get_configuration('database.name')
            port = self.get_configuration('database.port')
            orm.SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db}"
            orm.DB_ENGINE = create_engine(orm.SQLALCHEMY_DATABASE_URL)

            orm.DBSessionLocal = sessionmaker(bind=orm.DB_ENGINE)
        else:
            raise ValueError('Unsupported database type')

    def __migrate_database(self):
        from convergence.internal.db.database_migrations import (
            load_database_migrations,
            get_list_of_migrations,
            initialize_formatters,
            create_connection_to_db,
            apply_database_migration,
            sort_migrations
        )

        migrations = load_database_migrations(self._db_migration_module)
        migrations = sort_migrations(migrations)
        formatters = initialize_formatters(self)

        with create_connection_to_db(self) as connection:
            print('Starting to apply database migrations:')
            applied_database_migrations = get_list_of_migrations(self, connection)

            error = None
            failed_migration = None
            for migration in migrations:
                if migration.name not in applied_database_migrations:
                    if failed_migration is not None:
                        print(f'   - {pad(migration.name + ":", 50)} [ SKIPPED ]')
                    else:
                        migration_error = apply_database_migration(self, migration, connection, formatters)
                        if migration_error is not None:
                            failed_migration = migration.name
                            error = migration_error
                            print(f'   - {pad(migration.name + ":", 50)} [ FAILED ]')
                        else:
                            print(f'   - {pad(migration.name + ":", 50)} [ SUCCESS ]')
                else:
                    print(f'   - {pad(migration.name + ":", 50)} [ ALREADY_APPLIED ]')

            if error is not None:
                raise ValueError(error)

    def __save_service_authority(self):
        self.service_state.status = "initializing_authorities"
        mode = self.get_configuration('application.mode')

        service_authorities_handler = self.get_service_authorities_handler()
        if str(service_authorities_handler).startswith('<class '):
            if mode == 'production':
                self.__register_class_service_authority(service_authorities_handler)
            else:
                print('Service is running in non-production mode, skipping the authorities initialization:')
                authorities = self.__get_declared_authorities(service_authorities_handler)
                if len(authorities) == 0:
                    print('   -> Service doesn\'t declares any authority')
                else:
                    for auth in authorities:
                        tier = pad(f'[Tier {auth.tier}]', 10)
                        print(f'   - {tier} {auth.authority}')
        elif str(service_authorities_handler).startswith('<method '):
            service_authorities_handler()

        self.service_state.status = "authorities_initialized"

    @abc.abstractmethod
    def get_service_authorities_handler(self):
        pass

    @abc.abstractmethod
    def get_service_info(self):
        pass

    def __register_class_service_authority(self, service_authorities_handler):
        authorities = self.__get_declared_authorities(service_authorities_handler)

        if len(authorities) > 0:
            print('Service is running in production mode, starting to initialize authorities:')
            infrastructure_service = InfrastructureMicroService(self)
            authentication_service_url = infrastructure_service.get_service_url('authentication-service')
            print(f'   -> Authentication Service URL: {authentication_service_url}')
            authentication_service = AuthenticationMicroService(self, authentication_service_url)

            any_failed = False
            for authority in authorities:
                if not self.__register_single_service_authority(authority, authentication_service):
                    print(f'   * {pad(authority.authority + ":", 50)} [ FAILED INITIALIZATION ]')
                    any_failed = True
                else:
                    print(f'   * {pad(authority.authority + ":", 50)} [ INITIALIZED ]')

            if any_failed:
                raise ValueError('Service was unable to initialize the necessary authorities.')
        else:
            print('Service is running in production mode, but doesn\'t declare any authority')

    def __register_single_service_authority(self, authority, authentication_service):
        request = {
            'uuid': str(authority.uuid),
            'authority': authority.authority,
            'display_name': authority.display_name,
            'tier': authority.tier,
        }

        response = authentication_service.register_service_authority(request)
        return response['header']['status_code'] == 200

    def __get_declared_authorities(self, service_authorities_handler):
        authorities = []
        attributes = dir(service_authorities_handler)
        for attribute in attributes:
            value = getattr(service_authorities_handler, attribute)
            if isinstance(value, ServiceAuthorityDeclaration):
                authorities.append(value)
        return authorities

    def __print_figlet(self):
        print('   ' + """
   ______                                                    
  / ____/___  ____ _   _____  _________ ____  ____  ________ 
 / /   / __ \/ __ \ | / / _ \/ ___/ __ `/ _ \/ __ \/ ___/ _ \\
/ /___/ /_/ / / / / |/ /  __/ /  / /_/ /  __/ / / / /__/  __/
\____/\____/_/ /_/|___/\___/_/   \__, /\___/_/ /_/\___/\___/ 
                                /____/
        """.strip())  # noqa
        print(' :: Convergence Platform ::')
        print(f'     Version: {constants.VERSION}')
        print(f'     Hash: {constants.VERSION_HASH}')
        print(f'     Build Date: {constants.BUILD_DATE}')
        print('')

    def __print_server_port(self):
        print(f'Server will run on port: {self.get_configuration("server.port")}')

    def __initialize_cors(self):
        is_enabled = self.get_configuration('cors.enabled', default_value=False)
        if is_enabled:
            print('Initializing CORS headers for the service.')
            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=self.__to_list(self.get_configuration('cors.allow_origins')),
                allow_credentials=self.get_configuration('cors.allow_credentials'),
                allow_methods=self.__to_list(self.get_configuration('cors.allow_methods')),
                allow_headers=self.__to_list(self.get_configuration('cors.allow_headers')),
            )
        else:
            print('CORS header initialization is disabled for this service.')

    def __to_list(self, value):
        if not isinstance(value, list):
            value = [value]

        return value

    @staticmethod
    def register_endpoint_info(url, method, authorization, exposed_through_gateway):
        ConvergenceService.__endpoints_info.append(
            ConvergenceEndpointInfo(url, method.upper(), authorization, exposed_through_gateway))

    @staticmethod
    def get_endpoint_info(url: str, method: str):
        result = None
        method = method.upper()
        path_matched = False

        for info in ConvergenceService.__endpoints_info:
            url_matched = ConvergenceService.__match_url_to_endpoint(url, info.url)
            if url_matched:
                path_matched = True
            if info.method == method and url_matched:
                result = info
                break

        return result, path_matched

    @staticmethod
    def __match_url_to_endpoint(url, ep_url):
        if url == ep_url:
            return True

        comps_url = url.split('/')
        comps_ep_url = ep_url.split('/')

        if len(comps_url) == len(comps_ep_url):
            for a, b in zip(comps_url, comps_ep_url):
                if (b.startswith('{') and b.endswith('}')) or a == b:
                    continue
                return False

            return True
        else:
            return False

    def __initialize_service_filters(self):
        self.app.add_middleware(GatewayHeaderValidationMiddleware, service=self)
        self.app.add_middleware(AuthorizationMiddleware, service=self)
        self.app.add_middleware(InputValidationMiddleware, service=self)

    def __initialize_redirect_log_to_file(self):
        if self.get_configuration('observability.enable_stout_redirection'):
            dual_writer = ConsoleFileDualWriter(self, sys.stdout)
            sys.stdout = dual_writer
            sys.stderr = dual_writer
