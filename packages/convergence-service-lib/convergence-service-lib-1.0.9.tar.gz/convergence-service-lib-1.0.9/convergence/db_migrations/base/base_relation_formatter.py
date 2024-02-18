from convergence.db_migrations.blueprint_formatter import BlueprintFormatter
from convergence.db_migrations.structures import TablesRelationshipBlueprint


class BaseTableRelationFormatter(BlueprintFormatter):
    def to_sql(self, blueprint: TablesRelationshipBlueprint):
        return f'ALTER TABLE {blueprint.table} ADD FOREIGN KEY ({blueprint.foreign_key}) REFERENCES {blueprint.primary_table}({blueprint.primary_key});'
