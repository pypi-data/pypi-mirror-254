import pyparsing as pp

from .base import objectName

columnName = pp.Suppress("column") + objectName("name")

# Boolean #

isKey = pp.Keyword("isKey")("is_key")
isKey.set_parse_action(lambda _: True)

isNameInferred = pp.Keyword("isNameInferred")("is_name_inferred")
isNameInferred.set_parse_action(lambda _: True)

# String #

dataType = (
    pp.Suppress("dataType:")
    + pp.ZeroOrMore(" ")  # potential spaces
    + pp.restOfLine("data_type")
)

summarizeBy = (
    pp.Suppress("summarizeBy:")
    + pp.ZeroOrMore(" ")  # potential spaces
    + pp.restOfLine("summarize_by")
)

formatString = (
    pp.Suppress("formatString:")
    + pp.ZeroOrMore(" ")  # potential spaces
    + pp.restOfLine("format_string")
)

sourceColumn = (
    pp.Suppress("sourceColumn:")
    + pp.ZeroOrMore(" ")  # potential spaces
    + pp.restOfLine("source_column")
)

annotation = pp.Keyword("annotation") + pp.restOfLine

# Full Column #

columnParser = (
    columnName
    & pp.Opt(dataType)
    & pp.Opt(isKey)
    & pp.Opt(formatString)
    & pp.Opt(summarizeBy)
    & pp.Opt(isNameInferred)
    & pp.Opt(sourceColumn)
    & pp.Suppress(pp.ZeroOrMore(annotation))
)
"""A column is a name followed by properties without any specific order"""
