import typing as t
from enum import Enum

from pydantic import BaseModel

from .column import Column


class DataCategory(Enum):
    """
    Source: https://docs.tabulareditor.com/api/TabularEditor.TOMWrapper.Table.html#TabularEditor_TOMWrapper_Table_DataCategory
    """

    DEFAULT = "Default"
    TIME = "Time"
    GEOGRAPHY = "Geography"


class Table(BaseModel):

    name: str
    data_category: DataCategory = DataCategory.DEFAULT

    columns: t.List[Column]

    def dump(self):
        table_str = f"""table {self.name}
    dataCategory: {self.data_category.value}

"""
        for column in self.columns:
            table_str += column.dump()

        return table_str
