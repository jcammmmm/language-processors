grammar PsiCoder;

program
    : (definition)* 'funcion_principal' block 'fin_principal' (definition)*;

definition
    : function
    | structure
    ;

function
    : 'funcion' type ID '(' (type ID) (',' type ID)* ')'
            'hacer' (block | return)
      'fin_funcion'
    ;

return
    : 'retornar' (expression | ID)? ';'
    ;
    
structure
    : 'estructura' ID (declaration)* 'fin_estructura'
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
    | return
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
    : type (assignment | ID) (',' (assignment | ID))* SMCOLON
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

type
    : ID | 'entero' | 'real' | 'cadena' | 'booleano' | 'caracter'
    ;


COMMENT 	: '/*' .*? '*/' -> skip ;
LINE_COMMENT: '//' ~[\r\n]* -> skip ;
WS		    : [ \t\r\n]+ -> skip ;
LIT_NUM     : [0-9]+(.[0-9]+)?;
LIT_BUL     : 'verdadero' | 'falso';
LIT_CAD     : '"'[ a-zA-Z0-9_-]*'"';
LIT_CHR     : '\''[a-z]'\'';
ID          : [a-zA-Z][a-zA-Z0-9_]*;
BIN_OP      : '+' | '-' | '/' | '*' | '%' | '||' | '&&' |
              '<' | '<=' | '==' | '!=' | '=>' | '>' ;
UNA_OP      : '!';
SMCOLON     : ';';