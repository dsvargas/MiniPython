from miParserLexer import *
from miParserParser import *
from antlr4 import *

def main():
    input = FileStream('test.txt')
    lexer = miParserLexer(input)
    stream = CommonTokenStream(lexer)
    parser = miParserParser(stream)
    tree = parser.program()

if __name__ == '__main__':
    main()