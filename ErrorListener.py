import unittest
from miParserLexer import *
from miParserParser import *
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def SintaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("ERROR: when parsing line %d column %d: %s\n" % \
                        (line, column, msg))


class TestMyParser(unittest.TestCase):
    def test_with_testfile(self):
        error_listener = MyErrorListener()
        input_stream = FileStream("testfile")
        lexer = miParserLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)
        stream = CommonTokenStream(lexer)
        parser = miParserParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)



