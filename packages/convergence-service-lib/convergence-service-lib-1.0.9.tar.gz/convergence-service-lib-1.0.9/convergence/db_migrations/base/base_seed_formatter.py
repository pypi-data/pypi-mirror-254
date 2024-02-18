import datetime
import uuid

from convergence.db_migrations.blueprint_formatter import BlueprintFormatter


class BaseDatabaseSeedFormatter(BlueprintFormatter):
    def to_sql(self, blueprint):
        result = []

        for seed in blueprint:
            field_list = []
            values_list = []

            sep = ""
            for field in seed.fields:
                field_list.append(sep)
                values_list.append(sep)

                field_list.append(field)
                values_list.append(self.format_value(seed.fields[field]))
                sep = ", "

            result.append("INSERT INTO ")
            result.append(''.join(seed.table_name))
            result.append("(")
            result.append(''.join(field_list))
            result.append(") VALUES(")
            result.append(''.join(values_list))
            result.append("); \n\n")

        result = ''.join(result)
        return result

    def format_value(self, o):
        result = None

        if o is None:
            result = "NULL"
        elif isinstance(o, uuid.UUID):
            result = f"'{str(o)}'"
        elif isinstance(o, bool):
            result = 'true' if o else 'false'
        elif isinstance(o, datetime.datetime):
            result = o.strftime("%Y-%m-%d %H:%M:%S")
            result = f"'{result}'"
        elif isinstance(o, int) or isinstance(o, float):
            result = str(o)
        elif isinstance(o, str):
            lower = o.lower()
            forbidden = ['--', "'", 'create', 'drop', 'alter', 'insert', 'grant']
            for s in forbidden:
                if s in lower:
                    raise ValueError("This could be an SQL injection.")

            result = "'" + o + "'"
        else:
            raise ValueError()

        result = ''.join(result)
        return result
