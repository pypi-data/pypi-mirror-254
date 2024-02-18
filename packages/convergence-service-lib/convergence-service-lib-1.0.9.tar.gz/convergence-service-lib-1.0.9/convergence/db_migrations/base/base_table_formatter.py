from convergence.db_migrations.blueprint_formatter import BlueprintFormatter
from convergence.db_migrations.structures import TableIndexBlueprint
from convergence.db_migrations.structures import TableBlueprint, TableColumnBlueprint


class BaseTableBlueprintFormatter(BlueprintFormatter):
    def to_sql(self, blueprint: TableBlueprint):
        result = []

        check_existence = ""
        if blueprint.check_existence:
            check_existence = "IF NOT EXISTS "

        result.append("CREATE TABLE ")
        result.append(check_existence)
        result.append(blueprint.name)
        result.append(" \n(")

        constraint_count = 0
        for column in blueprint.columns:
            if column.is_unique:
                constraint_count += 1

        index = 0
        for column in blueprint.columns:
            index += 1
            is_last_statement = index == len(blueprint.columns) and constraint_count == 0
            result.append("\n    ")
            result.append(self.get_column_definition(column))
            if not is_last_statement:
                result.append(",")

        index = 0
        for column in blueprint.columns:
            if column.is_unique:
                if index == 0:
                    result.append("\n")
                index += 1
                is_last_statement = index == constraint_count
                result.append(f"\n    CONSTRAINT {blueprint.name}_{column.name}_unique_index UNIQUE ({column.name})")

                if not is_last_statement:
                    result.append(",")

        result.append("\n)")

        if len(blueprint.indices) > 0:
            for indexBlueprint in blueprint.indices:
                result.append("\n\n")
                result.append(self.format_table_index(blueprint, indexBlueprint))
                result.append("")

        result = ''.join(result)
        return result

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
        return f"CREATE INDEX {table}_{fields_underscore}_index ON {table} USING {index_blueprint.type}({fields_comma})"

    def get_column_definition(self, column: TableColumnBlueprint):
        result = []

        result.append(self.prepare_column_name_for_creation(column))
        result.append(' ')
        result.append(self.to_sql_type(column.type))
        result.append(' ')

        if column.is_primary_key:
            result.append("PRIMARY KEY ")

        if column.allow_null:
            result.append("NULL")
        else:
            result.append("NOT NULL")

        if column.default_value is not None:
            result.append(" DEFAULT ")
            result.append(column.default_value)

        result = ''.join(result)
        return result

    def prepare_column_name_for_creation(self, column: TableColumnBlueprint):
        return column.name

    def to_sql_type(self, type: str):
        result = ""

        if type == "String":
            result = "text"
        elif type.startswith("String[") and type.endswith("]"):
            length = type[7:-1]
            result = f"varchar({length})"
        elif type == "bool" or type == "boolean":
            result = "boolean"
        elif type.lower() == "json":
            result = "json"
        elif type == "int":
            result = "int"
        elif type == "date":
            result = "date"
        elif type == "double":
            result = "float8"
        elif type == "float":
            result = "float4"
        elif type == "timestamp":
            result = "timestamp"
        elif type.lower() == "uuid":
            result = "uuid"

        return result
