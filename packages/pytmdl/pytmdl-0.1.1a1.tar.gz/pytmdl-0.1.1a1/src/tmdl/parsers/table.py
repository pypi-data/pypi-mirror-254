import pyparsing as pp

from .base import objectName
from .column import columnParser

tableName = pp.Suppress("table") + objectName("name")

# Properties #

dataCategory = (
    pp.Suppress("dataCategory:")
    + pp.ZeroOrMore(" ")  # potential spaces
    + pp.restOfLine("data_category")
)

# Columns #

columns = pp.OneOrMore(pp.Group(columnParser))("columns")

# Final #

tableParser = tableName & pp.Opt(dataCategory) & columns
