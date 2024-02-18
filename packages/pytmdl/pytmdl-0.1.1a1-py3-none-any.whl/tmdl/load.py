from io import TextIOWrapper

from .parsers import parser


def load(stream: str | TextIOWrapper):
    if isinstance(stream, TextIOWrapper):
        text = stream.read()
    else:
        text = stream

    return parser.parse_string(text, parse_all=True).as_dict()
