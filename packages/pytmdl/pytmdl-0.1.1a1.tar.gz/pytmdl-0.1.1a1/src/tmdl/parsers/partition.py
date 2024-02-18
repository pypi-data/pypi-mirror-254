import pyparsing as pp

from .base import objectName

partitionName = pp.Suppress("partition") + objectName("name")

mode = (
    pp.Suppress("mode:")
    + pp.ZeroOrMore(" ")  # potential spaces
    + pp.restOfLine("mode")
)

sourceLine = pp.Word(pp.printables) + pp.Keyword("=") + pp.restOfLine + pp.LineEnd

source = (
    pp.Suppress(pp.Keyword("source"))
    + pp.Suppress(pp.Keyword("="))
    + pp.Suppress(pp.Keyword("let"))
    + pp.OneOrMore(sourceLine)("source")
    + pp.Suppress(pp.Keyword("in"))
    + pp.Suppress(pp.restOfLine)
)


partitionParser = partitionName & mode & source
