import pyparsing as pp

objectName = pp.QuotedString("'") | pp.Word(pp.alphanums)
