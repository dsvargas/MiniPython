from miParserLexer import *
from miParserParser import *
from antlr4 import *
from ErrorListener import *
from AnalisisContextual import*

from CodeGen import *

import os

def generar_bytecode(codigo):
    f = open('bytecode.txt', 'w')
    cont = 0
    for instr in codigo:
        if (instr.arg == None):
            f.write("{} {}\n".format(str(cont), instr.instr))
        else:
            f.write("{} {} {}\n".format(str(cont), instr.instr, instr.arg))
        cont += 1
    f.close()


def main():
    input = FileStream('prueba.txt')
    lexer = miParserLexer(input)
    lexer._listeners = [errorLexer()]
    stream = CommonTokenStream(lexer)
    parser = miParserParser(stream)
    parser._listeners = [errorParser()]
   # mv = AContextual()
    tree = parser.program()
    #mv.visit(tree)
    gc = codeGen()
    #gc.visit(tree)
    generar_bytecode(gc.visit(tree))

    #os.system("MiniPY.exe bytecode.txt")


if __name__ == '__main__':
    main()