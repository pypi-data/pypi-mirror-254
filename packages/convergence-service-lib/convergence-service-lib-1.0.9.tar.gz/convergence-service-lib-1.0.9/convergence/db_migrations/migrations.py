import abc
from typing import List

from convergence.convergence_service import ConvergenceService
from convergence.db_migrations.blueprint_formatter import SqlDialectFormatter


class DatabaseSeedSpec:
    def __init__(self):
        self.table_name = None
        self.fields = {}

    def table(self, table):
        self.table_name = table
        return self

    def field(self, name: str, value):
        self.fields[name] = value
        return self


class DatabasePreparationStep(abc.ABC):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def get_dependencies(self) -> List[str]:
        pass

    def __repr__(self):
        return self.name


class BaseDatabaseSeed(DatabasePreparationStep):
    def __init__(self, name):
        super().__init__(name)

    @abc.abstractmethod
    def get_dependencies(self):
        pass

    @abc.abstractmethod
    def get_seeds(self, service: ConvergenceService) -> List[DatabaseSeedSpec]:
        pass


class BaseDatabaseMigration(DatabasePreparationStep):
    def __init__(self, name):
        super().__init__(name)

    @abc.abstractmethod
    def get_dependencies(self):
        pass

    @abc.abstractmethod
    def get_migration_ddl(self, formatters: SqlDialectFormatter):
        pass

    @abc.abstractmethod
    def allow_failure(self):
        pass
