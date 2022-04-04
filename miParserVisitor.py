# Generated from C:/Users/dilan/OneDrive - Estudiantes ITCR/Semestre I 2022/Compiladores/Proyecto/Proyecto/MiniPython\miParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miParserParser import miParserParser
else:
    from miParserParser import miParserParser

# This class defines a complete generic visitor for a parse tree produced by miParserParser.

class miParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by miParserParser#programAST.
    def visitProgramAST(self, ctx:miParserParser.ProgramASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#statementDefStatementAST.
    def visitStatementDefStatementAST(self, ctx:miParserParser.StatementDefStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#statementIfStatementAST.
    def visitStatementIfStatementAST(self, ctx:miParserParser.StatementIfStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#statementReturnStatementAST.
    def visitStatementReturnStatementAST(self, ctx:miParserParser.StatementReturnStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#statementPrintStatementAST.
    def visitStatementPrintStatementAST(self, ctx:miParserParser.StatementPrintStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#statementWhileStatementAST.
    def visitStatementWhileStatementAST(self, ctx:miParserParser.StatementWhileStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#statementForStatementAST.
    def visitStatementForStatementAST(self, ctx:miParserParser.StatementForStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#statementAssignStatementAST.
    def visitStatementAssignStatementAST(self, ctx:miParserParser.StatementAssignStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#statementFunctionCallStatementAST.
    def visitStatementFunctionCallStatementAST(self, ctx:miParserParser.StatementFunctionCallStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#statementExpressionStatementAST.
    def visitStatementExpressionStatementAST(self, ctx:miParserParser.StatementExpressionStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#defStatementAST.
    def visitDefStatementAST(self, ctx:miParserParser.DefStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#moreArgListAST.
    def visitMoreArgListAST(self, ctx:miParserParser.MoreArgListASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#epsilonArgListAST.
    def visitEpsilonArgListAST(self, ctx:miParserParser.EpsilonArgListASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#moreArgsAST.
    def visitMoreArgsAST(self, ctx:miParserParser.MoreArgsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#ifStatement.
    def visitIfStatement(self, ctx:miParserParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#whileStatementAST.
    def visitWhileStatementAST(self, ctx:miParserParser.WhileStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#forStatementAST.
    def visitForStatementAST(self, ctx:miParserParser.ForStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#returnStatementAST.
    def visitReturnStatementAST(self, ctx:miParserParser.ReturnStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#printStatementAST.
    def visitPrintStatementAST(self, ctx:miParserParser.PrintStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#assignStatementAST.
    def visitAssignStatementAST(self, ctx:miParserParser.AssignStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#functionCallStatementAST.
    def visitFunctionCallStatementAST(self, ctx:miParserParser.FunctionCallStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#expressionStatementAST.
    def visitExpressionStatementAST(self, ctx:miParserParser.ExpressionStatementASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#sequenceAST.
    def visitSequenceAST(self, ctx:miParserParser.SequenceASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#moreStatementsAST.
    def visitMoreStatementsAST(self, ctx:miParserParser.MoreStatementsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#expressionAST.
    def visitExpressionAST(self, ctx:miParserParser.ExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#comparisonAST.
    def visitComparisonAST(self, ctx:miParserParser.ComparisonASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#additionExpressionAST.
    def visitAdditionExpressionAST(self, ctx:miParserParser.AdditionExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#additionFactorAST.
    def visitAdditionFactorAST(self, ctx:miParserParser.AdditionFactorASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#multiplicationExpressionAST.
    def visitMultiplicationExpressionAST(self, ctx:miParserParser.MultiplicationExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#epsilonMultiplicationExpression.
    def visitEpsilonMultiplicationExpression(self, ctx:miParserParser.EpsilonMultiplicationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#multiplicationFactorAST.
    def visitMultiplicationFactorAST(self, ctx:miParserParser.MultiplicationFactorASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#elementExpressionAST.
    def visitElementExpressionAST(self, ctx:miParserParser.ElementExpressionASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#elementAccessAST.
    def visitElementAccessAST(self, ctx:miParserParser.ElementAccessASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#expressionListAST.
    def visitExpressionListAST(self, ctx:miParserParser.ExpressionListASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#epsilonExpressionList.
    def visitEpsilonExpressionList(self, ctx:miParserParser.EpsilonExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#moreExpressionsAST.
    def visitMoreExpressionsAST(self, ctx:miParserParser.MoreExpressionsASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#primitiveExpressionINTLITERAL.
    def visitPrimitiveExpressionINTLITERAL(self, ctx:miParserParser.PrimitiveExpressionINTLITERALContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#primitiveExpressionFLOATLITERAL.
    def visitPrimitiveExpressionFLOATLITERAL(self, ctx:miParserParser.PrimitiveExpressionFLOATLITERALContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#primitiveExpressionCHAR_LITERAL.
    def visitPrimitiveExpressionCHAR_LITERAL(self, ctx:miParserParser.PrimitiveExpressionCHAR_LITERALContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#primitiveExpressionRAWSTRINGLITERAL.
    def visitPrimitiveExpressionRAWSTRINGLITERAL(self, ctx:miParserParser.PrimitiveExpressionRAWSTRINGLITERALContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#primitiveExpressionID.
    def visitPrimitiveExpressionID(self, ctx:miParserParser.PrimitiveExpressionIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#primitiveExpressionExpression.
    def visitPrimitiveExpressionExpression(self, ctx:miParserParser.PrimitiveExpressionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#primitiveExpressionListExpression.
    def visitPrimitiveExpressionListExpression(self, ctx:miParserParser.PrimitiveExpressionListExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#primitiveExpressionLEN.
    def visitPrimitiveExpressionLEN(self, ctx:miParserParser.PrimitiveExpressionLENContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#listExpressionAST.
    def visitListExpressionAST(self, ctx:miParserParser.ListExpressionASTContext):
        return self.visitChildren(ctx)



del miParserParser