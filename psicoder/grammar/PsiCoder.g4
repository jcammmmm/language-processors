grammar PsiCoder;

program
    : definitions 'funcion_principal' block 'fin_principal' definitions;

definitions
    : (definition)*
    ;

definition
    : function
    | structure
    ;

function
    : 'funcion'
    ;
    
structure
    : 'estructura'
    ;

block
    : (declaration)*
    | //
    ;

declaration
    : TYPE dclrBody (',' dclrBody)* SMCOLON;

dclrBody
    : ID '=' LITERAL
    | ID '=' ID
    | ID '=' arithExpr
    | //
    ;

arithExpr
    : (LIT_NUM | ID) BIN_OP arithExpr
    | '(' arithExpr ')' (BIN_OP arithExpr)*
    | (LIT_NUM | ID)
    ;

COMMENT 	: '/*' .*? '*/' -> skip ;
LINE_COMMENT: '//' ~[\r\n]* -> skip ;
WS		    : [ \t\r\n]+ -> skip ;
TYPE        : 'entero' | 'real' | 'cadena' | 'booleano' | 'caracter';
LIT_NUM     : [0-9]+([0.9]+)?;
LIT_BUL     : 'verdadero' | 'falso';
LIT_CAD     : '"'.*?'"';
LIT_CHR     : '\''[a-z]'\'';
LITERAL     : LIT_NUM | LIT_BUL | LIT_CAD | LIT_CHR ;
ID          : [a-zA-Z][a-zA-Z0-9_]*;
BIN_OP      : '+' | '-' | '\\' | '*' | '%';
UNA_OP      : '!';
SMCOLON     : ';';