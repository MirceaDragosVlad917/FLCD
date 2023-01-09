%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1
%}

%token FOR
%token IN
%token ARRAY
%token CHAR
%token CONST
%token RANGE
%token IF
%token ELSE
%token DO
%token READ
%token THEN
%token WHILE
%token PRINT
%left '+' '-' '*' '/'
%token PLUS
%token MINUS
%token DIV
%token MOD
%token MUL
%token OPEN_CURLY_BRACKET
%token CLOSED_CURLY_BRACKET
%token OPEN_ROUND_BRACKET
%token CLOSED_ROUND_BRACKET
%token OPEN_RIGHT_BRACKET
%token CLOSED_RIGHT_BRACKET
%token COMMA
%token SEMI_COLON
%token COLON
%token DOLLAR
%token APOSTROPHE
