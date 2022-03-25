# Generated from C:/Users/caohi/Desktop/2022/Compi/Proyectos/Proyecto/MiniPython\miParser.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3G")
        buf.write("\u00ec\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\7\2;\n\2\f")
        buf.write("\2\16\2>\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3")
        buf.write("I\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5")
        buf.write("V\n\5\3\6\3\6\7\6Z\n\6\f\6\16\6]\13\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\7\20\u0091\n\20")
        buf.write("\f\20\16\20\u0094\13\20\3\21\3\21\3\21\3\22\3\22\7\22")
        buf.write("\u009b\n\22\f\22\16\22\u009e\13\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\7\24\u00a5\n\24\f\24\16\24\u00a8\13\24\3\25\3\25")
        buf.write("\3\25\3\25\5\25\u00ae\n\25\3\26\3\26\7\26\u00b2\n\26\f")
        buf.write("\26\16\26\u00b5\13\26\3\27\3\27\3\27\3\30\3\30\3\30\3")
        buf.write("\30\7\30\u00be\n\30\f\30\16\30\u00c1\13\30\3\31\3\31\3")
        buf.write("\31\3\31\5\31\u00c7\n\31\3\32\3\32\7\32\u00cb\n\32\f\32")
        buf.write("\16\32\u00ce\13\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\5\33\u00da\n\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\5\33\u00e6\n\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\2\2\35\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\66\2\5\4\2\35\35+.\4\2!!$$\4")
        buf.write("\2&&((\2\u00eb\28\3\2\2\2\4H\3\2\2\2\6J\3\2\2\2\bU\3\2")
        buf.write("\2\2\n[\3\2\2\2\f^\3\2\2\2\16f\3\2\2\2\20k\3\2\2\2\22")
        buf.write("r\3\2\2\2\24v\3\2\2\2\26|\3\2\2\2\30\u0081\3\2\2\2\32")
        buf.write("\u0087\3\2\2\2\34\u008a\3\2\2\2\36\u008e\3\2\2\2 \u0095")
        buf.write("\3\2\2\2\"\u009c\3\2\2\2$\u009f\3\2\2\2&\u00a6\3\2\2\2")
        buf.write("(\u00ad\3\2\2\2*\u00b3\3\2\2\2,\u00b6\3\2\2\2.\u00bf\3")
        buf.write("\2\2\2\60\u00c6\3\2\2\2\62\u00cc\3\2\2\2\64\u00e5\3\2")
        buf.write("\2\2\66\u00e7\3\2\2\28<\5\4\3\29;\5\4\3\2:9\3\2\2\2;>")
        buf.write("\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\3\3\2\2\2><\3\2\2\2?I\5")
        buf.write("\6\4\2@I\5\f\7\2AI\5\22\n\2BI\5\24\13\2CI\5\16\b\2DI\5")
        buf.write("\20\t\2EI\5\26\f\2FI\5\30\r\2GI\5\32\16\2H?\3\2\2\2H@")
        buf.write("\3\2\2\2HA\3\2\2\2HB\3\2\2\2HC\3\2\2\2HD\3\2\2\2HE\3\2")
        buf.write("\2\2HF\3\2\2\2HG\3\2\2\2I\5\3\2\2\2JK\7\24\2\2KL\7<\2")
        buf.write("\2LM\7\66\2\2MN\5\b\5\2NO\7\67\2\2OP\7\33\2\2PQ\5\34\17")
        buf.write("\2Q\7\3\2\2\2RS\7<\2\2SV\5\n\6\2TV\3\2\2\2UR\3\2\2\2U")
        buf.write("T\3\2\2\2V\t\3\2\2\2WX\7\30\2\2XZ\7<\2\2YW\3\2\2\2Z]\3")
        buf.write("\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\\13\3\2\2\2][\3\2\2\2^_\7")
        buf.write("\3\2\2_`\5 \21\2`a\7\33\2\2ab\5\34\17\2bc\7\4\2\2cd\7")
        buf.write("\33\2\2de\5\34\17\2e\r\3\2\2\2fg\7\5\2\2gh\5 \21\2hi\7")
        buf.write("\33\2\2ij\5\34\17\2j\17\3\2\2\2kl\7\b\2\2lm\5 \21\2mn")
        buf.write("\7\t\2\2no\5\60\31\2op\7\33\2\2pq\5\34\17\2q\21\3\2\2")
        buf.write("\2rs\7\20\2\2st\5 \21\2tu\7E\2\2u\23\3\2\2\2vw\7\21\2")
        buf.write("\2wx\7\66\2\2xy\5 \21\2yz\7\67\2\2z{\7E\2\2{\25\3\2\2")
        buf.write("\2|}\7<\2\2}~\7\36\2\2~\177\5 \21\2\177\u0080\7E\2\2\u0080")
        buf.write("\27\3\2\2\2\u0081\u0082\5\64\33\2\u0082\u0083\7\66\2\2")
        buf.write("\u0083\u0084\5\60\31\2\u0084\u0085\7\67\2\2\u0085\u0086")
        buf.write("\7E\2\2\u0086\31\3\2\2\2\u0087\u0088\5\60\31\2\u0088\u0089")
        buf.write("\7E\2\2\u0089\33\3\2\2\2\u008a\u008b\7F\2\2\u008b\u008c")
        buf.write("\5\36\20\2\u008c\u008d\7G\2\2\u008d\35\3\2\2\2\u008e\u0092")
        buf.write("\5\4\3\2\u008f\u0091\5\4\3\2\u0090\u008f\3\2\2\2\u0091")
        buf.write("\u0094\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2\2")
        buf.write("\u0093\37\3\2\2\2\u0094\u0092\3\2\2\2\u0095\u0096\5$\23")
        buf.write("\2\u0096\u0097\5\"\22\2\u0097!\3\2\2\2\u0098\u0099\t\2")
        buf.write("\2\2\u0099\u009b\5$\23\2\u009a\u0098\3\2\2\2\u009b\u009e")
        buf.write("\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d")
        buf.write("#\3\2\2\2\u009e\u009c\3\2\2\2\u009f\u00a0\5(\25\2\u00a0")
        buf.write("\u00a1\5&\24\2\u00a1%\3\2\2\2\u00a2\u00a3\t\3\2\2\u00a3")
        buf.write("\u00a5\5(\25\2\u00a4\u00a2\3\2\2\2\u00a5\u00a8\3\2\2\2")
        buf.write("\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\'\3\2\2")
        buf.write("\2\u00a8\u00a6\3\2\2\2\u00a9\u00aa\5,\27\2\u00aa\u00ab")
        buf.write("\5*\26\2\u00ab\u00ae\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad")
        buf.write("\u00a9\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae)\3\2\2\2\u00af")
        buf.write("\u00b0\t\4\2\2\u00b0\u00b2\5,\27\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3")
        buf.write("\2\2\2\u00b4+\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7")
        buf.write("\5\64\33\2\u00b7\u00b8\5.\30\2\u00b8-\3\2\2\2\u00b9\u00ba")
        buf.write("\78\2\2\u00ba\u00bb\5 \21\2\u00bb\u00bc\79\2\2\u00bc\u00be")
        buf.write("\3\2\2\2\u00bd\u00b9\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf")
        buf.write("\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0/\3\2\2\2\u00c1")
        buf.write("\u00bf\3\2\2\2\u00c2\u00c3\5 \21\2\u00c3\u00c4\5\62\32")
        buf.write("\2\u00c4\u00c7\3\2\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00c2")
        buf.write("\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7\61\3\2\2\2\u00c8\u00c9")
        buf.write("\7\30\2\2\u00c9\u00cb\5 \21\2\u00ca\u00c8\3\2\2\2\u00cb")
        buf.write("\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2")
        buf.write("\u00cd\63\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00e6\7?\2")
        buf.write("\2\u00d0\u00e6\7A\2\2\u00d1\u00e6\7=\2\2\u00d2\u00e6\7")
        buf.write(">\2\2\u00d3\u00d9\7<\2\2\u00d4\u00d5\7\66\2\2\u00d5\u00d6")
        buf.write("\5\60\31\2\u00d6\u00d7\7\67\2\2\u00d7\u00da\3\2\2\2\u00d8")
        buf.write("\u00da\3\2\2\2\u00d9\u00d4\3\2\2\2\u00d9\u00d8\3\2\2\2")
        buf.write("\u00da\u00e6\3\2\2\2\u00db\u00dc\7\66\2\2\u00dc\u00dd")
        buf.write("\5 \21\2\u00dd\u00de\7\67\2\2\u00de\u00e6\3\2\2\2\u00df")
        buf.write("\u00e6\5\66\34\2\u00e0\u00e1\7\27\2\2\u00e1\u00e2\7\66")
        buf.write("\2\2\u00e2\u00e3\5 \21\2\u00e3\u00e4\7\67\2\2\u00e4\u00e6")
        buf.write("\3\2\2\2\u00e5\u00cf\3\2\2\2\u00e5\u00d0\3\2\2\2\u00e5")
        buf.write("\u00d1\3\2\2\2\u00e5\u00d2\3\2\2\2\u00e5\u00d3\3\2\2\2")
        buf.write("\u00e5\u00db\3\2\2\2\u00e5\u00df\3\2\2\2\u00e5\u00e0\3")
        buf.write("\2\2\2\u00e6\65\3\2\2\2\u00e7\u00e8\78\2\2\u00e8\u00e9")
        buf.write("\5\60\31\2\u00e9\u00ea\79\2\2\u00ea\67\3\2\2\2\20<HU[")
        buf.write("\u0092\u009c\u00a6\u00ad\u00b3\u00bf\u00c6\u00cc\u00d9")
        buf.write("\u00e5")
        return buf.getvalue()


