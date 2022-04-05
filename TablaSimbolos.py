from antlr4 import *

class TablaSimbolos:

    tabla = []

    nivelActual =0

    class Ident:
        token = None
        type = 0
        nivel = 0
        valor = 0
        #ParserRuleContext declCtx

        def Ident( t, tp, decl):
            tok = None
            type = tp
            valor = 0
            declCtx=decl


        def setValue(v):
            valor = v



    def TablaSimbolos(self):
        tabla = []
        nivelActual=-1;



