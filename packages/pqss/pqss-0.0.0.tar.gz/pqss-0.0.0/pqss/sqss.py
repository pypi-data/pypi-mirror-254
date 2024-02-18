import os.path

from .lex import *
from .env import *
from .parse import *


def compile_sqss(source: str) -> str:
    if os.path.isfile(source):
        source = read_file(source)

    compiler = Parser(Lexer(source))
    style_sheet = compiler.parse_sqss()
    qss = style_sheet.eval(Environment())
    return qss


def read_file(p: str):
    res = ''
    with open(p, 'r') as f:
        res = f.read()
    return res