class miParserParser ( Parser ):

    grammarFileName = "miParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'while'", "'do'", "'break'", 
                     "'for'", "'in'", "'begin'", "'end'", "'let'", "'const'", 
                     "'var'", "'continue'", "'return'", "'print'", "'package'", 
                     "'type'", "'def'", "'struct'", "'append'", "'len'", 
                     "','", "';'", "'.'", "':'", "':='", "'=='", "'='", 
                     "'++'", "'+='", "'+'", "'--'", "'-='", "'-'", "'/='", 
                     "'/'", "'*='", "'*'", "'!='", "'!'", "'>='", "'>'", 
                     "'<='", "'<'", "'%'", "'%='", "'&&'", "'&'", "'||'", 
                     "'|'", "'|='", "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "WHILE", "DO", "BREAK", 
                      "FOR", "IN", "BEGIN", "END", "LET", "CONST", "VAR", 
                      "CONTINUE", "RETURN", "PRINT", "PACKAGE", "TYPE", 
                      "DEF", "STRUCT", "APPEND", "LEN", "COMA", "PyCOMA", 
                      "PUNTO", "DOSPUNTOS", "DOSPUNTOSIGUAL", "EQUALS", 
                      "ASYGN", "SUM2", "SUMIGUAL", "SUM", "RES2", "RESIGUAL", 
                      "RES", "DIVIGUAL", "DIV", "MULIGUAL", "MUL", "DIF", 
                      "ADMIRACION", "MAYORIGUAL", "MAYOR", "MENORIGUAL", 
                      "MENOR", "PORCENTAJE", "PORCENTAJEIGUAL", "AND2", 
                      "AND", "OR2", "OR", "ORIGUAL", "PARENTESISIZQ", "PARENTESISDER", 
                      "BRACKETIZQ", "BRACKETDER", "LLAVEIZQ", "LLAVEDER", 
                      "ID", "CHAR_LITERAL", "RAWSTRINGLITERAL", "INTLITERAL", 
                      "DECIMAL_FLOAT_LIT", "FLOATLITERAL", "HEX_FLOAT_LIT", 
                      "COMMENT", "WS", "NEWLINE", "INDENT", "DEDENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_defStatement = 2
    RULE_argList = 3
    RULE_moreArgs = 4
    RULE_ifStatement = 5
    RULE_whileStatement = 6
    RULE_forStatement = 7
    RULE_returnStatement = 8
    RULE_printStatement = 9
    RULE_assignStatement = 10
    RULE_functionCallStatement = 11
    RULE_expressionStatement = 12
    RULE_sequence = 13
    RULE_moreStatements = 14
    RULE_expression = 15
    RULE_comparison = 16
    RULE_additionExpression = 17
    RULE_additionFactor = 18
    RULE_multiplicationExpression = 19
    RULE_multiplicationFactor = 20
    RULE_elementExpression = 21
    RULE_elementAccess = 22
    RULE_expressionList = 23
    RULE_moreExpressions = 24
    RULE_primitiveExpression = 25
    RULE_listExpression = 26

    ruleNames =  [ "program", "statement", "defStatement", "argList", "moreArgs", 
                   "ifStatement", "whileStatement", "forStatement", "returnStatement", 
                   "printStatement", "assignStatement", "functionCallStatement", 
                   "expressionStatement", "sequence", "moreStatements", 
                   "expression", "comparison", "additionExpression", "additionFactor", 
                   "multiplicationExpression", "multiplicationFactor", "elementExpression", 
                   "elementAccess", "expressionList", "moreExpressions", 
                   "primitiveExpression", "listExpression" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    WHILE=3
    DO=4
    BREAK=5
    FOR=6
    IN=7
    BEGIN=8
    END=9
    LET=10
    CONST=11
    VAR=12
    CONTINUE=13
    RETURN=14
    PRINT=15
    PACKAGE=16
    TYPE=17
    DEF=18
    STRUCT=19
    APPEND=20
    LEN=21
    COMA=22
    PyCOMA=23
    PUNTO=24
    DOSPUNTOS=25
    DOSPUNTOSIGUAL=26
    EQUALS=27
    ASYGN=28
    SUM2=29
    SUMIGUAL=30
    SUM=31
    RES2=32
    RESIGUAL=33
    RES=34
    DIVIGUAL=35
    DIV=36
    MULIGUAL=37
    MUL=38
    DIF=39
    ADMIRACION=40
    MAYORIGUAL=41
    MAYOR=42
    MENORIGUAL=43
    MENOR=44
    PORCENTAJE=45
    PORCENTAJEIGUAL=46
    AND2=47
    AND=48
    OR2=49
    OR=50
    ORIGUAL=51
    PARENTESISIZQ=52
    PARENTESISDER=53
    BRACKETIZQ=54
    BRACKETDER=55
    LLAVEIZQ=56
    LLAVEDER=57
    ID=58
    CHAR_LITERAL=59
    RAWSTRINGLITERAL=60
    INTLITERAL=61
    DECIMAL_FLOAT_LIT=62
    FLOATLITERAL=63
    HEX_FLOAT_LIT=64
    COMMENT=65
    WS=66
    NEWLINE=67
    INDENT=68
    DEDENT=69

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(miParserParser.StatementContext,i)


        def getRuleIndex(self):
            return miParserParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = miParserParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.statement()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.IF) | (1 << miParserParser.WHILE) | (1 << miParserParser.FOR) | (1 << miParserParser.RETURN) | (1 << miParserParser.PRINT) | (1 << miParserParser.DEF) | (1 << miParserParser.LEN) | (1 << miParserParser.COMA) | (1 << miParserParser.EQUALS) | (1 << miParserParser.SUM) | (1 << miParserParser.RES) | (1 << miParserParser.MAYORIGUAL) | (1 << miParserParser.MAYOR) | (1 << miParserParser.MENORIGUAL) | (1 << miParserParser.MENOR) | (1 << miParserParser.PARENTESISIZQ) | (1 << miParserParser.BRACKETIZQ) | (1 << miParserParser.ID) | (1 << miParserParser.CHAR_LITERAL) | (1 << miParserParser.RAWSTRINGLITERAL) | (1 << miParserParser.INTLITERAL) | (1 << miParserParser.FLOATLITERAL))) != 0) or _la==miParserParser.NEWLINE:
                self.state = 55
                self.statement()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def defStatement(self):
            return self.getTypedRuleContext(miParserParser.DefStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(miParserParser.IfStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(miParserParser.ReturnStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(miParserParser.PrintStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(miParserParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(miParserParser.ForStatementContext,0)


        def assignStatement(self):
            return self.getTypedRuleContext(miParserParser.AssignStatementContext,0)


        def functionCallStatement(self):
            return self.getTypedRuleContext(miParserParser.FunctionCallStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(miParserParser.ExpressionStatementContext,0)


        def getRuleIndex(self):
            return miParserParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = miParserParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.defStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.ifStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.returnStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 64
                self.printStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 65
                self.whileStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 66
                self.forStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 67
                self.assignStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 68
                self.functionCallStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 69
                self.expressionStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(miParserParser.DEF, 0)

        def ID(self):
            return self.getToken(miParserParser.ID, 0)

        def PARENTESISIZQ(self):
            return self.getToken(miParserParser.PARENTESISIZQ, 0)

        def argList(self):
            return self.getTypedRuleContext(miParserParser.ArgListContext,0)


        def PARENTESISDER(self):
            return self.getToken(miParserParser.PARENTESISDER, 0)

        def DOSPUNTOS(self):
            return self.getToken(miParserParser.DOSPUNTOS, 0)

        def sequence(self):
            return self.getTypedRuleContext(miParserParser.SequenceContext,0)


        def getRuleIndex(self):
            return miParserParser.RULE_defStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefStatement" ):
                listener.enterDefStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefStatement" ):
                listener.exitDefStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefStatement" ):
                return visitor.visitDefStatement(self)
            else:
                return visitor.visitChildren(self)




    def defStatement(self):

        localctx = miParserParser.DefStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_defStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(miParserParser.DEF)
            self.state = 73
            self.match(miParserParser.ID)
            self.state = 74
            self.match(miParserParser.PARENTESISIZQ)
            self.state = 75
            self.argList()
            self.state = 76
            self.match(miParserParser.PARENTESISDER)
            self.state = 77
            self.match(miParserParser.DOSPUNTOS)
            self.state = 78
            self.sequence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(miParserParser.ID, 0)

        def moreArgs(self):
            return self.getTypedRuleContext(miParserParser.MoreArgsContext,0)


        def getRuleIndex(self):
            return miParserParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = miParserParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_argList)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [miParserParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(miParserParser.ID)
                self.state = 81
                self.moreArgs()
                pass
            elif token in [miParserParser.PARENTESISDER]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoreArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.COMA)
            else:
                return self.getToken(miParserParser.COMA, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.ID)
            else:
                return self.getToken(miParserParser.ID, i)

        def getRuleIndex(self):
            return miParserParser.RULE_moreArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoreArgs" ):
                listener.enterMoreArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoreArgs" ):
                listener.exitMoreArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoreArgs" ):
                return visitor.visitMoreArgs(self)
            else:
                return visitor.visitChildren(self)




    def moreArgs(self):

        localctx = miParserParser.MoreArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_moreArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.COMA:
                self.state = 85
                self.match(miParserParser.COMA)
                self.state = 86
                self.match(miParserParser.ID)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(miParserParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)


        def DOSPUNTOS(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.DOSPUNTOS)
            else:
                return self.getToken(miParserParser.DOSPUNTOS, i)

        def sequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.SequenceContext)
            else:
                return self.getTypedRuleContext(miParserParser.SequenceContext,i)


        def ELSE(self):
            return self.getToken(miParserParser.ELSE, 0)

        def getRuleIndex(self):
            return miParserParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = miParserParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(miParserParser.IF)
            self.state = 93
            self.expression()
            self.state = 94
            self.match(miParserParser.DOSPUNTOS)
            self.state = 95
            self.sequence()
            self.state = 96
            self.match(miParserParser.ELSE)
            self.state = 97
            self.match(miParserParser.DOSPUNTOS)
            self.state = 98
            self.sequence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(miParserParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)


        def DOSPUNTOS(self):
            return self.getToken(miParserParser.DOSPUNTOS, 0)

        def sequence(self):
            return self.getTypedRuleContext(miParserParser.SequenceContext,0)


        def getRuleIndex(self):
            return miParserParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = miParserParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(miParserParser.WHILE)
            self.state = 101
            self.expression()
            self.state = 102
            self.match(miParserParser.DOSPUNTOS)
            self.state = 103
            self.sequence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(miParserParser.FOR, 0)

        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)


        def IN(self):
            return self.getToken(miParserParser.IN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)


        def DOSPUNTOS(self):
            return self.getToken(miParserParser.DOSPUNTOS, 0)

        def sequence(self):
            return self.getTypedRuleContext(miParserParser.SequenceContext,0)


        def getRuleIndex(self):
            return miParserParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = miParserParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(miParserParser.FOR)
            self.state = 106
            self.expression()
            self.state = 107
            self.match(miParserParser.IN)
            self.state = 108
            self.expressionList()
            self.state = 109
            self.match(miParserParser.DOSPUNTOS)
            self.state = 110
            self.sequence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(miParserParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(miParserParser.NEWLINE, 0)

        def getRuleIndex(self):
            return miParserParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = miParserParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(miParserParser.RETURN)
            self.state = 113
            self.expression()
            self.state = 114
            self.match(miParserParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(miParserParser.PRINT, 0)

        def PARENTESISIZQ(self):
            return self.getToken(miParserParser.PARENTESISIZQ, 0)

        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)


        def PARENTESISDER(self):
            return self.getToken(miParserParser.PARENTESISDER, 0)

        def NEWLINE(self):
            return self.getToken(miParserParser.NEWLINE, 0)

        def getRuleIndex(self):
            return miParserParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = miParserParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(miParserParser.PRINT)
            self.state = 117
            self.match(miParserParser.PARENTESISIZQ)
            self.state = 118
            self.expression()
            self.state = 119
            self.match(miParserParser.PARENTESISDER)
            self.state = 120
            self.match(miParserParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(miParserParser.ID, 0)

        def ASYGN(self):
            return self.getToken(miParserParser.ASYGN, 0)

        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(miParserParser.NEWLINE, 0)

        def getRuleIndex(self):
            return miParserParser.RULE_assignStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStatement" ):
                listener.enterAssignStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStatement" ):
                listener.exitAssignStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignStatement(self):

        localctx = miParserParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(miParserParser.ID)
            self.state = 123
            self.match(miParserParser.ASYGN)
            self.state = 124
            self.expression()
            self.state = 125
            self.match(miParserParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveExpression(self):
            return self.getTypedRuleContext(miParserParser.PrimitiveExpressionContext,0)


        def PARENTESISIZQ(self):
            return self.getToken(miParserParser.PARENTESISIZQ, 0)

        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)


        def PARENTESISDER(self):
            return self.getToken(miParserParser.PARENTESISDER, 0)

        def NEWLINE(self):
            return self.getToken(miParserParser.NEWLINE, 0)

        def getRuleIndex(self):
            return miParserParser.RULE_functionCallStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallStatement" ):
                listener.enterFunctionCallStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallStatement" ):
                listener.exitFunctionCallStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallStatement" ):
                return visitor.visitFunctionCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def functionCallStatement(self):

        localctx = miParserParser.FunctionCallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_functionCallStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.primitiveExpression()
            self.state = 128
            self.match(miParserParser.PARENTESISIZQ)
            self.state = 129
            self.expressionList()
            self.state = 130
            self.match(miParserParser.PARENTESISDER)
            self.state = 131
            self.match(miParserParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)


        def NEWLINE(self):
            return self.getToken(miParserParser.NEWLINE, 0)

        def getRuleIndex(self):
            return miParserParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = miParserParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.expressionList()
            self.state = 134
            self.match(miParserParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(miParserParser.INDENT, 0)

        def moreStatements(self):
            return self.getTypedRuleContext(miParserParser.MoreStatementsContext,0)


        def DEDENT(self):
            return self.getToken(miParserParser.DEDENT, 0)

        def getRuleIndex(self):
            return miParserParser.RULE_sequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequence" ):
                listener.enterSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequence" ):
                listener.exitSequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequence" ):
                return visitor.visitSequence(self)
            else:
                return visitor.visitChildren(self)




    def sequence(self):

        localctx = miParserParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_sequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(miParserParser.INDENT)
            self.state = 137
            self.moreStatements()
            self.state = 138
            self.match(miParserParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoreStatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(miParserParser.StatementContext,i)


        def getRuleIndex(self):
            return miParserParser.RULE_moreStatements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoreStatements" ):
                listener.enterMoreStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoreStatements" ):
                listener.exitMoreStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoreStatements" ):
                return visitor.visitMoreStatements(self)
            else:
                return visitor.visitChildren(self)




    def moreStatements(self):

        localctx = miParserParser.MoreStatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_moreStatements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.statement()
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.IF) | (1 << miParserParser.WHILE) | (1 << miParserParser.FOR) | (1 << miParserParser.RETURN) | (1 << miParserParser.PRINT) | (1 << miParserParser.DEF) | (1 << miParserParser.LEN) | (1 << miParserParser.COMA) | (1 << miParserParser.EQUALS) | (1 << miParserParser.SUM) | (1 << miParserParser.RES) | (1 << miParserParser.MAYORIGUAL) | (1 << miParserParser.MAYOR) | (1 << miParserParser.MENORIGUAL) | (1 << miParserParser.MENOR) | (1 << miParserParser.PARENTESISIZQ) | (1 << miParserParser.BRACKETIZQ) | (1 << miParserParser.ID) | (1 << miParserParser.CHAR_LITERAL) | (1 << miParserParser.RAWSTRINGLITERAL) | (1 << miParserParser.INTLITERAL) | (1 << miParserParser.FLOATLITERAL))) != 0) or _la==miParserParser.NEWLINE:
                self.state = 141
                self.statement()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additionExpression(self):
            return self.getTypedRuleContext(miParserParser.AdditionExpressionContext,0)


        def comparison(self):
            return self.getTypedRuleContext(miParserParser.ComparisonContext,0)


        def getRuleIndex(self):
            return miParserParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = miParserParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.additionExpression()
            self.state = 148
            self.comparison()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additionExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.AdditionExpressionContext)
            else:
                return self.getTypedRuleContext(miParserParser.AdditionExpressionContext,i)


        def MENOR(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.MENOR)
            else:
                return self.getToken(miParserParser.MENOR, i)

        def MAYOR(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.MAYOR)
            else:
                return self.getToken(miParserParser.MAYOR, i)

        def MENORIGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.MENORIGUAL)
            else:
                return self.getToken(miParserParser.MENORIGUAL, i)

        def MAYORIGUAL(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.MAYORIGUAL)
            else:
                return self.getToken(miParserParser.MAYORIGUAL, i)

        def EQUALS(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.EQUALS)
            else:
                return self.getToken(miParserParser.EQUALS, i)

        def getRuleIndex(self):
            return miParserParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = miParserParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.EQUALS) | (1 << miParserParser.MAYORIGUAL) | (1 << miParserParser.MAYOR) | (1 << miParserParser.MENORIGUAL) | (1 << miParserParser.MENOR))) != 0):
                self.state = 150
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.EQUALS) | (1 << miParserParser.MAYORIGUAL) | (1 << miParserParser.MAYOR) | (1 << miParserParser.MENORIGUAL) | (1 << miParserParser.MENOR))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 151
                self.additionExpression()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditionExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicationExpression(self):
            return self.getTypedRuleContext(miParserParser.MultiplicationExpressionContext,0)


        def additionFactor(self):
            return self.getTypedRuleContext(miParserParser.AdditionFactorContext,0)


        def getRuleIndex(self):
            return miParserParser.RULE_additionExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditionExpression" ):
                listener.enterAdditionExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditionExpression" ):
                listener.exitAdditionExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditionExpression" ):
                return visitor.visitAdditionExpression(self)
            else:
                return visitor.visitChildren(self)




    def additionExpression(self):

        localctx = miParserParser.AdditionExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_additionExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.multiplicationExpression()
            self.state = 158
            self.additionFactor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditionFactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicationExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.MultiplicationExpressionContext)
            else:
                return self.getTypedRuleContext(miParserParser.MultiplicationExpressionContext,i)


        def SUM(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.SUM)
            else:
                return self.getToken(miParserParser.SUM, i)

        def RES(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.RES)
            else:
                return self.getToken(miParserParser.RES, i)

        def getRuleIndex(self):
            return miParserParser.RULE_additionFactor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditionFactor" ):
                listener.enterAdditionFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditionFactor" ):
                listener.exitAdditionFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditionFactor" ):
                return visitor.visitAdditionFactor(self)
            else:
                return visitor.visitChildren(self)




    def additionFactor(self):

        localctx = miParserParser.AdditionFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_additionFactor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.SUM or _la==miParserParser.RES:
                self.state = 160
                _la = self._input.LA(1)
                if not(_la==miParserParser.SUM or _la==miParserParser.RES):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 161
                self.multiplicationExpression()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicationExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementExpression(self):
            return self.getTypedRuleContext(miParserParser.ElementExpressionContext,0)


        def multiplicationFactor(self):
            return self.getTypedRuleContext(miParserParser.MultiplicationFactorContext,0)


        def getRuleIndex(self):
            return miParserParser.RULE_multiplicationExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicationExpression" ):
                listener.enterMultiplicationExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicationExpression" ):
                listener.exitMultiplicationExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicationExpression" ):
                return visitor.visitMultiplicationExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicationExpression(self):

        localctx = miParserParser.MultiplicationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_multiplicationExpression)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [miParserParser.LEN, miParserParser.PARENTESISIZQ, miParserParser.BRACKETIZQ, miParserParser.ID, miParserParser.CHAR_LITERAL, miParserParser.RAWSTRINGLITERAL, miParserParser.INTLITERAL, miParserParser.FLOATLITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.elementExpression()
                self.state = 168
                self.multiplicationFactor()
                pass
            elif token in [miParserParser.IN, miParserParser.COMA, miParserParser.DOSPUNTOS, miParserParser.EQUALS, miParserParser.SUM, miParserParser.RES, miParserParser.MAYORIGUAL, miParserParser.MAYOR, miParserParser.MENORIGUAL, miParserParser.MENOR, miParserParser.PARENTESISDER, miParserParser.BRACKETDER, miParserParser.NEWLINE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicationFactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.ElementExpressionContext)
            else:
                return self.getTypedRuleContext(miParserParser.ElementExpressionContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.MUL)
            else:
                return self.getToken(miParserParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.DIV)
            else:
                return self.getToken(miParserParser.DIV, i)

        def getRuleIndex(self):
            return miParserParser.RULE_multiplicationFactor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicationFactor" ):
                listener.enterMultiplicationFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicationFactor" ):
                listener.exitMultiplicationFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicationFactor" ):
                return visitor.visitMultiplicationFactor(self)
            else:
                return visitor.visitChildren(self)




    def multiplicationFactor(self):

        localctx = miParserParser.MultiplicationFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_multiplicationFactor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.DIV or _la==miParserParser.MUL:
                self.state = 173
                _la = self._input.LA(1)
                if not(_la==miParserParser.DIV or _la==miParserParser.MUL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 174
                self.elementExpression()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveExpression(self):
            return self.getTypedRuleContext(miParserParser.PrimitiveExpressionContext,0)


        def elementAccess(self):
            return self.getTypedRuleContext(miParserParser.ElementAccessContext,0)


        def getRuleIndex(self):
            return miParserParser.RULE_elementExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementExpression" ):
                listener.enterElementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementExpression" ):
                listener.exitElementExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementExpression" ):
                return visitor.visitElementExpression(self)
            else:
                return visitor.visitChildren(self)




    def elementExpression(self):

        localctx = miParserParser.ElementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_elementExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.primitiveExpression()
            self.state = 181
            self.elementAccess()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACKETIZQ(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.BRACKETIZQ)
            else:
                return self.getToken(miParserParser.BRACKETIZQ, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(miParserParser.ExpressionContext,i)


        def BRACKETDER(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.BRACKETDER)
            else:
                return self.getToken(miParserParser.BRACKETDER, i)

        def getRuleIndex(self):
            return miParserParser.RULE_elementAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementAccess" ):
                listener.enterElementAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementAccess" ):
                listener.exitElementAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementAccess" ):
                return visitor.visitElementAccess(self)
            else:
                return visitor.visitChildren(self)




    def elementAccess(self):

        localctx = miParserParser.ElementAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_elementAccess)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.BRACKETIZQ:
                self.state = 183
                self.match(miParserParser.BRACKETIZQ)
                self.state = 184
                self.expression()
                self.state = 185
                self.match(miParserParser.BRACKETDER)
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)


        def moreExpressions(self):
            return self.getTypedRuleContext(miParserParser.MoreExpressionsContext,0)


        def getRuleIndex(self):
            return miParserParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = miParserParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expressionList)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.expression()
                self.state = 193
                self.moreExpressions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoreExpressionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(miParserParser.COMA)
            else:
                return self.getToken(miParserParser.COMA, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(miParserParser.ExpressionContext,i)


        def getRuleIndex(self):
            return miParserParser.RULE_moreExpressions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoreExpressions" ):
                listener.enterMoreExpressions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoreExpressions" ):
                listener.exitMoreExpressions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoreExpressions" ):
                return visitor.visitMoreExpressions(self)
            else:
                return visitor.visitChildren(self)




    def moreExpressions(self):

        localctx = miParserParser.MoreExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_moreExpressions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.COMA:
                self.state = 198
                self.match(miParserParser.COMA)
                self.state = 199
                self.expression()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLITERAL(self):
            return self.getToken(miParserParser.INTLITERAL, 0)

        def FLOATLITERAL(self):
            return self.getToken(miParserParser.FLOATLITERAL, 0)

        def CHAR_LITERAL(self):
            return self.getToken(miParserParser.CHAR_LITERAL, 0)

        def RAWSTRINGLITERAL(self):
            return self.getToken(miParserParser.RAWSTRINGLITERAL, 0)

        def ID(self):
            return self.getToken(miParserParser.ID, 0)

        def PARENTESISIZQ(self):
            return self.getToken(miParserParser.PARENTESISIZQ, 0)

        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)


        def PARENTESISDER(self):
            return self.getToken(miParserParser.PARENTESISDER, 0)

        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)


        def listExpression(self):
            return self.getTypedRuleContext(miParserParser.ListExpressionContext,0)


        def LEN(self):
            return self.getToken(miParserParser.LEN, 0)

        def getRuleIndex(self):
            return miParserParser.RULE_primitiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExpression" ):
                listener.enterPrimitiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExpression" ):
                listener.exitPrimitiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExpression" ):
                return visitor.visitPrimitiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def primitiveExpression(self):

        localctx = miParserParser.PrimitiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_primitiveExpression)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [miParserParser.INTLITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(miParserParser.INTLITERAL)
                pass
            elif token in [miParserParser.FLOATLITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.match(miParserParser.FLOATLITERAL)
                pass
            elif token in [miParserParser.CHAR_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.match(miParserParser.CHAR_LITERAL)
                pass
            elif token in [miParserParser.RAWSTRINGLITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 208
                self.match(miParserParser.RAWSTRINGLITERAL)
                pass
            elif token in [miParserParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 209
                self.match(miParserParser.ID)
                self.state = 215
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 210
                    self.match(miParserParser.PARENTESISIZQ)
                    self.state = 211
                    self.expressionList()
                    self.state = 212
                    self.match(miParserParser.PARENTESISDER)
                    pass

                elif la_ == 2:
                    pass


                pass
            elif token in [miParserParser.PARENTESISIZQ]:
                self.enterOuterAlt(localctx, 6)
                self.state = 217
                self.match(miParserParser.PARENTESISIZQ)
                self.state = 218
                self.expression()
                self.state = 219
                self.match(miParserParser.PARENTESISDER)
                pass
            elif token in [miParserParser.BRACKETIZQ]:
                self.enterOuterAlt(localctx, 7)
                self.state = 221
                self.listExpression()
                pass
            elif token in [miParserParser.LEN]:
                self.enterOuterAlt(localctx, 8)
                self.state = 222
                self.match(miParserParser.LEN)
                self.state = 223
                self.match(miParserParser.PARENTESISIZQ)
                self.state = 224
                self.expression()
                self.state = 225
                self.match(miParserParser.PARENTESISDER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACKETIZQ(self):
            return self.getToken(miParserParser.BRACKETIZQ, 0)

        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)


        def BRACKETDER(self):
            return self.getToken(miParserParser.BRACKETDER, 0)

        def getRuleIndex(self):
            return miParserParser.RULE_listExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListExpression" ):
                listener.enterListExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListExpression" ):
                listener.exitListExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExpression" ):
                return visitor.visitListExpression(self)
            else:
                return visitor.visitChildren(self)




    def listExpression(self):

        localctx = miParserParser.ListExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_listExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(miParserParser.BRACKETIZQ)
            self.state = 230
            self.expressionList()
            self.state = 231
            self.match(miParserParser.BRACKETDER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





