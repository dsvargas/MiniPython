
from antlr4.error.ErrorListener import *

class MyErrorListener(ErrorListener):
    def SintaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("ERROR: when parsing line %d column %d: %s\n" % \
                        (line, column, msg))


class errorLexer( ErrorListener ):

    def __init__(self):
        super(errorLexer, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print ("LEXER ERROR: ", line,  column,
               "Mensaje: ", msg)
        sys.exit()


#Mostrar Mensaje Error proveniente del Parser
class errorParser( ErrorListener ):

    def __init__(self):
        super(errorParser, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("SINTAX ERROR: ", line, column,
              "Mensaje: ", msg)
        sys.exit()


