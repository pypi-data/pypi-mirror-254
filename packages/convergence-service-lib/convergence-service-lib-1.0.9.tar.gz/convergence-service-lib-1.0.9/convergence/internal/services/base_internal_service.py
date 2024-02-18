import time
from datetime import timezone, datetime, timedelta

import jwt
import requests


class BaseExternalService:
    def __init__(self, service, url, jwt_authority=None, service_jwt=False):
        self.url = url
        self.service = service
        self.jwt = self.__create_internal_jwt(service, jwt_authority, service_jwt)

    def __create_internal_jwt(self, service, authorities, service_jwt):
        service_info = service.get_service_info()
        signing_key = service.get_configuration('security.authentication.secret').replace('\\n', '\n')

        payload = {
            "sub": service_info.SERVICE_NAME,
            "iss": service_info.SERVICE_NAME,
            "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=1),
        }

        if service_jwt:
            payload['is_inter_service_call'] = True

        if authorities is not None:
            authorities = [] if authorities is None else authorities
            authorities = [authorities] if not isinstance(authorities, list) else authorities
            payload['authorities'] = authorities

        return jwt.encode(payload, signing_key, algorithm="ES512")

    def get_service_url(self, service_name):
        from convergence.internal.services.infrastructure_service import InfrastructureMicroService
        infra_service = InfrastructureMicroService(self.service)
        connection_details = infra_service.get_service_connection_details(service_name)
        print(connection_details)
        if self.is_successful(connection_details):
            body = connection_details['body']
            return f'http://{body["host"]}:{body["port"]}'
        else:
            raise ValueError(f'Unable to get the base url for service ({service_name})')

    def post_request(self, endpoint, payload):
        _url = self.url + endpoint
        arguments = {
            'json': payload,
            'headers': {
                'Authorization': 'Bearer ' + self.jwt
            }
        }

        response = None
        success = False

        for i in range(5):
            try:
                response = requests.post(_url, **arguments)
                response = response.json()
                success = True
            except:
                time.sleep(0.5)

        if not success:
            response = {
                'header': {
                    'status_code': 500,
                    'code': 'err_api_internal_error',
                    'message': 'Unable to connect to the service after 5 retries.',
                    'body_type': 'failure_info'
                },
                'body': None
            }

        return response

    def is_successful(self, response):
        if response is None:
            return False

        header = response.get('header')
        if header is None:
            return False

        http_code = header.get('status_code')
        if http_code is None or not isinstance(http_code, int):
            return False

        return 200 <= http_code < 300
