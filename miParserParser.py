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
        buf.write("\u00f4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\3\2")
        buf.write("\7\2=\n\2\f\2\16\2@\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3K\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\5\5X\n\5\3\6\3\6\7\6\\\n\6\f\6\16\6_\13\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\7\20")
        buf.write("\u0093\n\20\f\20\16\20\u0096\13\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\7\22\u009d\n\22\f\22\16\22\u00a0\13\22\3\23\3\23")
        buf.write("\3\23\3\24\3\24\7\24\u00a7\n\24\f\24\16\24\u00aa\13\24")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u00b0\n\25\3\26\3\26\7\26\u00b4")
        buf.write("\n\26\f\26\16\26\u00b7\13\26\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\7\30\u00c0\n\30\f\30\16\30\u00c3\13\30\3\31")
        buf.write("\3\31\3\31\3\31\5\31\u00c9\n\31\3\32\3\32\7\32\u00cd\n")
        buf.write("\32\f\32\16\32\u00d0\13\32\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\5\33\u00dc\n\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u00e8\n\33\3")
        buf.write("\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\5\35\u00f2\n\35")
        buf.write("\3\35\2\2\36\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668\2\5\4\2\35\35+.\4\2!!$$\4\2&&((\2")
        buf.write("\u00f5\2:\3\2\2\2\4J\3\2\2\2\6L\3\2\2\2\bW\3\2\2\2\n]")
        buf.write("\3\2\2\2\f`\3\2\2\2\16h\3\2\2\2\20m\3\2\2\2\22t\3\2\2")
        buf.write("\2\24x\3\2\2\2\26~\3\2\2\2\30\u0083\3\2\2\2\32\u0089\3")
        buf.write("\2\2\2\34\u008c\3\2\2\2\36\u0090\3\2\2\2 \u0097\3\2\2")
        buf.write("\2\"\u009e\3\2\2\2$\u00a1\3\2\2\2&\u00a8\3\2\2\2(\u00af")
        buf.write("\3\2\2\2*\u00b5\3\2\2\2,\u00b8\3\2\2\2.\u00c1\3\2\2\2")
        buf.write("\60\u00c8\3\2\2\2\62\u00ce\3\2\2\2\64\u00e7\3\2\2\2\66")
        buf.write("\u00e9\3\2\2\28\u00f1\3\2\2\2:>\5\4\3\2;=\5\4\3\2<;\3")
        buf.write("\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?\3\3\2\2\2@>\3\2")
        buf.write("\2\2AK\5\6\4\2BK\5\f\7\2CK\5\22\n\2DK\5\24\13\2EK\5\16")
        buf.write("\b\2FK\5\20\t\2GK\5\26\f\2HK\5\30\r\2IK\5\32\16\2JA\3")
        buf.write("\2\2\2JB\3\2\2\2JC\3\2\2\2JD\3\2\2\2JE\3\2\2\2JF\3\2\2")
        buf.write("\2JG\3\2\2\2JH\3\2\2\2JI\3\2\2\2K\5\3\2\2\2LM\7\24\2\2")
        buf.write("MN\7<\2\2NO\7\66\2\2OP\5\b\5\2PQ\7\67\2\2QR\7\33\2\2R")
        buf.write("S\5\34\17\2S\7\3\2\2\2TU\7<\2\2UX\5\n\6\2VX\3\2\2\2WT")
        buf.write("\3\2\2\2WV\3\2\2\2X\t\3\2\2\2YZ\7\30\2\2Z\\\7<\2\2[Y\3")
        buf.write("\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^\13\3\2\2\2_]\3")
        buf.write("\2\2\2`a\7\3\2\2ab\5 \21\2bc\7\33\2\2cd\5\34\17\2de\7")
        buf.write("\4\2\2ef\7\33\2\2fg\5\34\17\2g\r\3\2\2\2hi\7\5\2\2ij\5")
        buf.write(" \21\2jk\7\33\2\2kl\5\34\17\2l\17\3\2\2\2mn\7\b\2\2no")
        buf.write("\5 \21\2op\7\t\2\2pq\5\60\31\2qr\7\33\2\2rs\5\34\17\2")
        buf.write("s\21\3\2\2\2tu\7\20\2\2uv\5 \21\2vw\7E\2\2w\23\3\2\2\2")
        buf.write("xy\7\21\2\2yz\7\66\2\2z{\5 \21\2{|\7\67\2\2|}\7E\2\2}")
        buf.write("\25\3\2\2\2~\177\7<\2\2\177\u0080\7\36\2\2\u0080\u0081")
        buf.write("\5 \21\2\u0081\u0082\7E\2\2\u0082\27\3\2\2\2\u0083\u0084")
        buf.write("\5\64\33\2\u0084\u0085\7\66\2\2\u0085\u0086\5\60\31\2")
        buf.write("\u0086\u0087\7\67\2\2\u0087\u0088\7E\2\2\u0088\31\3\2")
        buf.write("\2\2\u0089\u008a\5\60\31\2\u008a\u008b\7E\2\2\u008b\33")
        buf.write("\3\2\2\2\u008c\u008d\7F\2\2\u008d\u008e\5\36\20\2\u008e")
        buf.write("\u008f\7G\2\2\u008f\35\3\2\2\2\u0090\u0094\5\4\3\2\u0091")
        buf.write("\u0093\5\4\3\2\u0092\u0091\3\2\2\2\u0093\u0096\3\2\2\2")
        buf.write("\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\37\3\2")
        buf.write("\2\2\u0096\u0094\3\2\2\2\u0097\u0098\5$\23\2\u0098\u0099")
        buf.write("\5\"\22\2\u0099!\3\2\2\2\u009a\u009b\t\2\2\2\u009b\u009d")
        buf.write("\5$\23\2\u009c\u009a\3\2\2\2\u009d\u00a0\3\2\2\2\u009e")
        buf.write("\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f#\3\2\2\2\u00a0")
        buf.write("\u009e\3\2\2\2\u00a1\u00a2\5(\25\2\u00a2\u00a3\5&\24\2")
        buf.write("\u00a3%\3\2\2\2\u00a4\u00a5\t\3\2\2\u00a5\u00a7\5(\25")
        buf.write("\2\u00a6\u00a4\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\'\3\2\2\2\u00aa\u00a8")
        buf.write("\3\2\2\2\u00ab\u00ac\5,\27\2\u00ac\u00ad\5*\26\2\u00ad")
        buf.write("\u00b0\3\2\2\2\u00ae\u00b0\3\2\2\2\u00af\u00ab\3\2\2\2")
        buf.write("\u00af\u00ae\3\2\2\2\u00b0)\3\2\2\2\u00b1\u00b2\t\4\2")
        buf.write("\2\u00b2\u00b4\5,\27\2\u00b3\u00b1\3\2\2\2\u00b4\u00b7")
        buf.write("\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6")
        buf.write("+\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00b9\5\64\33\2\u00b9")
        buf.write("\u00ba\5.\30\2\u00ba-\3\2\2\2\u00bb\u00bc\78\2\2\u00bc")
        buf.write("\u00bd\5 \21\2\u00bd\u00be\79\2\2\u00be\u00c0\3\2\2\2")
        buf.write("\u00bf\u00bb\3\2\2\2\u00c0\u00c3\3\2\2\2\u00c1\u00bf\3")
        buf.write("\2\2\2\u00c1\u00c2\3\2\2\2\u00c2/\3\2\2\2\u00c3\u00c1")
        buf.write("\3\2\2\2\u00c4\u00c5\5 \21\2\u00c5\u00c6\5\62\32\2\u00c6")
        buf.write("\u00c9\3\2\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00c4\3\2\2\2")
        buf.write("\u00c8\u00c7\3\2\2\2\u00c9\61\3\2\2\2\u00ca\u00cb\7\30")
        buf.write("\2\2\u00cb\u00cd\5 \21\2\u00cc\u00ca\3\2\2\2\u00cd\u00d0")
        buf.write("\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf")
        buf.write("\63\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1\u00e8\7?\2\2\u00d2")
        buf.write("\u00e8\7A\2\2\u00d3\u00e8\7=\2\2\u00d4\u00e8\7>\2\2\u00d5")
        buf.write("\u00db\7<\2\2\u00d6\u00d7\7\66\2\2\u00d7\u00d8\5\60\31")
        buf.write("\2\u00d8\u00d9\7\67\2\2\u00d9\u00dc\3\2\2\2\u00da\u00dc")
        buf.write("\3\2\2\2\u00db\u00d6\3\2\2\2\u00db\u00da\3\2\2\2\u00dc")
        buf.write("\u00e8\3\2\2\2\u00dd\u00de\7\66\2\2\u00de\u00df\5 \21")
        buf.write("\2\u00df\u00e0\7\67\2\2\u00e0\u00e8\3\2\2\2\u00e1\u00e8")
        buf.write("\5\66\34\2\u00e2\u00e3\7\27\2\2\u00e3\u00e4\7\66\2\2\u00e4")
        buf.write("\u00e5\5 \21\2\u00e5\u00e6\7\67\2\2\u00e6\u00e8\3\2\2")
        buf.write("\2\u00e7\u00d1\3\2\2\2\u00e7\u00d2\3\2\2\2\u00e7\u00d3")
        buf.write("\3\2\2\2\u00e7\u00d4\3\2\2\2\u00e7\u00d5\3\2\2\2\u00e7")
        buf.write("\u00dd\3\2\2\2\u00e7\u00e1\3\2\2\2\u00e7\u00e2\3\2\2\2")
        buf.write("\u00e8\65\3\2\2\2\u00e9\u00ea\78\2\2\u00ea\u00eb\5\60")
        buf.write("\31\2\u00eb\u00ec\79\2\2\u00ec\67\3\2\2\2\u00ed\u00f2")
        buf.write("\5\64\33\2\u00ee\u00f2\7<\2\2\u00ef\u00f2\5\30\r\2\u00f0")
        buf.write("\u00f2\5 \21\2\u00f1\u00ed\3\2\2\2\u00f1\u00ee\3\2\2\2")
        buf.write("\u00f1\u00ef\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f29\3\2\2")
        buf.write("\2\21>JW]\u0094\u009e\u00a8\u00af\u00b5\u00c1\u00c8\u00ce")
        buf.write("\u00db\u00e7\u00f1")
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
    RULE_expr = 27

    ruleNames =  [ "program", "statement", "defStatement", "argList", "moreArgs", 
                   "ifStatement", "whileStatement", "forStatement", "returnStatement", 
                   "printStatement", "assignStatement", "functionCallStatement", 
                   "expressionStatement", "sequence", "moreStatements", 
                   "expression", "comparison", "additionExpression", "additionFactor", 
                   "multiplicationExpression", "multiplicationFactor", "elementExpression", 
                   "elementAccess", "expressionList", "moreExpressions", 
                   "primitiveExpression", "listExpression", "expr" ]

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


        def getRuleIndex(self):
            return miParserParser.RULE_program

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProgramASTContext(ProgramContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ProgramContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(miParserParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgramAST" ):
                listener.enterProgramAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgramAST" ):
                listener.exitProgramAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgramAST" ):
                return visitor.visitProgramAST(self)
            else:
                return visitor.visitChildren(self)



    def program(self):

        localctx = miParserParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.ProgramASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.statement()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.IF) | (1 << miParserParser.WHILE) | (1 << miParserParser.FOR) | (1 << miParserParser.RETURN) | (1 << miParserParser.PRINT) | (1 << miParserParser.DEF) | (1 << miParserParser.LEN) | (1 << miParserParser.COMA) | (1 << miParserParser.EQUALS) | (1 << miParserParser.SUM) | (1 << miParserParser.RES) | (1 << miParserParser.MAYORIGUAL) | (1 << miParserParser.MAYOR) | (1 << miParserParser.MENORIGUAL) | (1 << miParserParser.MENOR) | (1 << miParserParser.PARENTESISIZQ) | (1 << miParserParser.BRACKETIZQ) | (1 << miParserParser.ID) | (1 << miParserParser.CHAR_LITERAL) | (1 << miParserParser.RAWSTRINGLITERAL) | (1 << miParserParser.INTLITERAL) | (1 << miParserParser.FLOATLITERAL))) != 0) or _la==miParserParser.NEWLINE:
                self.state = 57
                self.statement()
                self.state = 62
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


        def getRuleIndex(self):
            return miParserParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StatementDefStatementASTContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def defStatement(self):
            return self.getTypedRuleContext(miParserParser.DefStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementDefStatementAST" ):
                listener.enterStatementDefStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementDefStatementAST" ):
                listener.exitStatementDefStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementDefStatementAST" ):
                return visitor.visitStatementDefStatementAST(self)
            else:
                return visitor.visitChildren(self)


    class StatementAssignStatementASTContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignStatement(self):
            return self.getTypedRuleContext(miParserParser.AssignStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementAssignStatementAST" ):
                listener.enterStatementAssignStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementAssignStatementAST" ):
                listener.exitStatementAssignStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementAssignStatementAST" ):
                return visitor.visitStatementAssignStatementAST(self)
            else:
                return visitor.visitChildren(self)


    class StatementPrintStatementASTContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def printStatement(self):
            return self.getTypedRuleContext(miParserParser.PrintStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementPrintStatementAST" ):
                listener.enterStatementPrintStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementPrintStatementAST" ):
                listener.exitStatementPrintStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementPrintStatementAST" ):
                return visitor.visitStatementPrintStatementAST(self)
            else:
                return visitor.visitChildren(self)


    class StatementIfStatementASTContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifStatement(self):
            return self.getTypedRuleContext(miParserParser.IfStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementIfStatementAST" ):
                listener.enterStatementIfStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementIfStatementAST" ):
                listener.exitStatementIfStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementIfStatementAST" ):
                return visitor.visitStatementIfStatementAST(self)
            else:
                return visitor.visitChildren(self)


    class StatementForStatementASTContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def forStatement(self):
            return self.getTypedRuleContext(miParserParser.ForStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementForStatementAST" ):
                listener.enterStatementForStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementForStatementAST" ):
                listener.exitStatementForStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementForStatementAST" ):
                return visitor.visitStatementForStatementAST(self)
            else:
                return visitor.visitChildren(self)


    class StatementFunctionCallStatementASTContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCallStatement(self):
            return self.getTypedRuleContext(miParserParser.FunctionCallStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementFunctionCallStatementAST" ):
                listener.enterStatementFunctionCallStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementFunctionCallStatementAST" ):
                listener.exitStatementFunctionCallStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementFunctionCallStatementAST" ):
                return visitor.visitStatementFunctionCallStatementAST(self)
            else:
                return visitor.visitChildren(self)


    class StatementExpressionStatementASTContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressionStatement(self):
            return self.getTypedRuleContext(miParserParser.ExpressionStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementExpressionStatementAST" ):
                listener.enterStatementExpressionStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementExpressionStatementAST" ):
                listener.exitStatementExpressionStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementExpressionStatementAST" ):
                return visitor.visitStatementExpressionStatementAST(self)
            else:
                return visitor.visitChildren(self)


    class StatementReturnStatementASTContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def returnStatement(self):
            return self.getTypedRuleContext(miParserParser.ReturnStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementReturnStatementAST" ):
                listener.enterStatementReturnStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementReturnStatementAST" ):
                listener.exitStatementReturnStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementReturnStatementAST" ):
                return visitor.visitStatementReturnStatementAST(self)
            else:
                return visitor.visitChildren(self)


    class StatementWhileStatementASTContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def whileStatement(self):
            return self.getTypedRuleContext(miParserParser.WhileStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementWhileStatementAST" ):
                listener.enterStatementWhileStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementWhileStatementAST" ):
                listener.exitStatementWhileStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementWhileStatementAST" ):
                return visitor.visitStatementWhileStatementAST(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = miParserParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = miParserParser.StatementDefStatementASTContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.defStatement()
                pass

            elif la_ == 2:
                localctx = miParserParser.StatementIfStatementASTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.ifStatement()
                pass

            elif la_ == 3:
                localctx = miParserParser.StatementReturnStatementASTContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.returnStatement()
                pass

            elif la_ == 4:
                localctx = miParserParser.StatementPrintStatementASTContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 66
                self.printStatement()
                pass

            elif la_ == 5:
                localctx = miParserParser.StatementWhileStatementASTContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 67
                self.whileStatement()
                pass

            elif la_ == 6:
                localctx = miParserParser.StatementForStatementASTContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 68
                self.forStatement()
                pass

            elif la_ == 7:
                localctx = miParserParser.StatementAssignStatementASTContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 69
                self.assignStatement()
                pass

            elif la_ == 8:
                localctx = miParserParser.StatementFunctionCallStatementASTContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 70
                self.functionCallStatement()
                pass

            elif la_ == 9:
                localctx = miParserParser.StatementExpressionStatementASTContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 71
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


        def getRuleIndex(self):
            return miParserParser.RULE_defStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DefStatementASTContext(DefStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.DefStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefStatementAST" ):
                listener.enterDefStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefStatementAST" ):
                listener.exitDefStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefStatementAST" ):
                return visitor.visitDefStatementAST(self)
            else:
                return visitor.visitChildren(self)



    def defStatement(self):

        localctx = miParserParser.DefStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_defStatement)
        try:
            localctx = miParserParser.DefStatementASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(miParserParser.DEF)
            self.state = 75
            self.match(miParserParser.ID)
            self.state = 76
            self.match(miParserParser.PARENTESISIZQ)
            self.state = 77
            self.argList()
            self.state = 78
            self.match(miParserParser.PARENTESISDER)
            self.state = 79
            self.match(miParserParser.DOSPUNTOS)
            self.state = 80
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


        def getRuleIndex(self):
            return miParserParser.RULE_argList

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EpsilonArgListASTContext(ArgListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ArgListContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEpsilonArgListAST" ):
                listener.enterEpsilonArgListAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEpsilonArgListAST" ):
                listener.exitEpsilonArgListAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEpsilonArgListAST" ):
                return visitor.visitEpsilonArgListAST(self)
            else:
                return visitor.visitChildren(self)


    class MoreArgListASTContext(ArgListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ArgListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(miParserParser.ID, 0)
        def moreArgs(self):
            return self.getTypedRuleContext(miParserParser.MoreArgsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoreArgListAST" ):
                listener.enterMoreArgListAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoreArgListAST" ):
                listener.exitMoreArgListAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoreArgListAST" ):
                return visitor.visitMoreArgListAST(self)
            else:
                return visitor.visitChildren(self)



    def argList(self):

        localctx = miParserParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_argList)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [miParserParser.ID]:
                localctx = miParserParser.MoreArgListASTContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.match(miParserParser.ID)
                self.state = 83
                self.moreArgs()
                pass
            elif token in [miParserParser.PARENTESISDER]:
                localctx = miParserParser.EpsilonArgListASTContext(self, localctx)
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


        def getRuleIndex(self):
            return miParserParser.RULE_moreArgs

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MoreArgsASTContext(MoreArgsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.MoreArgsContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoreArgsAST" ):
                listener.enterMoreArgsAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoreArgsAST" ):
                listener.exitMoreArgsAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoreArgsAST" ):
                return visitor.visitMoreArgsAST(self)
            else:
                return visitor.visitChildren(self)



    def moreArgs(self):

        localctx = miParserParser.MoreArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_moreArgs)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.MoreArgsASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.COMA:
                self.state = 87
                self.match(miParserParser.COMA)
                self.state = 88
                self.match(miParserParser.ID)
                self.state = 93
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


        def getRuleIndex(self):
            return miParserParser.RULE_ifStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfStatementASTContext(IfStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.IfStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatementAST" ):
                listener.enterIfStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatementAST" ):
                listener.exitIfStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatementAST" ):
                return visitor.visitIfStatementAST(self)
            else:
                return visitor.visitChildren(self)



    def ifStatement(self):

        localctx = miParserParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        try:
            localctx = miParserParser.IfStatementASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(miParserParser.IF)
            self.state = 95
            self.expression()
            self.state = 96
            self.match(miParserParser.DOSPUNTOS)
            self.state = 97
            self.sequence()
            self.state = 98
            self.match(miParserParser.ELSE)
            self.state = 99
            self.match(miParserParser.DOSPUNTOS)
            self.state = 100
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


        def getRuleIndex(self):
            return miParserParser.RULE_whileStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WhileStatementASTContext(WhileStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.WhileStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(miParserParser.WHILE, 0)
        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)

        def DOSPUNTOS(self):
            return self.getToken(miParserParser.DOSPUNTOS, 0)
        def sequence(self):
            return self.getTypedRuleContext(miParserParser.SequenceContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatementAST" ):
                listener.enterWhileStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatementAST" ):
                listener.exitWhileStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatementAST" ):
                return visitor.visitWhileStatementAST(self)
            else:
                return visitor.visitChildren(self)



    def whileStatement(self):

        localctx = miParserParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_whileStatement)
        try:
            localctx = miParserParser.WhileStatementASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(miParserParser.WHILE)
            self.state = 103
            self.expression()
            self.state = 104
            self.match(miParserParser.DOSPUNTOS)
            self.state = 105
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


        def getRuleIndex(self):
            return miParserParser.RULE_forStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForStatementASTContext(ForStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ForStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatementAST" ):
                listener.enterForStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatementAST" ):
                listener.exitForStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatementAST" ):
                return visitor.visitForStatementAST(self)
            else:
                return visitor.visitChildren(self)



    def forStatement(self):

        localctx = miParserParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forStatement)
        try:
            localctx = miParserParser.ForStatementASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(miParserParser.FOR)
            self.state = 108
            self.expression()
            self.state = 109
            self.match(miParserParser.IN)
            self.state = 110
            self.expressionList()
            self.state = 111
            self.match(miParserParser.DOSPUNTOS)
            self.state = 112
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


        def getRuleIndex(self):
            return miParserParser.RULE_returnStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReturnStatementASTContext(ReturnStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ReturnStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(miParserParser.RETURN, 0)
        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)

        def NEWLINE(self):
            return self.getToken(miParserParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatementAST" ):
                listener.enterReturnStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatementAST" ):
                listener.exitReturnStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatementAST" ):
                return visitor.visitReturnStatementAST(self)
            else:
                return visitor.visitChildren(self)



    def returnStatement(self):

        localctx = miParserParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_returnStatement)
        try:
            localctx = miParserParser.ReturnStatementASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(miParserParser.RETURN)
            self.state = 115
            self.expression()
            self.state = 116
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


        def getRuleIndex(self):
            return miParserParser.RULE_printStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintStatementASTContext(PrintStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrintStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatementAST" ):
                listener.enterPrintStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatementAST" ):
                listener.exitPrintStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatementAST" ):
                return visitor.visitPrintStatementAST(self)
            else:
                return visitor.visitChildren(self)



    def printStatement(self):

        localctx = miParserParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_printStatement)
        try:
            localctx = miParserParser.PrintStatementASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(miParserParser.PRINT)
            self.state = 119
            self.match(miParserParser.PARENTESISIZQ)
            self.state = 120
            self.expression()
            self.state = 121
            self.match(miParserParser.PARENTESISDER)
            self.state = 122
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


        def getRuleIndex(self):
            return miParserParser.RULE_assignStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignStatementASTContext(AssignStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.AssignStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(miParserParser.ID, 0)
        def ASYGN(self):
            return self.getToken(miParserParser.ASYGN, 0)
        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)

        def NEWLINE(self):
            return self.getToken(miParserParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStatementAST" ):
                listener.enterAssignStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStatementAST" ):
                listener.exitAssignStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatementAST" ):
                return visitor.visitAssignStatementAST(self)
            else:
                return visitor.visitChildren(self)



    def assignStatement(self):

        localctx = miParserParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignStatement)
        try:
            localctx = miParserParser.AssignStatementASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(miParserParser.ID)
            self.state = 125
            self.match(miParserParser.ASYGN)
            self.state = 126
            self.expression()
            self.state = 127
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


        def getRuleIndex(self):
            return miParserParser.RULE_functionCallStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FunctionCallStatementASTContext(FunctionCallStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.FunctionCallStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallStatementAST" ):
                listener.enterFunctionCallStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallStatementAST" ):
                listener.exitFunctionCallStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallStatementAST" ):
                return visitor.visitFunctionCallStatementAST(self)
            else:
                return visitor.visitChildren(self)



    def functionCallStatement(self):

        localctx = miParserParser.FunctionCallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_functionCallStatement)
        try:
            localctx = miParserParser.FunctionCallStatementASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.primitiveExpression()
            self.state = 130
            self.match(miParserParser.PARENTESISIZQ)
            self.state = 131
            self.expressionList()
            self.state = 132
            self.match(miParserParser.PARENTESISDER)
            self.state = 133
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


        def getRuleIndex(self):
            return miParserParser.RULE_expressionStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExpressionStatementASTContext(ExpressionStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ExpressionStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)

        def NEWLINE(self):
            return self.getToken(miParserParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatementAST" ):
                listener.enterExpressionStatementAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatementAST" ):
                listener.exitExpressionStatementAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatementAST" ):
                return visitor.visitExpressionStatementAST(self)
            else:
                return visitor.visitChildren(self)



    def expressionStatement(self):

        localctx = miParserParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expressionStatement)
        try:
            localctx = miParserParser.ExpressionStatementASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.expressionList()
            self.state = 136
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


        def getRuleIndex(self):
            return miParserParser.RULE_sequence

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SequenceASTContext(SequenceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.SequenceContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INDENT(self):
            return self.getToken(miParserParser.INDENT, 0)
        def moreStatements(self):
            return self.getTypedRuleContext(miParserParser.MoreStatementsContext,0)

        def DEDENT(self):
            return self.getToken(miParserParser.DEDENT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequenceAST" ):
                listener.enterSequenceAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequenceAST" ):
                listener.exitSequenceAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequenceAST" ):
                return visitor.visitSequenceAST(self)
            else:
                return visitor.visitChildren(self)



    def sequence(self):

        localctx = miParserParser.SequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_sequence)
        try:
            localctx = miParserParser.SequenceASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(miParserParser.INDENT)
            self.state = 139
            self.moreStatements()
            self.state = 140
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


        def getRuleIndex(self):
            return miParserParser.RULE_moreStatements

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MoreStatementsASTContext(MoreStatementsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.MoreStatementsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(miParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(miParserParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoreStatementsAST" ):
                listener.enterMoreStatementsAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoreStatementsAST" ):
                listener.exitMoreStatementsAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoreStatementsAST" ):
                return visitor.visitMoreStatementsAST(self)
            else:
                return visitor.visitChildren(self)



    def moreStatements(self):

        localctx = miParserParser.MoreStatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_moreStatements)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.MoreStatementsASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.statement()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.IF) | (1 << miParserParser.WHILE) | (1 << miParserParser.FOR) | (1 << miParserParser.RETURN) | (1 << miParserParser.PRINT) | (1 << miParserParser.DEF) | (1 << miParserParser.LEN) | (1 << miParserParser.COMA) | (1 << miParserParser.EQUALS) | (1 << miParserParser.SUM) | (1 << miParserParser.RES) | (1 << miParserParser.MAYORIGUAL) | (1 << miParserParser.MAYOR) | (1 << miParserParser.MENORIGUAL) | (1 << miParserParser.MENOR) | (1 << miParserParser.PARENTESISIZQ) | (1 << miParserParser.BRACKETIZQ) | (1 << miParserParser.ID) | (1 << miParserParser.CHAR_LITERAL) | (1 << miParserParser.RAWSTRINGLITERAL) | (1 << miParserParser.INTLITERAL) | (1 << miParserParser.FLOATLITERAL))) != 0) or _la==miParserParser.NEWLINE:
                self.state = 143
                self.statement()
                self.state = 148
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


        def getRuleIndex(self):
            return miParserParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExpressionASTContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def additionExpression(self):
            return self.getTypedRuleContext(miParserParser.AdditionExpressionContext,0)

        def comparison(self):
            return self.getTypedRuleContext(miParserParser.ComparisonContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionAST" ):
                listener.enterExpressionAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionAST" ):
                listener.exitExpressionAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionAST" ):
                return visitor.visitExpressionAST(self)
            else:
                return visitor.visitChildren(self)



    def expression(self):

        localctx = miParserParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        try:
            localctx = miParserParser.ExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.additionExpression()
            self.state = 150
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


        def getRuleIndex(self):
            return miParserParser.RULE_comparison

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ComparisonASTContext(ComparisonContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ComparisonContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonAST" ):
                listener.enterComparisonAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonAST" ):
                listener.exitComparisonAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonAST" ):
                return visitor.visitComparisonAST(self)
            else:
                return visitor.visitChildren(self)



    def comparison(self):

        localctx = miParserParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.ComparisonASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.EQUALS) | (1 << miParserParser.MAYORIGUAL) | (1 << miParserParser.MAYOR) | (1 << miParserParser.MENORIGUAL) | (1 << miParserParser.MENOR))) != 0):
                self.state = 152
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << miParserParser.EQUALS) | (1 << miParserParser.MAYORIGUAL) | (1 << miParserParser.MAYOR) | (1 << miParserParser.MENORIGUAL) | (1 << miParserParser.MENOR))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 153
                self.additionExpression()
                self.state = 158
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


        def getRuleIndex(self):
            return miParserParser.RULE_additionExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AdditionExpressionASTContext(AdditionExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.AdditionExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def multiplicationExpression(self):
            return self.getTypedRuleContext(miParserParser.MultiplicationExpressionContext,0)

        def additionFactor(self):
            return self.getTypedRuleContext(miParserParser.AdditionFactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditionExpressionAST" ):
                listener.enterAdditionExpressionAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditionExpressionAST" ):
                listener.exitAdditionExpressionAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditionExpressionAST" ):
                return visitor.visitAdditionExpressionAST(self)
            else:
                return visitor.visitChildren(self)



    def additionExpression(self):

        localctx = miParserParser.AdditionExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_additionExpression)
        try:
            localctx = miParserParser.AdditionExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.multiplicationExpression()
            self.state = 160
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


        def getRuleIndex(self):
            return miParserParser.RULE_additionFactor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AdditionFactorASTContext(AdditionFactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.AdditionFactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditionFactorAST" ):
                listener.enterAdditionFactorAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditionFactorAST" ):
                listener.exitAdditionFactorAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditionFactorAST" ):
                return visitor.visitAdditionFactorAST(self)
            else:
                return visitor.visitChildren(self)



    def additionFactor(self):

        localctx = miParserParser.AdditionFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_additionFactor)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.AdditionFactorASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.SUM or _la==miParserParser.RES:
                self.state = 162
                _la = self._input.LA(1)
                if not(_la==miParserParser.SUM or _la==miParserParser.RES):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 163
                self.multiplicationExpression()
                self.state = 168
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


        def getRuleIndex(self):
            return miParserParser.RULE_multiplicationExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MultiplicationExpressionASTContext(MultiplicationExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.MultiplicationExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def elementExpression(self):
            return self.getTypedRuleContext(miParserParser.ElementExpressionContext,0)

        def multiplicationFactor(self):
            return self.getTypedRuleContext(miParserParser.MultiplicationFactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicationExpressionAST" ):
                listener.enterMultiplicationExpressionAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicationExpressionAST" ):
                listener.exitMultiplicationExpressionAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicationExpressionAST" ):
                return visitor.visitMultiplicationExpressionAST(self)
            else:
                return visitor.visitChildren(self)


    class EpsilonMultiplicationExpressionContext(MultiplicationExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.MultiplicationExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEpsilonMultiplicationExpression" ):
                listener.enterEpsilonMultiplicationExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEpsilonMultiplicationExpression" ):
                listener.exitEpsilonMultiplicationExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEpsilonMultiplicationExpression" ):
                return visitor.visitEpsilonMultiplicationExpression(self)
            else:
                return visitor.visitChildren(self)



    def multiplicationExpression(self):

        localctx = miParserParser.MultiplicationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_multiplicationExpression)
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [miParserParser.LEN, miParserParser.PARENTESISIZQ, miParserParser.BRACKETIZQ, miParserParser.ID, miParserParser.CHAR_LITERAL, miParserParser.RAWSTRINGLITERAL, miParserParser.INTLITERAL, miParserParser.FLOATLITERAL]:
                localctx = miParserParser.MultiplicationExpressionASTContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.elementExpression()
                self.state = 170
                self.multiplicationFactor()
                pass
            elif token in [miParserParser.EOF, miParserParser.IN, miParserParser.COMA, miParserParser.DOSPUNTOS, miParserParser.EQUALS, miParserParser.SUM, miParserParser.RES, miParserParser.MAYORIGUAL, miParserParser.MAYOR, miParserParser.MENORIGUAL, miParserParser.MENOR, miParserParser.PARENTESISDER, miParserParser.BRACKETDER, miParserParser.NEWLINE]:
                localctx = miParserParser.EpsilonMultiplicationExpressionContext(self, localctx)
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


        def getRuleIndex(self):
            return miParserParser.RULE_multiplicationFactor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MultiplicationFactorASTContext(MultiplicationFactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.MultiplicationFactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicationFactorAST" ):
                listener.enterMultiplicationFactorAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicationFactorAST" ):
                listener.exitMultiplicationFactorAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicationFactorAST" ):
                return visitor.visitMultiplicationFactorAST(self)
            else:
                return visitor.visitChildren(self)



    def multiplicationFactor(self):

        localctx = miParserParser.MultiplicationFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_multiplicationFactor)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.MultiplicationFactorASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.DIV or _la==miParserParser.MUL:
                self.state = 175
                _la = self._input.LA(1)
                if not(_la==miParserParser.DIV or _la==miParserParser.MUL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 176
                self.elementExpression()
                self.state = 181
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


        def getRuleIndex(self):
            return miParserParser.RULE_elementExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ElementExpressionASTContext(ElementExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ElementExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primitiveExpression(self):
            return self.getTypedRuleContext(miParserParser.PrimitiveExpressionContext,0)

        def elementAccess(self):
            return self.getTypedRuleContext(miParserParser.ElementAccessContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementExpressionAST" ):
                listener.enterElementExpressionAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementExpressionAST" ):
                listener.exitElementExpressionAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementExpressionAST" ):
                return visitor.visitElementExpressionAST(self)
            else:
                return visitor.visitChildren(self)



    def elementExpression(self):

        localctx = miParserParser.ElementExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_elementExpression)
        try:
            localctx = miParserParser.ElementExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.primitiveExpression()
            self.state = 183
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


        def getRuleIndex(self):
            return miParserParser.RULE_elementAccess

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ElementAccessASTContext(ElementAccessContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ElementAccessContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementAccessAST" ):
                listener.enterElementAccessAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementAccessAST" ):
                listener.exitElementAccessAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementAccessAST" ):
                return visitor.visitElementAccessAST(self)
            else:
                return visitor.visitChildren(self)



    def elementAccess(self):

        localctx = miParserParser.ElementAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_elementAccess)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.ElementAccessASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.BRACKETIZQ:
                self.state = 185
                self.match(miParserParser.BRACKETIZQ)
                self.state = 186
                self.expression()
                self.state = 187
                self.match(miParserParser.BRACKETDER)
                self.state = 193
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


        def getRuleIndex(self):
            return miParserParser.RULE_expressionList

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EpsilonExpressionListContext(ExpressionListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ExpressionListContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEpsilonExpressionList" ):
                listener.enterEpsilonExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEpsilonExpressionList" ):
                listener.exitEpsilonExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEpsilonExpressionList" ):
                return visitor.visitEpsilonExpressionList(self)
            else:
                return visitor.visitChildren(self)


    class ExpressionListASTContext(ExpressionListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ExpressionListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)

        def moreExpressions(self):
            return self.getTypedRuleContext(miParserParser.MoreExpressionsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionListAST" ):
                listener.enterExpressionListAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionListAST" ):
                listener.exitExpressionListAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionListAST" ):
                return visitor.visitExpressionListAST(self)
            else:
                return visitor.visitChildren(self)



    def expressionList(self):

        localctx = miParserParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expressionList)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = miParserParser.ExpressionListASTContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.expression()
                self.state = 195
                self.moreExpressions()
                pass

            elif la_ == 2:
                localctx = miParserParser.EpsilonExpressionListContext(self, localctx)
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


        def getRuleIndex(self):
            return miParserParser.RULE_moreExpressions

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MoreExpressionsASTContext(MoreExpressionsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.MoreExpressionsContext
            super().__init__(parser)
            self.copyFrom(ctx)

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


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoreExpressionsAST" ):
                listener.enterMoreExpressionsAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoreExpressionsAST" ):
                listener.exitMoreExpressionsAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoreExpressionsAST" ):
                return visitor.visitMoreExpressionsAST(self)
            else:
                return visitor.visitChildren(self)



    def moreExpressions(self):

        localctx = miParserParser.MoreExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_moreExpressions)
        self._la = 0 # Token type
        try:
            localctx = miParserParser.MoreExpressionsASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==miParserParser.COMA:
                self.state = 200
                self.match(miParserParser.COMA)
                self.state = 201
                self.expression()
                self.state = 206
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


        def getRuleIndex(self):
            return miParserParser.RULE_primitiveExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrimitiveExpressionCHAR_LITERALContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR_LITERAL(self):
            return self.getToken(miParserParser.CHAR_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExpressionCHAR_LITERAL" ):
                listener.enterPrimitiveExpressionCHAR_LITERAL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExpressionCHAR_LITERAL" ):
                listener.exitPrimitiveExpressionCHAR_LITERAL(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExpressionCHAR_LITERAL" ):
                return visitor.visitPrimitiveExpressionCHAR_LITERAL(self)
            else:
                return visitor.visitChildren(self)


    class PrimitiveExpressionIDContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(miParserParser.ID, 0)
        def PARENTESISIZQ(self):
            return self.getToken(miParserParser.PARENTESISIZQ, 0)
        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)

        def PARENTESISDER(self):
            return self.getToken(miParserParser.PARENTESISDER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExpressionID" ):
                listener.enterPrimitiveExpressionID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExpressionID" ):
                listener.exitPrimitiveExpressionID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExpressionID" ):
                return visitor.visitPrimitiveExpressionID(self)
            else:
                return visitor.visitChildren(self)


    class PrimitiveExpressionExpressionContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PARENTESISIZQ(self):
            return self.getToken(miParserParser.PARENTESISIZQ, 0)
        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)

        def PARENTESISDER(self):
            return self.getToken(miParserParser.PARENTESISDER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExpressionExpression" ):
                listener.enterPrimitiveExpressionExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExpressionExpression" ):
                listener.exitPrimitiveExpressionExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExpressionExpression" ):
                return visitor.visitPrimitiveExpressionExpression(self)
            else:
                return visitor.visitChildren(self)


    class PrimitiveExpressionListExpressionContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def listExpression(self):
            return self.getTypedRuleContext(miParserParser.ListExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExpressionListExpression" ):
                listener.enterPrimitiveExpressionListExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExpressionListExpression" ):
                listener.exitPrimitiveExpressionListExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExpressionListExpression" ):
                return visitor.visitPrimitiveExpressionListExpression(self)
            else:
                return visitor.visitChildren(self)


    class PrimitiveExpressionFLOATLITERALContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOATLITERAL(self):
            return self.getToken(miParserParser.FLOATLITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExpressionFLOATLITERAL" ):
                listener.enterPrimitiveExpressionFLOATLITERAL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExpressionFLOATLITERAL" ):
                listener.exitPrimitiveExpressionFLOATLITERAL(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExpressionFLOATLITERAL" ):
                return visitor.visitPrimitiveExpressionFLOATLITERAL(self)
            else:
                return visitor.visitChildren(self)


    class PrimitiveExpressionINTLITERALContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTLITERAL(self):
            return self.getToken(miParserParser.INTLITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExpressionINTLITERAL" ):
                listener.enterPrimitiveExpressionINTLITERAL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExpressionINTLITERAL" ):
                listener.exitPrimitiveExpressionINTLITERAL(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExpressionINTLITERAL" ):
                return visitor.visitPrimitiveExpressionINTLITERAL(self)
            else:
                return visitor.visitChildren(self)


    class PrimitiveExpressionRAWSTRINGLITERALContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RAWSTRINGLITERAL(self):
            return self.getToken(miParserParser.RAWSTRINGLITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExpressionRAWSTRINGLITERAL" ):
                listener.enterPrimitiveExpressionRAWSTRINGLITERAL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExpressionRAWSTRINGLITERAL" ):
                listener.exitPrimitiveExpressionRAWSTRINGLITERAL(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExpressionRAWSTRINGLITERAL" ):
                return visitor.visitPrimitiveExpressionRAWSTRINGLITERAL(self)
            else:
                return visitor.visitChildren(self)


    class PrimitiveExpressionLENContext(PrimitiveExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.PrimitiveExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LEN(self):
            return self.getToken(miParserParser.LEN, 0)
        def PARENTESISIZQ(self):
            return self.getToken(miParserParser.PARENTESISIZQ, 0)
        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)

        def PARENTESISDER(self):
            return self.getToken(miParserParser.PARENTESISDER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveExpressionLEN" ):
                listener.enterPrimitiveExpressionLEN(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveExpressionLEN" ):
                listener.exitPrimitiveExpressionLEN(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveExpressionLEN" ):
                return visitor.visitPrimitiveExpressionLEN(self)
            else:
                return visitor.visitChildren(self)



    def primitiveExpression(self):

        localctx = miParserParser.PrimitiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_primitiveExpression)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [miParserParser.INTLITERAL]:
                localctx = miParserParser.PrimitiveExpressionINTLITERALContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.match(miParserParser.INTLITERAL)
                pass
            elif token in [miParserParser.FLOATLITERAL]:
                localctx = miParserParser.PrimitiveExpressionFLOATLITERALContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.match(miParserParser.FLOATLITERAL)
                pass
            elif token in [miParserParser.CHAR_LITERAL]:
                localctx = miParserParser.PrimitiveExpressionCHAR_LITERALContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self.match(miParserParser.CHAR_LITERAL)
                pass
            elif token in [miParserParser.RAWSTRINGLITERAL]:
                localctx = miParserParser.PrimitiveExpressionRAWSTRINGLITERALContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 210
                self.match(miParserParser.RAWSTRINGLITERAL)
                pass
            elif token in [miParserParser.ID]:
                localctx = miParserParser.PrimitiveExpressionIDContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 211
                self.match(miParserParser.ID)
                self.state = 217
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 212
                    self.match(miParserParser.PARENTESISIZQ)
                    self.state = 213
                    self.expressionList()
                    self.state = 214
                    self.match(miParserParser.PARENTESISDER)
                    pass

                elif la_ == 2:
                    pass


                pass
            elif token in [miParserParser.PARENTESISIZQ]:
                localctx = miParserParser.PrimitiveExpressionExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 219
                self.match(miParserParser.PARENTESISIZQ)
                self.state = 220
                self.expression()
                self.state = 221
                self.match(miParserParser.PARENTESISDER)
                pass
            elif token in [miParserParser.BRACKETIZQ]:
                localctx = miParserParser.PrimitiveExpressionListExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 223
                self.listExpression()
                pass
            elif token in [miParserParser.LEN]:
                localctx = miParserParser.PrimitiveExpressionLENContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 224
                self.match(miParserParser.LEN)
                self.state = 225
                self.match(miParserParser.PARENTESISIZQ)
                self.state = 226
                self.expression()
                self.state = 227
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


        def getRuleIndex(self):
            return miParserParser.RULE_listExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ListExpressionASTContext(ListExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a miParserParser.ListExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BRACKETIZQ(self):
            return self.getToken(miParserParser.BRACKETIZQ, 0)
        def expressionList(self):
            return self.getTypedRuleContext(miParserParser.ExpressionListContext,0)

        def BRACKETDER(self):
            return self.getToken(miParserParser.BRACKETDER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListExpressionAST" ):
                listener.enterListExpressionAST(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListExpressionAST" ):
                listener.exitListExpressionAST(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExpressionAST" ):
                return visitor.visitListExpressionAST(self)
            else:
                return visitor.visitChildren(self)



    def listExpression(self):

        localctx = miParserParser.ListExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_listExpression)
        try:
            localctx = miParserParser.ListExpressionASTContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(miParserParser.BRACKETIZQ)
            self.state = 232
            self.expressionList()
            self.state = 233
            self.match(miParserParser.BRACKETDER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveExpression(self):
            return self.getTypedRuleContext(miParserParser.PrimitiveExpressionContext,0)


        def ID(self):
            return self.getToken(miParserParser.ID, 0)

        def functionCallStatement(self):
            return self.getTypedRuleContext(miParserParser.FunctionCallStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(miParserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return miParserParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = miParserParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.primitiveExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(miParserParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.functionCallStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 238
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





