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
N ::= X | N Y  ->  N::= X Y*
*/

//1.	Program := Statement | Statement Program
//    N       X           Y           N
//program := statement | statement Program
program : statement statement *                                                                 #programAST;

//2. Statement := DefStatement | IfStatement | ReturnStatement | PrintStatement | WhileStatement | ForStatement | AssignStatment | FunctionCallStatement | ExpressionStatement
statement : defStatement                                                                        #statementDefStatementAST
            | ifStatement                                                                       #statementIfStatementAST
            | returnStatement                                                                   #statementReturnStatementAST
            | printStatement                                                                    #statementPrintStatementAST
            | whileStatement                                                                    #statementWhileStatementAST
            | forStatement                                                                      #statementForStatementAST
            | assignStatement                                                                   #statementAssignStatementAST
            | functionCallStatement                                                             #statementFunctionCallStatementAST
            | expressionStatement                                                               #statementExpressionStatementAST;
//3.	DefStatement := def identifier ( ArgList ) : Sequence
defStatement : DEF ID PARENTESISIZQ argList PARENTESISDER DOSPUNTOS sequence                    #defStatementAST;
//4.	ArgList := identifier MoreArgs | ε
argList : ID moreArgs                                                                           #moreArgListAST
            |                                                                                   #epsilonArgListAST;
//          N
//5.	MoreArgs := , identifier MoreArgs | ε
moreArgs : (COMA ID)*                                                                           #moreArgsAST;
//6.	IfStatement := if Expression : Sequence else : Sequence
ifStatement : IF expression DOSPUNTOS sequence ( ELSE DOSPUNTOS sequence | )                    #ifStatementAST;
//7.	WhileStatement := while Expression : Sequence
whileStatement : WHILE expression DOSPUNTOS sequence                                            #whileStatementAST;
//8.	ForStatement := for Expression in ExpressionList : Sequence
forStatement : FOR expression IN expressionList DOSPUNTOS sequence                              #forStatementAST;
//9.	ReturnStatement := return Expression NEWLINE
returnStatement : RETURN expression NEWLINE                                                     #returnStatementAST;
//10.	PrintStatement := print Expression NEWLINE
printStatement : PRINT PARENTESISIZQ expression PARENTESISDER NEWLINE                           #printStatementAST;
//11.	AssignStatement := identifier = Expression NEWLINE
assignStatement : ID ASYGN expression NEWLINE                                                   #assignStatementAST;
//12.	FunctionCallStatement := PrimitiveExpression ( ExpressionList ) NEWLINE
functionCallStatement : primitiveExpression PARENTESISIZQ expressionList PARENTESISDER NEWLINE  #functionCallStatementAST;
//13.	ExpressionStatement := ExpressionList NEWLINE
expressionStatement : expressionList NEWLINE                                                    #expressionStatementAST;
//14.	Sequence := INDENT MoreStatements DEDENT
sequence : INDENT moreStatements DEDENT                                                         #sequenceAST;

//N ::= X | N Y  ->  N::= X Y*
//            N               x           n              Y
//15.	MoreStatements := Statement MoreStatements | Statement
moreStatements : statement  statement*                                                          #moreStatementsAST;
//16.	Expression := AdditionExpression Comparison
expression : additionExpression comparison                                                      #expressionAST;
//          N               x               y               n
//17.	Comparison := (<|>|<=|>=|==) AdditionExpression*
comparison : ( (MENOR|MAYOR|MENORIGUAL|MAYORIGUAL|EQUALS) additionExpression )*                 #comparisonAST;
//18.	AdditionExpression := MultiplicationExpression AdditionFactor
additionExpression : multiplicationExpression additionFactor                                    #additionExpressionAST;
//19.	AdditionFactor := (+|-) MultiplicationExpression AdditionFactor | ε
// N                 X                Y                       N
additionFactor :( (SUM|RES) multiplicationExpression )*                                         #additionFactorAST;
//20.	MultiplicationExpression := ElementExpression MultiplicationFactor
multiplicationExpression : elementExpression multiplicationFactor                               #multiplicationExpressionAST
                            |                                                                   #epsilonMultiplicationExpression;
