from miParserLexer import *
from miParserParser import *
from antlr4 import *
from ErrorListener import *
from AnalisisContextual import*

def main():
    input = FileStream('test.py')
    lexer = miParserLexer(input)
    lexer._listeners = [errorLexer()]
    stream = CommonTokenStream(lexer)
    parser = miParserParser(stream)
    parser._listeners = [errorParser()]
    mv = AContextual()
    tree = parser.program()
    mv.visit(tree)


if __name__ == '__main__':
    main()