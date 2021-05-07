grammar ArrayInit;

init    : '{' value (',' value)* '}' ;
value   : init
        | INT
        ;
// una recomendacion es que los tokens mas generales queden abajo ... ;)
INT     : [0-9]+ ;
WS      : [ \t\r\n]+ -> skip ;