grammar miParser;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from miParserParser import miParserParser
}
@lexer::members {
class MyCoolDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: miParserLexer = lexer

    def pull_token(self):
        return super(miParserLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.MyCoolDenter(self, self.NEWLINE, miParserParser.INDENT, miParserParser.DEDENT, False)
    return self.denter.next_token()
}


program : statement | statement program  ;
statement : defStatement
            | ifStatement
            | returnStatement
            | printStatement
            | whileStatement
            | forStatement
            | assignStatement
            | functionCallStatement
            | expressionStatement;

defStatement : DEF ID ( argList ) DOSPUNTOS sequence;

argList : ID argList | ;

moreArgs :  ID moreArgs |  ;

ifStatement : IF expression DOSPUNTOS sequence ELSE DOSPUNTOS sequence;

whileStatement : WHILE expression DOSPUNTOS sequence;

forStatement : FOR expression IN expressionList DOSPUNTOS sequence;

returnStatement : RETURN expression NEWLINE;

printStatement : PRINT expression NEWLINE;

assignStatement : ID EQUALS expression NEWLINE;

functionCallStatement : primitiveExpression PARENTESISIZQ expressionList PARENTESISDER NEWLINE;

expressionStatement : expressionList NEWLINE;

sequence : INDENT moreStatements DEDENT;

moreStatements : statement moreStatements
                | statement;

expression : additionExpression comparison;

comparison : (MENOR|MAYOR|MENORIGUAL|MAYORIGUAL|EQUALS) additionExpression comparison |  ;

additionExpression : multiplicationExpression additionFactor;

additionFactor : (SUM|RES) multiplicationExpression additionFactor |  ;

multiplicationExpression : elementExpression multiplicationFactor;

multiplicationFactor : (MUL|DIV) elementExpression multiplicationFactor |  ;

elementExpression : primitiveExpression elementAccess;

elementAccess : BRACKETIZQ expression BRACKETDER elementAccess |  ;

functionCallExpression : primitiveExpression ( expressionList );

expressionList : expression moreExpressions |  ;

moreExpressions : COMA expression moreExpressions |  ;

primitiveExpression : INTLITERAL
                    | FLOATLITERAL
                    | LETTER
                    | RAWSTRINGLITERAL
                    | ID (( expressionList ) |   )
                    | ( expression )
                    | listExpression
                    | LEN ( expression );

listExpression : BRACKETIZQ expressionList BRACKETDER;

// PALABRAS RESERVADAS

IF : 'if';
ELSE : 'else';

WHILE : 'while';
DO : 'do';
BREAK : 'break';
FOR : 'for';
IN : 'in';
BEGIN : 'begin';
END : 'end';
LET : 'let';
CONST : 'const';
VAR : 'var';
CONTINUE : 'continue';
RETURN : 'return';
PRINT : 'print';
PACKAGE : 'package';
TYPE: 'type';
DEF: 'def';
STRUCT: 'struct';
APPEND: 'append';
LEN : 'len';




// SIMBOLOS
PyCOMA : ';';
EQUALS : '==';
ASYGN : '=';
SUM2: '++';
SUMIGUAL: '+=';
SUM : '+';
RES2: '--';
RESIGUAL: '-=';
RES : '-';
DIVIGUAL: '/=';
DIV : '/';
MULIGUAL: '*=';
MUL : '*';
DIF : '!=';
ADMIRACION : '!';
MAYORIGUAL : '>=';
MAYOR : '>';
MENORIGUAL: '<=';
MENOR : '<';
PORCENTAJE: '%';
PORCENTAJEIGUAL: '%=';


AND2:'&&';
AND:'&';
OR2:'||';
ORIGUAL: '|=';
OR:'|';
PARENTESISIZQ:'(';
PARENTESISDER:')';
COMA:',';
PUNTO:'.';
DOSPUNTOS:':';
DOSPUNTOSIGUAL: ':=';
BRACKETIZQ:'[';
BRACKETDER:']';
DOBLEMENORQUE: '<<';

DOBLEMAYORQUE: '>>';

ELEVADO:'^';
ELEVADOIGUAL: '^=';

GUIONBAJO:'_';
LLAVEIZQ:'{';
LLAVEDER:'}';




//************LITERALS*******************+
INTLITERAL: DIGIT DIGIT* ;
fragment DIGIT : [0-9];

FLOATLITERAL: DECIMAL_FLOAT_LIT | HEX_FLOAT_LIT;
DECIMAL_FLOAT_LIT      : DECIMALS ('.' DECIMALS? EXPONENT? | EXPONENT)
                       | '.' DECIMALS EXPONENT?;
HEX_FLOAT_LIT          : '0' [xX] HEX_MANTISSA HEX_EXPONENT;
fragment HEX_MANTISSA  : ('_'? HEX_DIGIT)+ ('.' ( '_'? HEX_DIGIT )*)?
                       | '.' HEX_DIGIT ('_'? HEX_DIGIT)*;
fragment HEX_EXPONENT  : [pP] [+-] DECIMALS;
fragment DECIMALS: [0-9] ('_'? [0-9])*;
fragment EXPONENT: [eE] [+-]? DECIMALS;
fragment HEX_DIGIT: [0-9a-fA-F];

//-------------------------------------------------------
ID : LETTER (LETTER+DIGIT)*;
fragment LETTER : [a-z];

RAWSTRINGLITERAL: '`' ~'`'*                      '`';

NEWLINE: ('\r'? '\n' (' ' | '\t')*); //For tabs just switch out ' '* with '\t'*

WS  :   [ +\r\n\t] -> skip ;




