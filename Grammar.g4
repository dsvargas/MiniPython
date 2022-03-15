lexer grammar Grammar;

//Tokens de MiniPy

// PALABRAS RESERVADAS
IF : 'if';
ELSE : 'else';
SWITCH : 'switch';
CASE : 'case';
DEFAULT : 'default';
FOR : 'for';
BREAK : 'break';
CONTINUE : 'continue';
RETURN : 'return';
PRINT : 'print';
PRINTLN: 'println';
PACKAGE : 'package';
VAR: 'var';
TYPE: 'type';
FUNC: 'func';
STRUCT: 'struct';
APPEND: 'append';
LEN : 'len';
CAP: 'cap';

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

//-------------------------------------------------------
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
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
program : statement | statement Program;

statement : defStatement
            | ifStatement
            | returnStatement
            | printStatement
            | whileStatement
            | forStatement
            | assignStatment
            | functionCallStatement
            | expressionStatement;

defStatement : def identifier ( argList ) DOSPUNTOS Sequence;

argList : identifier arglist | ε;

moreArgs :  identifier moreArgs | ε;
ifStatement : If expression DOSPUNTOS sequence else DOSPUNTOS sequence;

whileStatement : While expression DOSPUNTOS sequence;
forStatement : For expression IN expressionList DOSPUNTOS Sequence;

returnStatement : RETURN expression NEWLINE;
printStatement : PRINT expression NEWLINE;

assignStatement : identifier IGUAL expression NEWLINE;

functionCallStatement : primitiveExpression PARENTESISIZQ expressionList PARENTESISDER NEWLINE;

expressionStatement : expressionList NEWLINE;

sequence : NEWLINE INDENT MoreStatements DEDENT;

moreStatements : statement moreStatements
                | statement;

expression : additionExpression comparison;
comparison : (<|>|<=|>=|==) AdditionExpression Comparison | ε;
additionExpression : multiplicationExpression additionFactor;
additionFactor : (+|-) MultiplicationExpression AdditionFactor | ε;
multiplicationExpression : elementExpression multiplicationFactor;

multiplicationFactor : (*|/) elementExpression multiplicationFactor | ε;

elementExpression : primitiveExpression ElementAccess;
elementAccess : BRACKETIZQ expression BRACKETDER elementAcess | ε;

functionCallExpression : primitiveExpression ( expressionList );
expressionList : expression moreExpressions | ε;
moreExpressions : COMA expression moreExpressions | ε;
primitiveExpression : Integer
                    | String
                    | NAME
                    | ( expression )
                    | listExpression
                    | len ( expression )
                    | functionCallExpression;

listExpression : BRACKETIZQ expressionList BRACKETDER;

14.	Sequence := NEWLINE INDENT MoreStatements DEDENT //preguntar







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
//24.	FunctionCallExpression := PrimitiveExpression ( ExpressionList )
//25.	ExpressionList := Expression MoreExpressions | ε
//26.	MoreExpressions := , Expression MoreExpressions | ε
//27.	PrimitiveExpression := Integer | String | NAME | ( Expression ) | ListExpression | len ( Expression ) | FunctionCallExpression
//28.	ListExpression := [ ExpressionList ]
