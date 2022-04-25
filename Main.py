from miParserLexer import *
from miParserParser import *
from antlr4 import *
from ErrorListener import *

def main():
    input = FileStream('test.py')
    lexer = miParserLexer(input)
    lexer._listeners = [errorLexer()]
    stream = CommonTokenStream(lexer)
    parser = miParserParser(stream)
    parser._listeners = [errorParser()]
    tree = parser.program()

if __name__ == '__main__':
    main()