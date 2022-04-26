import token
from miParserVisitor import *
from TablaSimbolos import *

from antlr4 import *

class AContextual(miParserVisitor):
    tablaSimb = TablaSimbolos()
    errorMsgs = []
    nivelActual = 0

    def visitProgramAST(self, ctx: miParserParser.ProgramASTContext):

        self.visit(ctx.statement(0))
        for i in range(1, len(ctx.statement())):
            self.visit(ctx.statement(i))
            print(ctx.statement(i).getText())

        return None

    def visitStatementDefStatementAST(self, ctx: miParserParser.StatementDefStatementASTContext):
        self.visitDefStatementAST(ctx)
        return None

    def visitStatementIfStatementAST(self, ctx: miParserParser.StatementIfStatementASTContext):
        super().visitIfStatement(ctx)
        return None

    def visitStatementReturnStatementAST(self, ctx: miParserParser.StatementReturnStatementASTContext):
        super().visitReturnStatementAST(ctx)
        return None

    def visitStatementPrintStatementAST(self, ctx: miParserParser.StatementPrintStatementASTContext):
        super().visitPrintStatementAST(ctx)
        return None

    def visitStatementWhileStatementAST(self, ctx: miParserParser.StatementWhileStatementASTContext):
        super().visitWhileStatementAST(ctx)
        return None

    def visitStatementForStatementAST(self, ctx: miParserParser.StatementForStatementASTContext):
        super().visitForStatementAST(ctx)
        return None

    def visitStatementAssignStatementAST(self, ctx: miParserParser.StatementAssignStatementASTContext):
        self.visitAssignStatementAST(ctx)
        return None

    def visitStatementFunctionCallStatementAST(self, ctx: miParserParser.StatementFunctionCallStatementASTContext):
        super().visitFunctionCallStatementAST(ctx)
        return None

    def visitStatementExpressionStatementAST(self, ctx: miParserParser.StatementExpressionStatementASTContext):
        super().visitExpressionAST(ctx)
        return None
