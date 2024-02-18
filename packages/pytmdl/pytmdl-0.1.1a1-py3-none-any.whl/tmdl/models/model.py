import typing as t
from enum import Enum

from pydantic import BaseModel

from .relationship import Relationship
from .table import Table


class Culture(Enum):

    FR = "fr-FR"
    EN = "en-US"


class Model(BaseModel):
    name: str = "Model"
    description: t.Optional[str] = None
    culture: Culture = Culture.EN

    tables: t.List[Table] = []
    relationships: t.Optional[t.List[Relationship]] = None

    def dump(self) -> str:
        """Serialize a Model object into TMDL."""
        model_str = f"""model {self.name}
    culture: {self.culture.value}

"""
        for table in self.tables:
            model_str += f"ref table {table.name}\n"

        return model_str
