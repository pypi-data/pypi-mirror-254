import abc


class BlueprintFormatter(abc.ABC):
    @abc.abstractmethod
    def to_sql(self, blueprint):
        pass


class SqlDialectFormatter:
    def __init__(self):
        self.create_table_formatter = None
        self.create_relation_formatter = None
        self.insert_seeds_formatter = None
