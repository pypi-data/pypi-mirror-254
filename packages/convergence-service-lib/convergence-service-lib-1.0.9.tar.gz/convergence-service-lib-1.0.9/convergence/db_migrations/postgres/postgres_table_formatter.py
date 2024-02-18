from convergence.db_migrations.base.base_table_formatter import BaseTableBlueprintFormatter
from convergence.db_migrations.structures import TableBlueprint, TableIndexBlueprint


class PostgresTableFormatter(BaseTableBlueprintFormatter):
    def format_table_index(self, blueprint: TableBlueprint, index_blueprint: TableIndexBlueprint):
        table = blueprint.name
        fields_comma = []
        fields_underscore = []

        sc = ""
        su = ""

        for col in index_blueprint.columns:
            fields_comma.append(sc)
            fields_comma.append(col)
            fields_underscore.append(su)
            fields_underscore.append(col)
            sc = ", "
            su = "_"

        fields_underscore = ''.join(fields_underscore)
        fields_comma = ''.join(fields_comma)

        return f"CREATE INDEX CONCURRENTLY {table}_{fields_underscore}_index ON {table} USING {index_blueprint.type}({fields_comma})"
