lexer grammar Grammar;

//Tokens de MiniPy
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



// PALABRAS RESERVADAS
IF : 'if';
ELSE : 'else';
FOR : 'for';
IN:'in';
BREAK : 'break';
CONTINUE : 'continue';
RETURN : 'return';
PRINT : 'print';
PRINTLN: 'println';//¿R.10?
PACKAGE : 'package';
VAR: 'var';
TYPE: 'type';
DEF: 'def';
STRUCT: 'struct';
APPEND: 'append';
LEN : 'len';
CAP: 'cap';
WHILE: 'while';




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
ANDTECHO: '&^';
ANDIGUAL: '&=';
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
DOBLEMENORQUEIGUAL: '<<=';
DOBLEMAYORQUE: '>>';
DOBLEMAYORQUEIGUAL: '>>=';
ELEVADO:'^';
ELEVADOIGUAL: '^=';
ANDELEVADOIGUAL: '&^=';
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



///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
program : statement | statement program;

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

//14.	Sequence := NEWLINE INDENT MoreStatements DEDENT //preguntar







//1.	Program := Statement | Statement Program
//2.	Statement := DefStatement | IfStatement | ReturnStatement | PrintStatement | WhileStatement | ForStatement | AssignStatment | FunctionCallStatement | ExpressionStatement
//3.	DefStatement := def identifier ( ArgList ) : Sequence
//4.	ArgList := identifier Arglist | ε
//5.	MoreArgs := , identifier MoreArgs | ε
//6.	IfStatement := if Expression : Sequence else : Sequence
//7.	WhileStatement := while Expression : Sequence
//8.	ForStatement := for Expression in ExpressionList : Sequence
//9.	ReturnStatement := return Expression NEWLINE
//10.	PrintStatement := print Expression NEWLINE
//11.	AssignStatement := identifier = Expression NEWLINE
//12.	FunctionCallStatement := PrimitiveExpression ( ExpressionList ) NEWLINE
//13.	ExpressionStatement := ExpressionList NEWLINE
//14.	Sequence := NEWLINE INDENT MoreStatements DEDENT
//15.	MoreStatements := Statement MoreStatements | Statement
//16.	Expression := AdditionExpression Comparison
//17.	Comparison := (<|>|<=|>=|==) AdditionExpression Comparison | ε
//18.	AdditionExpression := MultiplicationExpression AdditionFactor
//19.	AdditionFactor := (+|-) MultiplicationExpression AdditionFactor | ε
//20.	MultiplicationExpression := ElementExpression MultiplicationFactor
//21.	MultiplicationFactor := (*|/) ElementExpression MultiplicationFactor | ε
//22.	ElementExpression := PrimitiveExpression ElementAccess
//23.	ElementAccess := [ Expression ] ElementAcess | ε
//24.	ExpressionList := Expression MoreExpressions | ε
//25.	MoreExpressions := , Expression MoreExpressions | ε
//26.	PrimitiveExpression := Integer | String | NAME | ( Expression ) | ListExpression | len ( Expression ) | FunctionCallExpression
//27.	ListExpression := [ ExpressionList ]