##################################################################################################################
    def visitDefStatementAST(self, ctx: miParserParser.DefStatementASTContext):
        #DEF ID PARENTESISIZQ argList PARENTESISDER DOSPUNTOS sequence
        self.visit(ctx.argList())
        self.visit(ctx.sequence())

        return None

    def visitMoreArgListAST(self, ctx: miParserParser.MoreArgListASTContext):
        super().visitMoreArgsAST(ctx)
        return None

    def visitEpsilonArgListAST(self, ctx: miParserParser.EpsilonArgListASTContext):
        return None

    def visitMoreArgsAST(self, ctx: miParserParser.MoreArgsASTContext):
        #Meter a la tabla (COMA ID)*
        return None

    def visitIfStatement(self, ctx: miParserParser.IfStatementContext):
        #IF expression DOSPUNTOS sequence ( ELSE DOSPUNTOS sequence | )
        self.visit(ctx.IF())
        self.visit(ctx.expression())

        #self.visit(ctx.sequence())
        # else visitar sequence
        return None

    def visitWhileStatementAST(self, ctx: miParserParser.WhileStatementASTContext):
        #while Expression : Sequence
        self.visit(ctx.expression())
        self.visit(ctx.sequence())
        return None

    def visitForStatementAST(self, ctx: miParserParser.ForStatementASTContext):
        #for i in list
        '''t = super().visit(ctx.FOR())
        var = super().visit(ctx.getToken())'''
        self.visit(ctx.expression())
        self.visit(ctx.expressionList())
        self.visit(ctx.sequence())

        return None

    def visitReturnStatementAST(self, ctx: miParserParser.ReturnStatementASTContext):
        #return Expression NEWLINE
        self.visit(ctx.expression())
        return None

    def visitPrintStatementAST(self, ctx: miParserParser.PrintStatementASTContext):
        #PRINT PARENTESISIZQ expression PARENTESISDER NEWLINE
        self.visit(ctx.expression())

        return None

    def visitAssignStatementAST(self, ctx: miParserParser.AssignStatementASTContext):
        #identifier = Expression NEWLINE
        self.tablaSimb.InsertarVarIdent(ctx.getToken(()), ctx, self.nivelActual)
        self.visit(ctx.expression())
        return None


    def visitFunctionCallStatementAST(self, ctx: miParserParser.FunctionCallStatementASTContext):
        #PrimitiveExpression ( ExpressionList ) NEWLINE
        self.visit(ctx.primitiveExpression())
        self.visit(ctx.expressionList())
        return None

    def visitExpressionStatementAST(self, ctx: miParserParser.ExpressionStatementASTContext):
        #ExpressionList NEWLINE
        self.visit(ctx.expressionList())
        return None

    def visitSequenceAST(self, ctx: miParserParser.SequenceASTContext):
        #INDENT MoreStatements DEDENT
        self.visit(ctx.moreStatements())
        return None

    def visitMoreStatementsAST(self, ctx: miParserParser.MoreStatementsASTContext):
        #statement  statement*
        #self.visit(ctx.moreStatements())
        for i in ctx.statement():
            self.visit(i)
        return None

    def visitExpressionAST(self, ctx: miParserParser.ExpressionASTContext):
        #additionExpression comparison
        self.visit(ctx.additionExpression())
        self.visit(ctx.comparison())
        return None

    def visitComparisonAST(self, ctx: miParserParser.ComparisonASTContext):
        #( (MENOR|MAYOR|MENORIGUAL|MAYORIGUAL|EQUALS) additionExpression )*
        for i in ctx.additionExpression():
            self.visit(i)
        return None

    def visitAdditionExpressionAST(self, ctx: miParserParser.AdditionExpressionASTContext):
        #multiplicationExpression additionFactor
        self.visit(ctx.multiplicationExpression())
        self.visit(ctx.additionFactor())
        return None

    def visitAdditionFactorAST(self, ctx: miParserParser.AdditionFactorASTContext):
        #( (SUM|RES) multiplicationExpression )*
        for i in ctx.multiplicationExpression():
            self.visit(i)
        return None

    def visitMultiplicationExpressionAST(self, ctx: miParserParser.MultiplicationExpressionASTContext):
        #elementExpression multiplicationFactor
        self.visit(ctx.elementExpression())
        self.visit(ctx.multiplicationFactor())
        return None

    def visitEpsilonMultiplicationExpression(self, ctx: miParserParser.EpsilonMultiplicationExpressionContext):
        return None

    def visitMultiplicationFactorAST(self, ctx: miParserParser.MultiplicationFactorASTContext):
        # ( (MUL|DIV) elementExpression )*
        for i in ctx.elementExpression():
            self.visit(i)
        return None

    def visitElementExpressionAST(self, ctx: miParserParser.ElementExpressionASTContext):
        #primitiveExpression elementAccess
        self.visit(ctx.primitiveExpression())
        self.visit(ctx.elementAccess())

        return None

    def visitElementAccessAST(self, ctx: miParserParser.ElementAccessASTContext):
        #(BRACKETIZQ expression BRACKETDER)*
        #self.visit(ctx.expression())
        for i in ctx.expression():
            self.visit(i)
        return None

    def visitExpressionListAST(self, ctx: miParserParser.ExpressionListASTContext):
        # expression moreExpressions
        self.visit(ctx.expression())
        self.visit(ctx.moreExpressions())
        return None

    def visitEpsilonExpressionList(self, ctx: miParserParser.EpsilonExpressionListContext):
        return None

    def visitMoreExpressionsAST(self, ctx: miParserParser.MoreExpressionsASTContext):
        #(COMA expression)*
        for i in ctx.expression():
            self.visit(i)
        return None

    def visitPrimitiveExpressionINTLITERAL(self, ctx: miParserParser.PrimitiveExpressionINTLITERALContext):
        #INTLITERAL
        #Añadir a la lista
        return None

    def visitPrimitiveExpressionFLOATLITERAL(self, ctx: miParserParser.PrimitiveExpressionFLOATLITERALContext):
        #FLOATLITERAL
        #Añadir a la lista
        return None

    def visitPrimitiveExpressionCHAR_LITERAL(self, ctx: miParserParser.PrimitiveExpressionCHAR_LITERALContext):
        #CHAR_LITERAL
        #Añadir a la lista
        return None

    def visitPrimitiveExpressionRAWSTRINGLITERAL(self, ctx: miParserParser.PrimitiveExpressionRAWSTRINGLITERALContext):
        #RAWSTRINGLITERAL
        #Añadir a la lista
        return None

    def visitPrimitiveExpressionID(self, ctx: miParserParser.PrimitiveExpressionIDContext):
        #ID (PARENTESISIZQ expressionList PARENTESISDER |   )
       #self.visit(ctx.expressionList())
        return None

    def visitPrimitiveExpressionExpression(self, ctx: miParserParser.PrimitiveExpressionExpressionContext):
        #PARENTESISIZQ expression PARENTESISDER
        self.visit(ctx.expression())
        return None

    def visitPrimitiveExpressionListExpression(self, ctx: miParserParser.PrimitiveExpressionListExpressionContext):
        #listExpression
        self.visit(ctx.listExpression())
        return None

    def visitPrimitiveExpressionLEN(self, ctx: miParserParser.PrimitiveExpressionLENContext):
        #LEN PARENTESISIZQ expression PARENTESISDER
        self.visit(ctx.expression())
        return None

    def visitListExpressionAST(self, ctx: miParserParser.ListExpressionASTContext):
        #BRACKETIZQ expressionList BRACKETDER
        self.visit(ctx.expressionList())
        return None

