import datetime
import time
import uuid
from typing import List

import psycopg2

from convergence.convergence_service import ConvergenceService
import convergence.database_orm as orm
from convergence.db_migrations.base_seed_migration_table import BaseCreateMigrationsTable, DatabaseMigration
from convergence.db_migrations.blueprint_formatter import SqlDialectFormatter
from convergence.db_migrations.migrations import DatabasePreparationStep, BaseDatabaseSeed, BaseDatabaseMigration
from convergence.db_migrations.postgres.postgres_relation_formatter import PostgresTableRelationBlueprintFormatter
from convergence.db_migrations.postgres.postgres_seed_formatter import PostgresDatabaseSeedFormatter
from convergence.db_migrations.postgres.postgres_table_formatter import PostgresTableFormatter
from convergence.internal.utils.dag import DirectedAcyclicGraph


class __ExternalMigrationDependency(DatabasePreparationStep):
    def __init__(self, name):
        super().__init__(name)

    def get_dependencies(self) -> List[str]:
        return []


def sort_migrations(migrations: List[DatabasePreparationStep]) \
        -> List[DatabasePreparationStep]:
    result = []
    internal_nodes = [m.name for m in migrations]
    external_dependencies = []
    for m in migrations:
        external_dependencies.extend(m.get_dependencies())

    external_dependencies = set(external_dependencies) - set(internal_nodes)
    for ex_dep in external_dependencies:
        result.append(__ExternalMigrationDependency(ex_dep))
    result.extend(migrations)

    dag = DirectedAcyclicGraph(result)
    sorted_steps = dag.topological_sort()

    result = []
    for m in sorted_steps:
        if not isinstance(m, __ExternalMigrationDependency):
            result.append(m)

    return result


def get_list_of_migrations(service: ConvergenceService, connection) -> List[str]:
    result = []

    cursor = connection.cursor()
    try:

        cursor.execute('''
            SELECT
                migration_name
            FROM database_migrations
        ''')
        records = cursor.fetchall()
        result = []

        for record in records:
            result.append(record[0])
    except:
        result = []
        connection.rollback()
    finally:
        cursor.close()

    return result


def initialize_formatters(service: ConvergenceService) -> SqlDialectFormatter:
    result = SqlDialectFormatter()
    db_type = service.get_configuration('database.type')

    if db_type == 'postgres':
        result.create_table_formatter = PostgresTableFormatter()
        result.insert_seeds_formatter = PostgresDatabaseSeedFormatter()
        result.create_relation_formatter = PostgresTableRelationBlueprintFormatter()
    else:
        raise ValueError()

    return result


def create_connection_to_db(service: ConvergenceService):
    attempts = 40
    for i in range(attempts):
        connection = __try_create_connection_to_db(service)
        if connection is not None:
            return connection
        print('Connection to DB attempt failed, waiting 0.5 second before retrying')
        time.sleep(0.5)


def __try_create_connection_to_db(service: ConvergenceService):
    try:
        return psycopg2.connect(user=service.get_configuration('database.username'),
                                password=service.get_configuration('database.password'),
                                host=service.get_configuration('database.host'),
                                port=service.get_configuration('database.port'),
                                database=service.get_configuration('database.name'))
    except:
        return None


def __execute_sql_command(command, connection):
    result = False
    error = None
    cursor = connection.cursor()

    try:
        cursor.execute(command)
        connection.commit()
        result = True
    except BaseException as ex:
        error = str(ex)
        connection.rollback()
    finally:
        cursor.close()

    return result, error


def __save_migration_state(connection, migration, command):
    entry = DatabaseMigration()
    entry.uuid = uuid.uuid4()
    entry.migration_name = migration.name
    entry.command = command
    entry.applied_timestamp = datetime.datetime.now()

    connection.add(entry)
    connection.commit()


def apply_database_migration(service, migration, connection, formatters: SqlDialectFormatter):
    command = None
    executed_with_success = False
    error = None

    if isinstance(migration, BaseDatabaseSeed):
        command = formatters.insert_seeds_formatter.to_sql(migration.get_seeds(service))
        executed_with_success = __execute_sql_command(command, connection)
    elif isinstance(migration, BaseDatabaseMigration):
        command = migration.get_migration_ddl(formatters)
        executed_with_success, error = __execute_sql_command(command, connection)
        if migration.allow_failure():
            executed_with_success = True
    else:
        return f'The migration type for {migration.name} is not supported'

    if not executed_with_success:
        return f'An error occurred while running migration {migration.name}: {error}'

    session_maker = orm.DBSessionLocal
    session = session_maker()
    __save_migration_state(session, migration, command)
    session.close()

    return None


def load_database_migrations(migrations_module: str) -> List[DatabasePreparationStep]:
    module = __get_source_module(migrations_module)
    service_migrations = __get_classes_of_module_with_base_classes(migrations_module, module, [DatabasePreparationStep],
                                                                   set())

    service_migrations.append(BaseCreateMigrationsTable())

    return service_migrations


def __is_of_base_classes(cls, base_types):
    try:
        obj = cls()
        result = False

        for t in base_types:
            result = result or isinstance(obj, t)

        return result
    except:
        return False


def __get_classes_of_module_with_base_classes(migrations_module, python_module, base_types, already_added):
    result = []
    attributes = dir(python_module)

    for attr_name in attributes:
        if attr_name.startswith('__'):
            continue

        attribute = getattr(python_module, attr_name)
        attribute_str = str(attribute)
        if attribute_str.startswith(f'<module \'{migrations_module}.'):
            result.extend(
                __get_classes_of_module_with_base_classes(migrations_module, attribute, base_types, already_added))
        if attribute_str.startswith(f'<class \'{migrations_module}.') and attribute_str not in already_added:
            already_added.add(attribute_str)
            if __is_of_base_classes(attribute, base_types):
                result.append(attribute())

    return result


def __get_source_module(migrations_module: str):
    sub_modules = migrations_module.split('.')
    result = __import__(sub_modules[0])

    for sub in sub_modules[1:]:
        result = getattr(result, sub)

    return result
