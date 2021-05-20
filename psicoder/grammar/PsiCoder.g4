grammar PsiCoder;

program
    : definition? 'funcion_principal' block 'fin_principal' definition?;

definition
    : function definition
    | structure definition
    ;

function
    : 'funcion'
    ;
    
structure
    : 'estructura'
    ;

block
    : (statement)*
    ;

statement
    : declaration
    | assignment ';'
    | print
    | read
    | funCall ';'
    | if
    | for
    | while
    | doWhile
    | switch
    ;

if
    : 'si' '(' expression ')' 'entonces' block ifThen
    ;

ifThen
    : 'fin_si'
    | 'si_no' block 'fin_si'
    ;

for
    : 'para' '('
        (declaration | assignment ';')
        expression ';'
        (value | expression) ')'
            'hacer' block 'fin_para'
    ;

while
    : 'mientras' '(' expression ')' 'hacer' block 'fin_mientras'
    ;

doWhile
    : 'hacer' block 'mientras' '(' expression ')' ';'
    ;

switch
    : 'seleccionar' '(' ID ')' 'entre' ((case)+ | default) 'fin_seleccionar'
    ;

case
    : 'caso' literal ':' (statement)* 'romper;'?
    | default
    ;

default
    : 'defecto' ':' (statement)* 'romper;'?
    ;

print
    : 'imprimir' '(' value (',' value)* ')' ';'
    ;

read
    : 'leer' '(' ID ')' ';'
    ;

declaration
    : TYPE (assignment | ID) (',' (assignment | ID))* SMCOLON
    ;

assignment
    : ID '=' value
    ;

value
    : (ID | literal | expression | funCall)
    ;

expression
    : (literal | ID) BIN_OP expression
    | '(' expression ')' (BIN_OP expression)*
    | (literal | ID)
    ;

funCall
    : ID '()'
    | ID '(' value (',' value)* ')'
    ;

literal
    : (LIT_BUL | LIT_CAD | LIT_NUM | LIT_CHR)
    ;


COMMENT 	: '/*' .*? '*/' -> skip ;
LINE_COMMENT: '//' ~[\r\n]* -> skip ;
WS		    : [ \t\r\n]+ -> skip ;
TYPE        : 'entero' | 'real' | 'cadena' | 'booleano' | 'caracter';
LIT_NUM     : [0-9]+(.[0-9]+)?;
LIT_BUL     : 'verdadero' | 'falso';
LIT_CAD     : '"'[ a-zA-Z0-9_-]*'"';
LIT_CHR     : '\''[a-z]'\'';
ID          : [a-zA-Z][a-zA-Z0-9_]*;
BIN_OP      : '+' | '-' | '/' | '*' | '%' | '||' | '&&' |
              '<' | '<=' | '==' | '!=' | '=>' | '>' ;
UNA_OP      : '!';
SMCOLON     : ';';