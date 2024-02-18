"""database Database
	id: b7d357fe-af44-4083-9e4d-2cb216640a3a
	compatibilityLevel: 1604
	compatibilityMode: powerBI
"""

import typing as t
from enum import Enum

from pydantic import BaseModel, Field

DEFAULT_COMPATIBILITY_LEVEL = 1605


class CompatibilityMode(str, Enum):
    """
    An enumeration of the compatibility modes supported by the various
    AnalysisServices services.
    """

    ANALYSIS_SERVICES = "AnalysisServices"
    EXCEL = "Excel"
    POWERBI = "PowerBI"
    UNKNOWN = "Unknown"


class Database(BaseModel):
    """Specifies an Analysis Services Tabular or PowerBI database."""

    name: str = "Database"
    id: t.Optional[str] = None
    description: t.Optional[str] = Field(
        default=None,
        serialization_alias="Description",
    )
    compatibility_level: int = Field(
        default=DEFAULT_COMPATIBILITY_LEVEL,
        serialization_alias="CompatibilityLevel",
    )
    compatibility_mode: CompatibilityMode = Field(
        default=CompatibilityMode.POWERBI,
        serialization_alias="CompatibilityMode",
    )

    def dump_tmdl(self):
        model_str = ""

        if self.description:
            model_str += f"/// {self.description}\n"

        model_str += f"database {self.name}\n"

        if self.id:
            model_str += f"  ID: {self.id}\n"

        model_str += f"    CompatibilityLevel: {self.compatibility_level}\n"
        model_str += f"    CompatibilityMode: {self.compatibility_mode}\n"

        return model_str
