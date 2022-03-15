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