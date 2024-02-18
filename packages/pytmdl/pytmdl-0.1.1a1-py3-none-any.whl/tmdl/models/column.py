import typing as t
from enum import Enum

from pydantic import BaseModel


class DataType(Enum):
    AUTOMATIC = "Automatic"
    STRING = "String"
    BOOLEAN = "Boolean"
    DATETIME = "DateTime"
    INT = "Int64"

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"'{self}'"


class Column(BaseModel):

    name: str
    description: t.Optional[str] = None
    source_column: str
    data_type: DataType = DataType.AUTOMATIC
    is_key: bool = False
    is_name_inferred: bool = False
    format_string: t.Optional[str] = None
    summarize_by: str = "None"

    def dump(self) -> str:
        column_str = f"""    column {self.name}
        sourceColumn: {self.source_column}
        dataType: {self.data_type.value}
        summarizeBy: {self.summarize_by}
"""
        if self.is_key:
            column_str += "        isKey\n"

        if self.is_name_inferred:
            column_str += "        isNameInferred\n"

        return column_str
