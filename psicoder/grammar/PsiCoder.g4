grammar PsiCoder;

program
    : (definition)* principal (definition)*;

principal
    : FUN_PPAL bloque END_PPAL
    ;

definition
    : funcion
    | estructura
    ;

funcion
    : 'funcion' tipo ID ('()' | '(' (tipo ID) (',' tipo ID)* ')')
            'hacer' bloque
      'fin_funcion'
    ;

retornar
    : 'retornar' (expresion | variable)? ';'
    ;
    
estructura
    : 'estructura' ID (declaracion)* 'fin_estructura'
    ;

bloque
    : (proposicion)*
    ;

proposicion
    : declaracion
    | asignacion ';'
    | imprimir
    | leer
    | funLlamado ';'
    | si
    | para
    | mientras
    | hacerMientras
    | seleccionar
    | retornar
    | romper
    ;

si
    : 'si' '(' expresion ')' 'entonces' bloque siEntonces
    ;

siEntonces
    : 'fin_si'
    | 'si_no' bloque 'fin_si'
    ;

para
    : 'para' '('
        inicio ';'
        expresion ';'
        (valor | expresion) ')'
            'hacer' bloque 'fin_para'
    ;

inicio
    : tipo ID '=' valor
    | ID '=' valor
    ;

mientras
    : 'mientras' '(' expresion ')' 'hacer' bloque 'fin_mientras'
    ;

hacerMientras
    : 'hacer' bloque 'mientras' '(' expresion ')' ';'
    ;

seleccionar
    : 'seleccionar' '(' ID ')' 'entre' ((caso)+ | defecto) 'fin_seleccionar'
    ;

caso
    : 'caso' literal ':' (proposicion)*
    | defecto
    ;

defecto
    : 'defecto' ':' (proposicion)*
    ;

imprimir
    : 'imprimir' '(' valor (',' valor)* ')' ';'
    ;

leer
    : 'leer' '(' variable ')' ';'
    ;

declaracion
    : tipo (inicializacion | ID) (',' (inicializacion | ID))* SMCOLON
    ;

inicializacion
    : variable '=' valor
    ;

asignacion
    : variable '=' valor
    ;

valor
    : (variable | literal | expresion | funLlamado)
    ;

expresion
    : (literal | variable) BIN_OP expresion
    | '(' expresion ')' (BIN_OP expresion)*
    | (literal | variable)
    ;

variable
    : ID ('.' ID)*
    ;

funLlamado
    : ID '()'
    | ID '(' valor (',' valor)* ')'
    ;

romper
    : 'romper;'
    ;

literal
    : (LIT_BUL | LIT_CAD | LIT_NUM | LIT_CHR)
    ;

tipo
    : ID | 'entero' | 'real' | 'cadena' | 'booleano' | 'caracter'
    ;

FUN_PPAL    : 'funcion_principal';
END_PPAL    : 'fin_principal';


COMMENT 	: '/*' .*? '*/' -> skip ;
LINE_COMMENT: '//' ~[\r\n]* -> skip ;
WS		    : [ \t\r\n]+ -> skip ;
LIT_NUM     : [0-9]+(.[0-9]+)?;
LIT_BUL     : 'verdadero' {setText("True");} | 'falso' {setText("False");};
LIT_CAD     : '"'[ a-zA-Z0-9_-]*'"';
LIT_CHR     : '\''[a-z]'\'';
ID          : [a-zA-Z][a-zA-Z0-9_]*;
BIN_OP      : '+' | '-' | '/' | '*' | '%' | '||' | '&&' |
              '<' | '<=' | '==' | '!=' | '=>' | '>' ;
UNA_OP      : '!';
SMCOLON     : ';';

