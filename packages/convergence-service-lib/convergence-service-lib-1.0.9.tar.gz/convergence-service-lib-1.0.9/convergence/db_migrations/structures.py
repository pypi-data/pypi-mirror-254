class TableColumnBlueprint:
    def __init__(self, name, type, is_primary_key=False, is_unique=False, allow_null=False, default_value=None):
        self.name = name
        self.type = type
        self.is_primary_key = is_primary_key
        self.is_unique = is_unique
        self.allow_null = allow_null
        self.default_value = default_value


class TableBlueprint:
    def __init__(self):
        self.name = ''
        self.check_existence = False
        self.columns = []
        self.indices = []

    def add_operation_dates(self, created_at=True, updated_at=True, deleted_at=True):
        if created_at:
            self.columns.append(TableColumnBlueprint('created_at', 'timestamp', default_value='CURRENT_TIMESTAMP'))
        if updated_at:
            self.columns.append(TableColumnBlueprint('updated_at', 'timestamp', allow_null=True, default_value='NULL'))
        if deleted_at:
            self.columns.append(TableColumnBlueprint('deleted_at', 'timestamp', allow_null=True, default_value='NULL'))


class TableIndexBlueprint:
    def __init__(self, type, columns):
        self.type = type
        self.columns = columns


class TablesRelationshipBlueprint:
    def __init__(self):
        self.table = ''
        self.foreign_key = ''
        self.primary_table = ''
        self.primary_key = ''
