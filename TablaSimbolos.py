import token

from miParserLexer import *
from miParserParser import *
from antlr4 import *


class TablaSimbolos:
    tabla = [] # tabla de simbolos

    def __init__(self):
        self.tabla = []


    class Ident:
        def __init__(self, token, context, nivel):
            self.token = token
            self.nivel = nivel
            self.contex = context

        def getNivel(self):
            return self.nivel
        def getToken(self):
            return self.token
        def getContexto(self):
            return self.contexto

    def repetido(self, id, nivel):
        aux = False
        for var in range(len(self.tabla)):
            if self.tabla[var].getToken() == id & self.tabla[var].getNivel() == nivel:
                aux = True
        return aux


    #termina la clase ident

    class VarIdent:
        def __init__(self,token, nivel, context):
            self.token = token
            self.nivel = nivel
            self.contex = context

    def InsertarVarIdent(self, token, ctx, nivel):
        if not self.repetido(token,nivel):
            newIdent = self.Ident(token, ctx, nivel)
            self.tabla.__add__(newIdent)
        else:
            # agregar a la clase de errores
            print("La variable ya ha sido declarada")


    #termina la clase VarIdent

    class FuncIdent:
        args = []
        def __init__(self,token, ctx, nivel):
            self.args = []
            self.token = token
            self.nivel = nivel
            self.contex = ctx

        def GetArgs(self):
            return self.args
        def SetArgs(self, args):
            self.args = args

    def InsertarFuncIdent(self, token, ctx, nivel):
        func = self.FuncIdent(token, ctx, nivel)
        self.args.append(func)


    #termina clase FuncIdent


    class ArrayIdent:
        def __init__(self, token, nivel, context):
            self.token = token
            self.nivel = nivel
            self.contex = context

    #termina la clase ArrayIdent