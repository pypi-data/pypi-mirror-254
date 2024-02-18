from sqlalchemy import Column, UUID, String, TIMESTAMP

from convergence.database_orm import EntityBase
from convergence.db_migrations.blueprint_formatter import SqlDialectFormatter
from convergence.db_migrations.migrations import BaseDatabaseMigration
from convergence.db_migrations.structures import TableBlueprint, TableColumnBlueprint


class DatabaseMigration(EntityBase):
    __tablename__ = "database_migrations"
    uuid = Column(UUID, primary_key=True)
    migration_name = Column(String)
    command = Column(String)
    applied_timestamp = Column(TIMESTAMP)


class BaseCreateMigrationsTable(BaseDatabaseMigration):
    def __init__(self):
        super().__init__('create_migration_table')

    def get_dependencies(self):
        return []

    def get_migration_ddl(self, formatters: SqlDialectFormatter):
        result = []

        migration_table = TableBlueprint()
        migration_table.name = "database_migrations"

        migration_table.columns.append(TableColumnBlueprint("uuid", "UUID", True, False, False, None))
        migration_table.columns.append(TableColumnBlueprint("migration_name", "String[255]", False, True, False, None))
        migration_table.columns.append(TableColumnBlueprint("command", "String", False, False, False, None))
        migration_table.columns.append(
            TableColumnBlueprint("applied_timestamp", "timestamp", False, False, False, "CURRENT_TIMESTAMP"))

        result.append(formatters.create_table_formatter.to_sql(migration_table))

        result = ''.join(result)
        return result

    def allow_failure(self):
        return False
