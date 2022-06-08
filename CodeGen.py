from miParserVisitor import miParserVisitor
from miParserParser import miParserParser
from miParserLexer import  miParserLexer

class codeGen(miParserVisitor):

    class Instr:
        def __init__(self, i, a):
            self.instr = i
            self.arg = a

    def __init__(self):
        self.codigo = []
        self.instActual = 0
        self.variablesLocalesDefinidas = []

    def generate(self, instr, arg):
        self.codigo.append(codeGen.Instr(instr, arg))
        self.instActual += 1

    def printCode(self):
        print("----- CODIGO GENERADO ------\n")
        for x in self.codigo:
            print(x.instr, end = '')
            if (x.arg):
                print(" " + x.arg)
            else:
                print("")

    def agregarVariableDefinida(self, nombre, lista):
        if (self.buscarVariableDefinida(nombre,lista) == False):
            lista.append(nombre)

    def buscarVariableDefinida(self, nombre, lista):
        for v in lista:
            if v == nombre:
                return True
        return False

    def visitProgramAST(self, ctx: miParserParser.ProgramASTContext):
        super().visitProgramAST(ctx)
        self.printCode()
        return self.codigo

    #las reglas del stament
    def visitStatementDefStatementAST(self, ctx: miParserParser.StatementDefStatementASTContext):
        return super().visitStatementDefStatementAST(ctx)

    def visitStatementIfStatementAST(self, ctx: miParserParser.StatementIfStatementASTContext):
        return super().visitStatementIfStatementAST(ctx)

    def visitStatementReturnStatementAST(self, ctx: miParserParser.StatementReturnStatementASTContext):
        return super().visitStatementReturnStatementAST(ctx)

    def visitStatementPrintStatementAST(self, ctx: miParserParser.StatementPrintStatementASTContext):
        return super().visitStatementPrintStatementAST(ctx)

    def visitStatementWhileStatementAST(self, ctx: miParserParser.StatementWhileStatementASTContext):
        return super().visitStatementWhileStatementAST(ctx)

    def visitStatementForStatementAST(self, ctx: miParserParser.StatementForStatementASTContext):
        return super().visitStatementForStatementAST(ctx)

    def visitStatementAssignStatementAST(self, ctx: miParserParser.StatementAssignStatementASTContext):
        return super().visitStatementAssignStatementAST(ctx)

    def visitStatementFunctionCallStatementAST(self, ctx: miParserParser.StatementFunctionCallStatementASTContext):
        return super().visitStatementFunctionCallStatementAST(ctx)

    def visitStatementExpressionStatementAST(self, ctx: miParserParser.StatementExpressionStatementASTContext):
        return super().visitStatementExpressionStatementAST(ctx)

    # las reglas del stament ^

    def visitDefStatementAST(self, ctx: miParserParser.DefStatementASTContext):
        self.generate("DEF", ctx.ID().getText())
        if (ctx.argList()):
            self.visit(ctx.argList())
        self.visit(ctx.sequence())
        if (ctx.ID().getText() == "Main"):
            self.generate("END", None)
        else:
            self.generate("RETURN", None)
        return None

    def visitMoreArgListAST(self, ctx: miParserParser.MoreArgListASTContext):
        self.generate("PUSH_LOCAL", ctx.ID().getText())
        self.agregarVariableDefinida(ctx.ID().getText(), self.variablesLocalesDefinidas)

        return super().visitMoreArgsAST(ctx)

    def visitEpsilonArgListAST(self, ctx: miParserParser.EpsilonArgListASTContext):
        return None

    def visitMoreArgsAST(self, ctx: miParserParser.MoreArgsASTContext):
        for i in ctx.ID():
            self.generate("PUSH_LOCAL", i.getText())
            self.agregarVariableDefinida(i.getText(), self.variablesLocalesDefinidas)
        return None

    def visitIfStatement(self, ctx: miParserParser.IfStatementContext):
        self.visit(ctx.expression())
        etiq1 = self.instActual
        self.generate("JUMP_IF_FALSE", "0")
        self.visit(ctx.sequence(0))
        if (ctx.ELSE()):
            etiq2 = self.instActual
            self.generate("JUMP_ABSOLUTE", "0")
            self.codigo[etiq1].arg = str(self.instActual)
            self.visit(ctx.sequence(1))
            self.codigo[etiq2].arg = str(self.instActual)
        else:
            self.codigo[etiq1].arg = str(self.instActual)
        return None

    def visitWhileStatementAST(self, ctx: miParserParser.WhileStatementASTContext):
        etiq1 = self.instActual
        self.generate("JUMP_ABSOLUTE", "0")
        etiq2 = self.instActual
        self.visit(ctx.sequence())
        self.codigo[etiq1].arg = str(self.instActual)
        self.visit(ctx.expression())
        self.generate("JUMP_IF_TRUE", str(etiq2))

        return super().visitWhileStatementAST(ctx)

    def visitForStatementAST(self, ctx: miParserParser.ForStatementASTContext):

        return super().visitForStatementAST(ctx)

    def visitReturnStatementAST(self, ctx: miParserParser.ReturnStatementASTContext):
        self.visit(ctx.expression())
        self.generate("RETURN_VALUE", None)
        return None

    def visitPrintStatementAST(self, ctx: miParserParser.PrintStatementASTContext):
        self.visit(ctx.expression())
        self.generate("LOAD_GLOBAL", "print")
        self.generate("CALL_FUNCTION", "1")
        return None

    def visitAssignStatementAST(self, ctx: miParserParser.AssignStatementASTContext):
        if (self.buscarVariableDefinida(ctx.ID().getText(), self.variablesLocalesDefinidas) == False):
            self.generate("PUSH_LOCAL", ctx.ID().getText())  # NO DEBERÍA HACERSE SIEMPRE EL PUSH
        self.visit(ctx.expression())
        self.generate("STORE_FAST", ctx.ID().getText())
        return None

    def visitFunctionCallStatementAST(self, ctx: miParserParser.FunctionCallStatementASTContext):
        cant_params = 0
        if (ctx.expressionList()):
            cant_params = self.visit(ctx.expressionList())
        self.generate("LOAD_GLOBAL", ctx.ID().getText())
        self.generate("CALL_FUNCTION", str(cant_params))
        return None

    def visitExpressionStatementAST(self, ctx: miParserParser.ExpressionStatementASTContext):
        self.visit(ctx.expressionList())
        return None

    def visitSequenceAST(self, ctx: miParserParser.SequenceASTContext):
        self.visit(ctx.moreStatements())
        return None

    def visitMoreStatementsAST(self, ctx: miParserParser.MoreStatementsASTContext):
        for mS in ctx.getChildren():
            self.visit(mS)
        return None

    def visitExpressionAST(self, ctx: miParserParser.ExpressionASTContext):
        self.visit(ctx.additionExpression())
        self.visit(ctx.comparison())
        return None

    def visitComparisonAST(self, ctx: miParserParser.ComparisonASTContext):
      for i in ctx.getChildren():
          oper = i.getText()
          self.visit(i)
          if oper == "<" or oper == ">" or oper == "<=" or oper == ">=" or oper == "==":
              self.generate("COMPARE_OP", oper)
      '''
      i = 0
      while i < len(ctx.getChildren()):
          oper = ctx.children[i]
          i += 1
          self.visit(ctx.getChild(i))
          self.generate("COMPARE_OP", oper.getText())
          i += 1
      return None '''
    def visitAdditionExpressionAST(self, ctx: miParserParser.AdditionExpressionASTContext):
        self.visit(ctx.multiplicationExpression())
        self.visit(ctx.additionFactor())
        return None

    def visitAdditionFactorAST(self, ctx: miParserParser.AdditionFactorASTContext):
        for i in ctx.getChildren():
            oper = i.getText()
            self.visit(i)
            if (oper == "+"):
                self.generate("BINARY_ADD", None)
            elif (oper == "-"):
                self.generate("BINARY_SUBSTRACT", None)

    def visitMultiplicationExpressionAST(self, ctx: miParserParser.MultiplicationExpressionASTContext):
        self.visit(ctx.elementExpression())
        self.visit(ctx.multiplicationFactor())
        return None

    def visitMultiplicationFactorAST(self, ctx: miParserParser.MultiplicationFactorASTContext):
        for i in ctx.getChildren():
            oper = i.getText()
            self.visit(i)
            # generar operación
            if (oper == "*"):
                self.generate("BINARY_MULTIPLY", None)
            elif (oper == "/"):
                self.generate("BINARY_DIVIDE", None)

    def visitEpsilonMultiplicationExpression(self, ctx: miParserParser.EpsilonMultiplicationExpressionContext):
        return None

    def visitElementExpressionAST(self, ctx: miParserParser.ElementExpressionASTContext):
        self.visit(ctx.primitiveExpression())
        self.visit(ctx.elementAccess())
        return None

    def visitElementAccessAST(self, ctx: miParserParser.ElementAccessASTContext):
        for e in ctx.expression():
            self.visit(e)
        return None

    def visitExpressionListAST(self, ctx: miParserParser.ExpressionListASTContext):
        for e in ctx.expression():
            self.visit(e)
        return len(ctx.expression())

    def visitEpsilonExpressionList(self, ctx: miParserParser.EpsilonExpressionListContext):
        return None

    def visitMoreExpressionsAST(self, ctx: miParserParser.MoreExpressionsASTContext):
        print("mas de una expresion")
        for mE in ctx.getChildren():
            self.visit(mE)
        return None

    def visitPrimitiveExpressionINTLITERAL(self, ctx: miParserParser.PrimitiveExpressionINTLITERALContext):
        self.generate("LOAD_CONST", ctx.INTLITERAL().getText())
        return None
    def visitPrimitiveExpressionFLOATLITERAL(self, ctx: miParserParser.PrimitiveExpressionFLOATLITERALContext):
        self.generate("LOAD_CONST", ctx.FLOATLITERAL().getText())
        return None
    def visitPrimitiveExpressionCHAR_LITERAL(self, ctx: miParserParser.PrimitiveExpressionCHAR_LITERALContext):
        self.generate("LOAD_CONST", ctx.CHAR_LITERAL().getText())
        return None
    def visitPrimitiveExpressionRAWSTRINGLITERAL(self, ctx: miParserParser.PrimitiveExpressionRAWSTRINGLITERALContext):
        self.generate("LOAD_CONST", ctx.RAWSTRINGLITERAL().getText())
        return None
    def visitPrimitiveExpressionID(self, ctx: miParserParser.PrimitiveExpressionIDContext):
        print("Primitive expresion ID")
        if (ctx.expressionList()==None):
            #deberíamos saber si es FAST o GLOBAL
            self.generate("LOAD_FAST",ctx.ID().getText())
        else:
            cant_params = self.visit(ctx.expressionList())
            self.generate("LOAD_GLOBAL", ctx.ID().getText())
            self.generate("CALL_FUNCTION", str(cant_params))
        return None

    def visitPrimitiveExpressionExpression(self, ctx: miParserParser.PrimitiveExpressionExpressionContext):
        return super().visitPrimitiveExpressionExpression(ctx)

    def visitPrimitiveExpressionListExpression(self, ctx: miParserParser.PrimitiveExpressionListExpressionContext):
        self.visit(ctx.listExpression())
        return None

    def visitPrimitiveExpressionLEN(self, ctx: miParserParser.PrimitiveExpressionLENContext):
        cont = 0

        return super().visitPrimitiveExpressionLEN(ctx)

    def visitListExpressionAST(self, ctx: miParserParser.ListExpressionASTContext):

        for i in ctx.getChildren():
            if i.getText() !="[" and i.getText() !="]":
                print(i.getText())
                self.generate("LOAD_CONST", i.getText())

       # cant_params = self.visit(ctx.expressionList())
        self.generate("BUILD_LIST",0)
        return None