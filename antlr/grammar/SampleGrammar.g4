// este nombre debe conincidir con el nombre del archivo ...
grammar SampleGrammar;

// * cero o muchos
// forma backus-naur
inicio : 'hola' ID(',' ID)*;
// + uno o muchos
ID : [a-zA-Z0-9_-]+ ;
// skip ignora
ESP : [ \t\r\n]+ -> skip ;