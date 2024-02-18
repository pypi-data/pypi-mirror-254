import re
from dataclasses import is_dataclass

from .sql_static import SqlStatic


class Sql:
    def __init__(self, cls: type):
        assert is_dataclass(cls), "mute have annotion named @dataclasses.dataclass"

        self.cls: type = cls

        self.table_name: str = self._get_table_name(cls)
        self.annotations: dict[str, type] = cls.__annotations__.copy()
        self.field_list_all: list[str] = self._get_field_list_all(cls)
        self.field_list_common: list[str] = self._get_field_list_common(cls, SqlStatic.FIELD_LIST_PRE)
        self.field_list_unique: list[str] = cls.field_list_unique

        assert SqlStatic.FIELD_LIST_PRE[0] in self.field_list_all, f"{SqlStatic.FIELD_LIST_PRE[0]} must in definition"

        assert not (
            field_list_else := set(self.field_list_unique) - set(self.field_list_common)
        ), f"field_list_unique <= field_list_common, {field_list_else=}, {self.field_list_unique=}, {self.field_list_common=}"

    @staticmethod
    def _get_table_name(cls: type) -> str:
        return Sql._camel_to_snake(cls.__name__)

    @staticmethod
    def _camel_to_snake(key_camel: str) -> str:
        key_snake = re.sub(r"([A-Z])", r"_\1", key_camel).lower()
        if key_snake.startswith("_"):
            key_snake = key_snake[1:]
        return key_snake

    @staticmethod
    def _get_field_list_all(cls: type) -> list[str]:
        return list(cls.__annotations__.copy())

    @staticmethod
    def _get_field_list_common(cls: type, field_list_pre: list[str]) -> list[str]:
        return [i for i in cls.__annotations__.copy() if i not in field_list_pre]

    def exist(self) -> str:
        return SqlStatic.exist(self.table_name)

    def desc(self) -> str:
        return SqlStatic.desc(self.table_name)

    def alert_modify(self, field_name: str, field_type: type, generated_expression: str = None) -> str:
        return SqlStatic.alert_modify(self.table_name, field_name, field_type, generated_expression)

    def create(self) -> str:
        assert isinstance(self.cls, type)
        return SqlStatic.create(
            self.table_name,
            self.annotations,
            self.field_list_common,
            self.field_list_unique,
        )

    def select(self, _where: str) -> str:
        return SqlStatic.select(self.table_name, self.field_list_all, _where)

    def insert(self) -> str:
        return SqlStatic.insert(self.table_name, self.field_list_common)

    def insert_with_duplicate(self, field_list: list[str]) -> str:
        field_list = field_list or self.field_list_common
        return SqlStatic.insert_with_duplicate(self.table_name, field_list)

    def update(self, field_list: list[str]) -> str:
        return SqlStatic.update(self.table_name, field_list)
