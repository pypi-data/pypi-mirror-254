from enum import Enum

from pydantic import BaseModel


class Mode(Enum):
    IMPORT = "Import"


class Partition(BaseModel):
    name: str
    type: str = "m"
    mode: Mode = Mode.IMPORT
    source: str
