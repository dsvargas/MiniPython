# Generated from C:/Users/caohi/Desktop/2022/Compi/Proyectos/Proyecto/MiniPython\miParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from miParserParser import miParserParser
else:
    from miParserParser import miParserParser

# This class defines a complete listener for a parse tree produced by miParserParser.
class miParserListener(ParseTreeListener):

    # Enter a parse tree produced by miParserParser#program.
    def enterProgram(self, ctx:miParserParser.ProgramContext):
        pass

    # Exit a parse tree produced by miParserParser#program.
    def exitProgram(self, ctx:miParserParser.ProgramContext):
        pass


    # Enter a parse tree produced by miParserParser#statement.
    def enterStatement(self, ctx:miParserParser.StatementContext):
        pass

    # Exit a parse tree produced by miParserParser#statement.
    def exitStatement(self, ctx:miParserParser.StatementContext):
        pass


    # Enter a parse tree produced by miParserParser#defStatement.
    def enterDefStatement(self, ctx:miParserParser.DefStatementContext):
        pass

    # Exit a parse tree produced by miParserParser#defStatement.
    def exitDefStatement(self, ctx:miParserParser.DefStatementContext):
        pass


    # Enter a parse tree produced by miParserParser#argList.
    def enterArgList(self, ctx:miParserParser.ArgListContext):
        pass

    # Exit a parse tree produced by miParserParser#argList.
    def exitArgList(self, ctx:miParserParser.ArgListContext):
        pass


    # Enter a parse tree produced by miParserParser#moreArgs.
    def enterMoreArgs(self, ctx:miParserParser.MoreArgsContext):
        pass

    # Exit a parse tree produced by miParserParser#moreArgs.
    def exitMoreArgs(self, ctx:miParserParser.MoreArgsContext):
        pass


    # Enter a parse tree produced by miParserParser#ifStatement.
    def enterIfStatement(self, ctx:miParserParser.IfStatementContext):
        pass

    # Exit a parse tree produced by miParserParser#ifStatement.
    def exitIfStatement(self, ctx:miParserParser.IfStatementContext):
        pass


    # Enter a parse tree produced by miParserParser#whileStatement.
    def enterWhileStatement(self, ctx:miParserParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by miParserParser#whileStatement.
    def exitWhileStatement(self, ctx:miParserParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by miParserParser#forStatement.
    def enterForStatement(self, ctx:miParserParser.ForStatementContext):
        pass

    # Exit a parse tree produced by miParserParser#forStatement.
    def exitForStatement(self, ctx:miParserParser.ForStatementContext):
        pass


    # Enter a parse tree produced by miParserParser#returnStatement.
    def enterReturnStatement(self, ctx:miParserParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by miParserParser#returnStatement.
    def exitReturnStatement(self, ctx:miParserParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by miParserParser#printStatement.
    def enterPrintStatement(self, ctx:miParserParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by miParserParser#printStatement.
    def exitPrintStatement(self, ctx:miParserParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by miParserParser#assignStatement.
    def enterAssignStatement(self, ctx:miParserParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by miParserParser#assignStatement.
    def exitAssignStatement(self, ctx:miParserParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by miParserParser#functionCallStatement.
    def enterFunctionCallStatement(self, ctx:miParserParser.FunctionCallStatementContext):
        pass

    # Exit a parse tree produced by miParserParser#functionCallStatement.
    def exitFunctionCallStatement(self, ctx:miParserParser.FunctionCallStatementContext):
        pass


    # Enter a parse tree produced by miParserParser#expressionStatement.
    def enterExpressionStatement(self, ctx:miParserParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by miParserParser#expressionStatement.
    def exitExpressionStatement(self, ctx:miParserParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by miParserParser#sequence.
    def enterSequence(self, ctx:miParserParser.SequenceContext):
        pass

    # Exit a parse tree produced by miParserParser#sequence.
    def exitSequence(self, ctx:miParserParser.SequenceContext):
        pass


    # Enter a parse tree produced by miParserParser#moreStatements.
    def enterMoreStatements(self, ctx:miParserParser.MoreStatementsContext):
        pass

    # Exit a parse tree produced by miParserParser#moreStatements.
    def exitMoreStatements(self, ctx:miParserParser.MoreStatementsContext):
        pass


    # Enter a parse tree produced by miParserParser#expression.
    def enterExpression(self, ctx:miParserParser.ExpressionContext):
        pass

    # Exit a parse tree produced by miParserParser#expression.
    def exitExpression(self, ctx:miParserParser.ExpressionContext):
        pass


    # Enter a parse tree produced by miParserParser#comparison.
    def enterComparison(self, ctx:miParserParser.ComparisonContext):
        pass

    # Exit a parse tree produced by miParserParser#comparison.
    def exitComparison(self, ctx:miParserParser.ComparisonContext):
        pass


    # Enter a parse tree produced by miParserParser#additionExpression.
    def enterAdditionExpression(self, ctx:miParserParser.AdditionExpressionContext):
        pass

    # Exit a parse tree produced by miParserParser#additionExpression.
    def exitAdditionExpression(self, ctx:miParserParser.AdditionExpressionContext):
        pass


    # Enter a parse tree produced by miParserParser#additionFactor.
    def enterAdditionFactor(self, ctx:miParserParser.AdditionFactorContext):
        pass

    # Exit a parse tree produced by miParserParser#additionFactor.
    def exitAdditionFactor(self, ctx:miParserParser.AdditionFactorContext):
        pass


    # Enter a parse tree produced by miParserParser#multiplicationExpression.
    def enterMultiplicationExpression(self, ctx:miParserParser.MultiplicationExpressionContext):
        pass

    # Exit a parse tree produced by miParserParser#multiplicationExpression.
    def exitMultiplicationExpression(self, ctx:miParserParser.MultiplicationExpressionContext):
        pass


    # Enter a parse tree produced by miParserParser#multiplicationFactor.
    def enterMultiplicationFactor(self, ctx:miParserParser.MultiplicationFactorContext):
        pass

    # Exit a parse tree produced by miParserParser#multiplicationFactor.
    def exitMultiplicationFactor(self, ctx:miParserParser.MultiplicationFactorContext):
        pass


    # Enter a parse tree produced by miParserParser#elementExpression.
    def enterElementExpression(self, ctx:miParserParser.ElementExpressionContext):
        pass

    # Exit a parse tree produced by miParserParser#elementExpression.
    def exitElementExpression(self, ctx:miParserParser.ElementExpressionContext):
        pass


    # Enter a parse tree produced by miParserParser#elementAccess.
    def enterElementAccess(self, ctx:miParserParser.ElementAccessContext):
        pass

    # Exit a parse tree produced by miParserParser#elementAccess.
    def exitElementAccess(self, ctx:miParserParser.ElementAccessContext):
        pass


    # Enter a parse tree produced by miParserParser#expressionList.
    def enterExpressionList(self, ctx:miParserParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by miParserParser#expressionList.
    def exitExpressionList(self, ctx:miParserParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by miParserParser#moreExpressions.
    def enterMoreExpressions(self, ctx:miParserParser.MoreExpressionsContext):
        pass

    # Exit a parse tree produced by miParserParser#moreExpressions.
    def exitMoreExpressions(self, ctx:miParserParser.MoreExpressionsContext):
        pass


    # Enter a parse tree produced by miParserParser#primitiveExpression.
    def enterPrimitiveExpression(self, ctx:miParserParser.PrimitiveExpressionContext):
        pass

    # Exit a parse tree produced by miParserParser#primitiveExpression.
    def exitPrimitiveExpression(self, ctx:miParserParser.PrimitiveExpressionContext):
        pass


    # Enter a parse tree produced by miParserParser#listExpression.
    def enterListExpression(self, ctx:miParserParser.ListExpressionContext):
        pass

    # Exit a parse tree produced by miParserParser#listExpression.
    def exitListExpression(self, ctx:miParserParser.ListExpressionContext):
        pass



del miParserParser