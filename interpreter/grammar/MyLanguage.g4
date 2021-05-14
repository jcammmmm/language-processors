grammar MyLanguage;		

commands	: command commands
			| EOF
			| // epsilon
			;

// commands	: command* ;

command 	: conditional
			| repeat
			| printexpr 
			| VAR ID 'as' expr SMCOLON
			;
/*
hay pragmas que permiten la generacion de metodos individuales por cada camino, a cambio de quitar el
camino pardre ... :
command 	: conditional       # miCondicional
			| repeat            # miRepeat
			| printexpr         # miPrintExpr
			| VAR ID 'as' expr SMCOLON
			;
*/

/**
 * Quemar la palabra no la agrega al contexto del codigo generado. Si quiero que
 * este debe estar como token e.g. ELSE
 */
conditional : 'if' expr ROP expr 'then' commands 'endif';
repeat		: 'repeat' expr 'times' commands 'endrepeat';
printexpr	: 'print' expr SMCOLON ;

expr:	expr MULOP expr
    |	expr SUMOP expr
    |	DOUBLE
    |	PIZQ expr PDER
    | 	ID
    ;

// .*? quiere decir un skip voraz se salta todo hasta encontrar
// el simbolo de la derecha ...
COMMENT 		: '/*' .*? '*/' -> skip ;
LINE_COMMENT 	: '//' ~[\r\n]* -> skip ;
WS		: [ \t\r\n]+ -> skip ;
VAR		: 'var';
PIZQ	: '(' ;
PDER	: ')' ;
ROP		: ( '<' | '<=' | '>=' | '>' | '==' | '!=' ) ;
SMCOLON : ';' ;
MULOP	: ( '*' | '/' );
SUMOP	: ('+' | '-') ;
DOUBLE	: [0-9]+( | [.][0-9]+);
ID 		: [a-zA-Z][a-zA-Z0-9_]* ;

