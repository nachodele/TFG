%{
#include <stdio.h>
int nc, np, nl;
//comentario de una linea
%}
%option noyywrap

digito [0-9]
letra [a-zA-Z]
%%
{letra}({letra}|{digito})* {printf("token IDENTIFICADOR: %s\n",yytext);}
[-+]?{digito}+  {printf("token ENTERO: %s\n",yytext);}
[-+]?{digito}+(.{digito}+)?((E|e)[-+]?{digito}+)? {printf("token REAL: %s\n",yytext);}
.|\n {/*no hace nada con resto*/}

%%
