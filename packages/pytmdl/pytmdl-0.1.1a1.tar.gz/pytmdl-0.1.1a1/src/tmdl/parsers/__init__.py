from .column import columnParser
from .table import tableParser

parser = tableParser ^ columnParser
