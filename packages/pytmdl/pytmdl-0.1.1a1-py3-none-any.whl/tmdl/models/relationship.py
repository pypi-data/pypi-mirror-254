"""relationship cdc1f678-516d-402a-8bd3-13b1df211879
	isActive: false
	fromColumn: Sales.'Delivery Date'
	toColumn: Date.Date
"""

from enum import Enum

from pydantic import BaseModel


class Cardinality(Enum):

    ONE = "One"
    MANY = "Many"


class Relationship(BaseModel):
    name: str
    from_column: str
    from_cardinality: Cardinality
    to_column: str
    to_cardinality: Cardinality
    state: str = "Ready"
    is_active: bool = True
