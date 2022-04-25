import token
from typing import Type

from miParserVisitor import *
from TablaSimbolos import *
from antlr4 import *

class AContextual(miParserVisitor):
    simbTabla: TablaSimbolos


    def __init__(self):
        self.simbTabla =  TablaSimbolos();

    def visitProgramAST(self, ctx: miParserParser.ProgramASTContext):
        super().visit(ctx.statement())
        for i in ctx.singleCommand():
            super().visit(ctx.statement(i))
        return None

    def visitStatementDefStatementAST(self, ctx: miParserParser.StatementDefStatementASTContext):
        super().visitDefStatementAST(ctx)
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
        super().visitAssignStatementAST(ctx)
        return None

    def visitStatementFunctionCallStatementAST(self, ctx: miParserParser.StatementFunctionCallStatementASTContext):
        super().visitFunctionCallStatementAST(ctx)
        return None

    def visitStatementExpressionStatementAST(self, ctx: miParserParser.StatementExpressionStatementASTContext):
        super().visitExpressionAST(ctx)
        return None
##################################################################################################################
    def visitDefStatementAST(self, ctx: miParserParser.DefStatementASTContext):
        #def identifier ( ArgList ) : Sequence
        super().visit(ctx.DEF())
        super().visit(ctx.ID())
        super().visit(ctx.argList(1))
        for i in ctx.argList():
            super().visit(ctx.argList())

        return None

    def visitMoreArgListAST(self, ctx: miParserParser.MoreArgListASTContext):
        super().visit(ctx.moreArgs())
        return None

    def visitEpsilonArgListAST(self, ctx: miParserParser.EpsilonArgListASTContext):
        super().visit(ctx.getTokens())

        return None

    def visitMoreArgsAST(self, ctx: miParserParser.MoreArgsASTContext):
        super().visit(ctx.ID())
        super().visit(ctx.COMA())

        return None

    def visitIfStatement(self, ctx: miParserParser.IfStatementContext):
        #if Expression : Sequence else : Sequence
        super().visit(ctx.IF())
        super().visit(ctx.expression(0))
        super().visit(ctx.ELSE())

        return None

    def visitWhileStatementAST(self, ctx: miParserParser.WhileStatementASTContext):
        #while Expression : Sequence
        super().visit(ctx.WHILE())
        super().visit(ctx.expression())

        return None

    def visitForStatementAST(self, ctx: miParserParser.ForStatementASTContext):
        #for i in list
        t = super().visit(ctx.FOR())
        super().visit(ctx.getTokens())
        super().visit(ctx.IN())
        super().visit(ctx.getTokens())

        var = super().visit(ctx.getToken())

        return None

    def visitReturnStatementAST(self, ctx: miParserParser.ReturnStatementASTContext):
        #return Expression NEWLINE
        super().visit(ctx.RETURN())
        super().visit(ctx.expression())

        return None

    def visitPrintStatementAST(self, ctx: miParserParser.PrintStatementASTContext):
        #print Expression NEWLINE
        super().visit(ctx.PRINT())
        super().visit(ctx.expression())
        return None

    def visitAssignStatementAST(self, ctx: miParserParser.AssignStatementASTContext):
        #identifier = Expression NEWLINE
        super().visit(ctx.ID())
        super().visit(ctx.ASYGN())
        super().visi(ctx.expression())
        return None

    def visitFunctionCallStatementAST(self, ctx: miParserParser.FunctionCallStatementASTContext):
        #PrimitiveExpression ( ExpressionList ) NEWLINE
        super().visit(ctx.getToken())
        super().visit(ctx.primitiveExpression())

        return None

    def visitExpressionStatementAST(self, ctx: miParserParser.ExpressionStatementASTContext):
        #ExpressionList NEWLINE
        super().visit(ctx.expressionList())

        return None

    def visitSequenceAST(self, ctx: miParserParser.SequenceASTContext):
        #INDENT MoreStatements DEDENT
        super().visit(ctx.moreStatements())

        return None

    def visitMoreStatementsAST(self, ctx: miParserParser.MoreStatementsASTContext):
        #statement  statement*
        super().visit(ctx.statement(0))
        #tiene que ser lista de recorrudo
        super().visit(ctx.statement(1))
        return None

    def visitExpressionAST(self, ctx: miParserParser.ExpressionASTContext):
        #additionExpression comparison
        super().visit(ctx.additionExpression())
        super().visit(ctx.comparison())
        return None

    def visitComparisonAST(self, ctx: miParserParser.ComparisonASTContext):
        #( (MENOR|MAYOR|MENORIGUAL|MAYORIGUAL|EQUALS) additionExpression )*
        super().visit(ctx.getToken())
        super().visit(ctx.additionExpression())

        return None

    def visitAdditionExpressionAST(self, ctx: miParserParser.AdditionExpressionASTContext):
        #multiplicationExpression additionFactor
        super().visit(ctx.multiplicationExpression())
        super().visit(ctx.additionFactor())
        return None

    def visitAdditionFactorAST(self, ctx: miParserParser.AdditionFactorASTContext):
        #( (SUM|RES) multiplicationExpression )*
        super().visit(ctx.getToken())
        super().visit(ctx.multiplicationExpression())
        return None


    def visitMultiplicationExpressionAST(self, ctx: miParserParser.MultiplicationExpressionASTContext):
        #elementExpression multiplicationFactor
        super().visit(ctx.elementExpression())
        super().visit(ctx.multiplicationFactor())
        return None

    def visitEpsilonMultiplicationExpression(self, ctx: miParserParser.EpsilonMultiplicationExpressionContext):
        super().visitEpsilonMultiplicationExpression(ctx)
        return None

    def visitMultiplicationFactorAST(self, ctx: miParserParser.MultiplicationFactorASTContext):
        # ( (MUL|DIV) elementExpression )*
        super().visit(ctx.getToken())
        super().visit(ctx.elementExpression())# lista
        return None

    def visitElementExpressionAST(self, ctx: miParserParser.ElementExpressionASTContext):
        #primitiveExpression elementAccess
        super().visit(ctx.primitiveExpression())
        super().visit(ctx.elementAccess())
        return None

    def visitElementAccessAST(self, ctx: miParserParser.ElementAccessASTContext):
        #(BRACKETIZQ expression BRACKETDER)*
        super().visit(ctx.expression()) #lista

        return None

    def visitExpressionListAST(self, ctx: miParserParser.ExpressionListASTContext):
        # expression moreExpressions
        super().visit(ctx.moreExpressions())
        return None

    def visitEpsilonExpressionList(self, ctx: miParserParser.EpsilonExpressionListContext):
        super().visitEpsilonExpressionList(ctx)
        return None

    def visitMoreExpressionsAST(self, ctx: miParserParser.MoreExpressionsASTContext):
        #(COMA expression)*
        super().visit(ctx.expression(0))# lista
        return None

    def visitPrimitiveExpressionINTLITERAL(self, ctx: miParserParser.PrimitiveExpressionINTLITERALContext):
        #INTLITERAL
        super().visitPrimitiveExpressionINTLITERAL(ctx)
        return None

    def visitPrimitiveExpressionFLOATLITERAL(self, ctx: miParserParser.PrimitiveExpressionFLOATLITERALContext):
        #FLOATLITERAL
        super().visitPrimitiveExpressionFLOATLITERAL(ctx)
        return None

    def visitPrimitiveExpressionCHAR_LITERAL(self, ctx: miParserParser.PrimitiveExpressionCHAR_LITERALContext):
        #CHAR_LITERAL
        super().visitPrimitiveExpressionCHAR_LITERAL(ctx)
        return None

    def visitPrimitiveExpressionRAWSTRINGLITERAL(self, ctx: miParserParser.PrimitiveExpressionRAWSTRINGLITERALContext):
        #RAWSTRINGLITERAL
        super().visitPrimitiveExpressionRAWSTRINGLITERAL(ctx)
        return None

    def visitPrimitiveExpressionID(self, ctx: miParserParser.PrimitiveExpressionIDContext):
        #ID (PARENTESISIZQ expressionList PARENTESISDER |   )
        super().visit(ctx.ID())
        super().visit(ctx.expressionList())
        return None

    def visitPrimitiveExpressionExpression(self, ctx: miParserParser.PrimitiveExpressionExpressionContext):
        #PARENTESISIZQ expression PARENTESISDER
        super().visit(ctx.expression())
        return None

    def visitPrimitiveExpressionListExpression(self, ctx: miParserParser.PrimitiveExpressionListExpressionContext):
        #listExpression
        super().visit(ctx.listExpression())

        return None

    def visitPrimitiveExpressionLEN(self, ctx: miParserParser.PrimitiveExpressionLENContext):
        #LEN PARENTESISIZQ expression PARENTESISDER
        super().visit(ctx.expression())
        return None

    def visitListExpressionAST(self, ctx: miParserParser.ListExpressionASTContext):
        #BRACKETIZQ expressionList BRACKETDER
        super().visit(ctx.expressionList())
        return None
