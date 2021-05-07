// este nombre debe conincidir con el nombre del archivo ...
grammar SampleGrammar_draft;

// * cero o muchos
// forma backus-naur
// esta forma 'inline' de especificar el codigo Java no se prefiere por obvias
// razones ... Aquí surge la necesidad de los listeners
inicio : {System.out.println("Entrando...");} 'hola' ID(',' ID)* {System.out.println("Saliendo...");};
// + uno o muchos
ID : [a-zA-Z0-9_-]+ ;
// skip ignora
ESP : [ \t\r\n]+ -> skip ;