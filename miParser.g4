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
//1,4,5,15,17,19,21,23 y 25

/*
    N       X           Y           N
program := statement | statement Program

N ::= X | N Y  ->  N::= X Y*

*/

//1.	Program := Statement | Statement Program
//program : statement | statement program  ;
program : statement statement * ;

//2. Statement := DefStatement | IfStatement | ReturnStatement | PrintStatement | WhileStatement | ForStatement | AssignStatment | FunctionCallStatement | ExpressionStatement
statement : defStatement
            | ifStatement
            | returnStatement
            | printStatement
            | whileStatement
            | forStatement
            | assignStatement
            | functionCallStatement
            | expressionStatement;
//3.	DefStatement := def identifier ( ArgList ) : Sequence
defStatement : DEF ID ( argList ) DOSPUNTOS sequence;
//4.	ArgList := identifier MoreArgs | ε
argList : ID moreArgs | ;///identifider*
//5.	MoreArgs := , identifier MoreArgs | ε
moreArgs : COMA ID moreArgs |  ;
//6.	IfStatement := if Expression : Sequence else : Sequence
ifStatement : IF expression DOSPUNTOS sequence ELSE DOSPUNTOS sequence;
//7.	WhileStatement := while Expression : Sequence
whileStatement : WHILE expression DOSPUNTOS sequence;
//8.	ForStatement := for Expression in ExpressionList : Sequence
forStatement : FOR expression IN expressionList DOSPUNTOS sequence;
//9.	ReturnStatement := return Expression NEWLINE
returnStatement : RETURN expression NEWLINE;
//10.	PrintStatement := print Expression NEWLINE
printStatement : PRINT expression NEWLINE;
//11.	AssignStatement := identifier = Expression NEWLINE
assignStatement : ID EQUALS expression NEWLINE;
//12.	FunctionCallStatement := PrimitiveExpression ( ExpressionList ) NEWLINE
functionCallStatement : primitiveExpression PARENTESISIZQ expressionList PARENTESISDER NEWLINE;
//13.	ExpressionStatement := ExpressionList NEWLINE
expressionStatement : expressionList NEWLINE;
//14.	Sequence := INDENT MoreStatements DEDENT
sequence : INDENT moreStatements DEDENT;

//N ::= X | N Y  ->  N::= X Y*
//            N               x           n              Y
//15.	MoreStatements := Statement MoreStatements | Statement
moreStatements : statement  statement*;
//16.	Expression := AdditionExpression Comparison
expression : additionExpression comparison;
//          N               x               y               n
//17.	Comparison := (<|>|<=|>=|==) AdditionExpression*
comparison : (MENOR|MAYOR|MENORIGUAL|MAYORIGUAL|EQUALS) additionExpression* ;
//18.	AdditionExpression := MultiplicationExpression AdditionFactor
additionExpression : multiplicationExpression additionFactor;
//19.	AdditionFactor := (+|-) MultiplicationExpression AdditionFactor | ε
// N                 X                Y                       N
additionFactor : (SUM|RES) multiplicationExpression* ;
//20.	MultiplicationExpression := ElementExpression MultiplicationFactor
multiplicationExpression : elementExpression multiplicationFactor | ;
//21.	MultiplicationFactor := (*|/) ElementExpression MultiplicationFactor | ε
//      N                    X                Y                      N
multiplicationFactor : (MUL|DIV) elementExpression*   ;
//22.	ElementExpression := PrimitiveExpression ElementAccess
elementExpression : primitiveExpression elementAccess;
//23.	ElementAccess := [ Expression ] ElementAcess | ε
// N                        X                          N            Y
//elementAccess : BRACKETIZQ expression BRACKETDER elementAccess |  ;
elementAccess : BRACKETIZQ expression BRACKETDER  |  ;

//24.	ExpressionList := Expression MoreExpressions | ε
expressionList : expression moreExpressions |  ;
//25.	MoreExpressions := , Expression MoreExpressions | ε
//  N                       X           N           Y
//moreExpressions : COMA expression moreExpressions |  ;
moreExpressions : COMA expression  |  ;

//26.	PrimitiveExpression := integer | float | charConst |  String | identifier (( ExpressionList ) | ε ) | ( Expression ) | ListExpression | len ( Expression )
primitiveExpression : INTLITERAL
                    | FLOATLITERAL
                    | LETTER
                    | RAWSTRINGLITERAL
                    | ID (( expressionList ) |   )
                    | ( expression )
                    | listExpression
                    | LEN ( expression );

//27.	ListExpression := [ ExpressionList ]
listExpression : BRACKETIZQ expressionList BRACKETDER;

//////////////////////////////////////////////////////////////////////////////////

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