//21.	MultiplicationFactor := (*|/) ElementExpression MultiplicationFactor | ε
//      N                    X                Y                      N
multiplicationFactor :( (MUL|DIV) elementExpression )*                                          #multiplicationFactorAST;
//22.	ElementExpression := PrimitiveExpression ElementAccess
elementExpression : primitiveExpression elementAccess                                           #elementExpressionAST;
//23.	ElementAccess := [ Expression ] ElementAcess | ε
// N                        X                          N            Y
//elementAccess : BRACKETIZQ expression BRACKETDER elementAccess |  ;
elementAccess : (BRACKETIZQ expression BRACKETDER)*                                             #elementAccessAST;

//24.	ExpressionList := Expression MoreExpressions | ε
expressionList : expression moreExpressions                                                     #expressionListAST
                |                                                                               #epsilonExpressionList;
//25.	MoreExpressions := , Expression MoreExpressions | ε
//  N                       X           N           Y
//moreExpressions : COMA expression moreExpressions |  ;
moreExpressions : (COMA expression)*                                                            #moreExpressionsAST;

//26.	PrimitiveExpression := integer | float | charConst |  String | identifier (( ExpressionList ) | ε ) | ( Expression ) | ListExpression | len ( Expression )
primitiveExpression : INTLITERAL                                                                #primitiveExpressionINTLITERAL
                    | FLOATLITERAL                                                              #primitiveExpressionFLOATLITERAL
                    | CHAR_LITERAL                                                              #primitiveExpressionCHAR_LITERAL
                    | RAWSTRINGLITERAL                                                          #primitiveExpressionRAWSTRINGLITERAL
                    | ID (PARENTESISIZQ expressionList PARENTESISDER |   )                      #primitiveExpressionID
                    | PARENTESISIZQ expression PARENTESISDER                                    #primitiveExpressionExpression
                    | listExpression                                                            #primitiveExpressionListExpression
                    | LEN PARENTESISIZQ expression PARENTESISDER                                #primitiveExpressionLEN;

//27.	ListExpression := [ ExpressionList ]
listExpression : BRACKETIZQ expressionList BRACKETDER                                           #listExpressionAST;


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

COMA:',';
PyCOMA : ';';
PUNTO:'.';
DOSPUNTOS:':';
DOSPUNTOSIGUAL: ':=';

ASYGN : '=';
EQUALS : '==';
SUM : '+';
SUM2: '++';
SUMIGUAL: '+=';
RES : '-';
RES2: '--';
RESIGUAL: '-=';
DIV : '/';
DIVIGUAL: '/=';
MUL : '*';
MULIGUAL: '*=';

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
OR:'|';
ORIGUAL: '|=';


PARENTESISIZQ:'(';
PARENTESISDER:')';
BRACKETIZQ:'[';
BRACKETDER:']';
LLAVEIZQ:'{';
LLAVEDER:'}';




//************LITERALS*******************+
ID : LETTER (LETTER|DIGIT)*;
CHAR_LITERAL:  '\\' [btnfr"'\\]
            |     '\'' ~['\\\r\n] '\''
            |'\\' 'u'+ [0-9a-fA-F];

RAWSTRINGLITERAL: '"' ~'"'* '"' ;
INTLITERAL: DIGIT DIGIT* ;


FLOATLITERAL: DECIMAL_FLOAT_LIT | HEX_FLOAT_LIT;

DECIMAL_FLOAT_LIT      : DECIMALS ('.' DECIMALS? EXPONENT? | EXPONENT)
                       | '.' DECIMALS EXPONENT?;

HEX_FLOAT_LIT          : '0' [xX] HEX_MANTISSA HEX_EXPONENT;
fragment HEX_MANTISSA  : ('_'? HEX_DIGIT)+ ('.' ( '_'? HEX_DIGIT )*)?
                       | '.' HEX_DIGIT ('_'? HEX_DIGIT)*;
fragment DIGIT : [0-9];
fragment DECIMALS: [0-9] ('_'? [0-9])*;
fragment HEX_EXPONENT  : [pP] [+-] DECIMALS;
fragment EXPONENT: [eE] [+-]? DECIMALS;
fragment HEX_DIGIT: [0-9a-fA-F];

fragment LETTER : '_'  | [a-z] | [A-Z];
// [a-zA-Z\u0080-\u00FF_];

BLOK_COMMENT : '"""' .*? '"""' -> skip;
COMMENT : '#' ~[\r\n\f]+ ->skip;
WS  :   [ +\r\n\t\f] -> skip ;
NEWLINE: ('\r'? '\n' (' ' | '\t')*); //For tabs just switch out ' '* with '\t'*
