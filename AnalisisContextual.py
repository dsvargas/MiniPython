import token
from miParserVisitor import *
from TablaSimbolos import *

from antlr4 import *

class AContextual(miParserVisitor):
    tablaSimb = TablaSimbolos()
    errorMsgs = []
    nivelActual = 1

    def openScope(self):
        self.nivelActual+=1;

    def closeScope(self):
        self.nivelActual -=1;

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
        self.visitIfStatement(ctx.ifStatement())
        return None

    def visitStatementReturnStatementAST(self, ctx: miParserParser.StatementReturnStatementASTContext):
        self.visitReturnStatementAST(ctx.returnStatement())
        return None

    def visitStatementPrintStatementAST(self, ctx: miParserParser.StatementPrintStatementASTContext):
        self.visitPrintStatementAST(ctx.printStatement())
        return None

    def visitStatementWhileStatementAST(self, ctx: miParserParser.StatementWhileStatementASTContext):
        self.visitWhileStatementAST(ctx.whileStatement())
        return None

    def visitStatementForStatementAST(self, ctx: miParserParser.StatementForStatementASTContext):
        self.visitForStatementAST(ctx.forStatement())
        return None

    def visitStatementAssignStatementAST(self, ctx: miParserParser.StatementAssignStatementASTContext):
        self.visitAssignStatementAST(ctx.assignStatement())
        return None

    def visitStatementFunctionCallStatementAST(self, ctx: miParserParser.StatementFunctionCallStatementASTContext):
        self.visitFunctionCallStatementAST(ctx.functionCallStatement())
        return None

    def visitStatementExpressionStatementAST(self, ctx: miParserParser.StatementExpressionStatementASTContext):
        self.visitExpressionAST(ctx.expressionStatement())
        return None
##################################################################################################################
    def visitDefStatementAST(self, ctx: miParserParser.DefStatementASTContext):
        #DEF ID PARENTESISIZQ argList PARENTESISDER DOSPUNTOS sequence

        self.visit(ctx.argList())
        self.visit(ctx.sequence())
        #openScope
        self.openScope()
        self.tablaSimb.InsertarFuncIdent(token, ctx, self.nivelActual)
        #closeScope
        self.closeScope()
        return None

    def visitMoreArgListAST(self, ctx: miParserParser.MoreArgListASTContext):
        self.visitMoreArgsAST(ctx)
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
        self.visit(ctx.sequence())
        # else visitar sequence
        return None

    def visitWhileStatementAST(self, ctx: miParserParser.WhileStatementASTContext):
        #while Expression : Sequence
        self.visit(ctx.expression())
        self.visit(ctx.sequence())
        return None

    def visitForStatementAST(self, ctx: miParserParser.ForStatementASTContext):
        #for i in list

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
        self.tablaSimb.InsertarVarIdent(ctx.ID(), ctx, self.nivelActual)
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
        if (ctx.additionExpression()):
            self.visit(ctx.additionExpression())
        else:
            self.visit(ctx.comparison())
        return None

    def visitComparisonAST(self, ctx: miParserParser.ComparisonASTContext):
        #( (MENOR|MAYOR|MENORIGUAL|MAYORIGUAL|EQUALS) additionExpression )*

        return self.visitChildren(ctx)

    def visitAdditionExpressionAST(self, ctx: miParserParser.AdditionExpressionASTContext):
        #multiplicationExpression additionFactor
        if(ctx.multiplicationExpression()):
            self.visit(ctx.multiplicationExpression())
        else:
            self.visit(ctx.additionFactor())
        return None

    def visitAdditionFactorAST(self, ctx: miParserParser.AdditionFactorASTContext):
        #( (SUM|RES) multiplicationExpression )*
        return self.visitChildren(ctx)

    def visitMultiplicationExpressionAST(self, ctx: miParserParser.MultiplicationExpressionASTContext):
        #elementExpression multiplicationFactor
        if(ctx.elementExpression()):
            self.visit(ctx.elementExpression())
        else:
            self.visit(ctx.multiplicationFactor())
        return None

    def visitEpsilonMultiplicationExpression(self, ctx: miParserParser.EpsilonMultiplicationExpressionContext):
        return None

    def visitMultiplicationFactorAST(self, ctx: miParserParser.MultiplicationFactorASTContext):
        # ( (MUL|DIV) elementExpression )*
        return self.visitChildren(ctx)

    def visitElementExpressionAST(self, ctx: miParserParser.ElementExpressionASTContext):
        #primitiveExpression elementAccess
        if(ctx.primitiveExpression()):
            self.visit(ctx.primitiveExpression())
        else:
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
        if ctx.expression():
            listaExp = ctx.moreExpressions()
            self.tablaSimb.InsertarArrayIdent(listaExp,ctx,self.nivelActual)
            self.visit(ctx.expression())
        else:
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
        return self.visitChildren(ctx)

    def visitPrimitiveExpressionFLOATLITERAL(self, ctx: miParserParser.PrimitiveExpressionFLOATLITERALContext):
        #FLOATLITERAL
        return self.visitChildren(ctx)

    def visitPrimitiveExpressionCHAR_LITERAL(self, ctx: miParserParser.PrimitiveExpressionCHAR_LITERALContext):
        #CHAR_LITERAL
        return self.visitChildren(ctx)

    def visitPrimitiveExpressionRAWSTRINGLITERAL(self, ctx: miParserParser.PrimitiveExpressionRAWSTRINGLITERALContext):
        #RAWSTRINGLITERAL
        return self.visitChildren(ctx)

    def visitPrimitiveExpressionID(self, ctx: miParserParser.PrimitiveExpressionIDContext):
        #ID (PARENTESISIZQ expressionList PARENTESISDER |   )
        var = self.tablaSimb.buscar(ctx.ID())
        return None

    def visitPrimitiveExpressionExpression(self, ctx: miParserParser.PrimitiveExpressionExpressionContext):
        #PARENTESISIZQ expression PARENTESISDER
        #self.visit(ctx.expression())
        return None

    def visitPrimitiveExpressionListExpression(self, ctx: miParserParser.PrimitiveExpressionListExpressionContext):
        #listExpression
        self.visit(ctx.listExpression())
        return None

    def visitPrimitiveExpressionLEN(self, ctx: miParserParser.PrimitiveExpressionLENContext):
        #LEN PARENTESISIZQ expression PARENTESISDER
        #self.tablaSimb.buscar(ctx.expression())
        self.visit(ctx.expression())
        return None

    def visitListExpressionAST(self, ctx: miParserParser.ListExpressionASTContext):
        #BRACKETIZQ expressionList BRACKETDER
        #self.visit(ctx.expressionList())
        return None

