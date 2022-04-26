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

    def InsertarVarIdent(self, token, ctx, nivel):
        if not self.repetido(token,nivel):
            newIdent = self.Ident(token, ctx, nivel)
            self.tabla.__add__(newIdent)
        else:
            # agregar a la clase de errores
            print("La variable ya ha sido declarada")


    #termina la clase ident

    class VarIdent(Ident):
        def __init__(self,token, nivel, context):
            self.token = token
            self.nivel = nivel
            self.contex = context


    #termina la clase VarIdent

    class ArrayIdent(Ident):
        def __init__(self, token, nivel, context):
            self.token = token
            self.nivel = nivel
            self.contex = context
