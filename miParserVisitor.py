# Generated from C:/Users/dilan/OneDrive - Estudiantes ITCR/Semestre I 2022/Compiladores/Proyecto/Proyecto/MiniPython\miParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .miParserParser import miParserParser
else:
    from miParserParser import miParserParser

# This class defines a complete generic visitor for a parse tree produced by miParserParser.

class miParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by miParserParser#program.
    def visitProgram(self, ctx:miParserParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#statement.
    def visitStatement(self, ctx:miParserParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#defStatement.
    def visitDefStatement(self, ctx:miParserParser.DefStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#argList.
    def visitArgList(self, ctx:miParserParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#moreArgs.
    def visitMoreArgs(self, ctx:miParserParser.MoreArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#ifStatement.
    def visitIfStatement(self, ctx:miParserParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#whileStatement.
    def visitWhileStatement(self, ctx:miParserParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#forStatement.
    def visitForStatement(self, ctx:miParserParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#returnStatement.
    def visitReturnStatement(self, ctx:miParserParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#printStatement.
    def visitPrintStatement(self, ctx:miParserParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#assignStatement.
    def visitAssignStatement(self, ctx:miParserParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#functionCallStatement.
    def visitFunctionCallStatement(self, ctx:miParserParser.FunctionCallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#expressionStatement.
    def visitExpressionStatement(self, ctx:miParserParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#sequence.
    def visitSequence(self, ctx:miParserParser.SequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#moreStatements.
    def visitMoreStatements(self, ctx:miParserParser.MoreStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#expression.
    def visitExpression(self, ctx:miParserParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#comparison.
    def visitComparison(self, ctx:miParserParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#additionExpression.
    def visitAdditionExpression(self, ctx:miParserParser.AdditionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#additionFactor.
    def visitAdditionFactor(self, ctx:miParserParser.AdditionFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#multiplicationExpression.
    def visitMultiplicationExpression(self, ctx:miParserParser.MultiplicationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#multiplicationFactor.
    def visitMultiplicationFactor(self, ctx:miParserParser.MultiplicationFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#elementExpression.
    def visitElementExpression(self, ctx:miParserParser.ElementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#elementAccess.
    def visitElementAccess(self, ctx:miParserParser.ElementAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#expressionList.
    def visitExpressionList(self, ctx:miParserParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#moreExpressions.
    def visitMoreExpressions(self, ctx:miParserParser.MoreExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#primitiveExpression.
    def visitPrimitiveExpression(self, ctx:miParserParser.PrimitiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miParserParser#listExpression.
    def visitListExpression(self, ctx:miParserParser.ListExpressionContext):
        return self.visitChildren(ctx)



del miParserParser