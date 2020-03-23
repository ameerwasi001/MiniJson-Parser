import sys
from Tokens import *
from Parser import Parser
from Lexer import Lexer

def run(text):
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    ast = parser.parse()
    return ast

print(run(open(sys.argv[1]).read()))
