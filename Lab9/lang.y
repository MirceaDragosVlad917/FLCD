%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1
int yydebug = 0;
%}

%token ID
%token CONSTVAR
%token NEW_LINE
%token TYPE
%token INTEGER
%token INT
%token BOOL
%token STRING
%left '+' '-' '*' '//'
%token PLUS
%token MINUS
%token EQUALS
%token MUL
%token DIV
%token ASSIGN
%token LESS
%token GREATER
%token LESS_OR_EQUAL
%token GREATER_OR_EQUAL
%token NOT_EQUAL
%token NOT
%token AND
%token OR
%token MOD
%token CURLY_BRACKET_OPEN
%token CURLY_BRACKET_CLOSE
%token SQUARE_BRACKET_OPEN
%token SQUARE_BRACKET_CLOSE
%token CLOSED_PARENTHESIS
%token OPENED_PARENTHESIS
%token SEMI_COLON
%token ENUMERATION_SIGN
%token COMMA
%token FOR
%token IN
%token RANGE
%token IF
%token ELSE
%token DO
%token READ
%token PRINT
%token THEN
%token WHILE

%start program

%%

program : decllist SEMI_COLON cmpdstmt;
decllist : declaration | declaration SEMI_COLON decllist;
declaration : type ID
type : INT | BOOL | STRING
cmpdstmt : OPENED_PARENTHESIS stmtlist CLOSED_PARENTHESIS;
stmtlist : stmt | stmt SEMI_COLON stmtlist;
stmt : simplstmt | structstmt;
simplstmt : assignstmt | instmt | outstmt;
assignstmt : ID ASSIGN expression;
expression : expression PLUS term | expression MINUS term | term;
term : term MUL factor | term DIV factor | factor;
factor : OPENED_PARENTHESIS expression CLOSED_PARENTHESIS | ID | CONSTVAR;
instmt : READ OPENED_PARENTHESIS ID CLOSED_PARENTHESIS;
outstmt : PRINT OPENED_PARENTHESIS ID CLOSED_PARENTHESIS;
structstmt : cmpdstmt | ifstmt | whilestmt;
ifstmt : IF OPENED_PARENTHESIS condition CLOSED_PARENTHESIS ENUMERATION_SIGN stmt ELSE stmt;
whilestmt : WHILE OPENED_PARENTHESIS condition CLOSED_PARENTHESIS ENUMERATION_SIGN stmt;
condition : expression RELATION expression;
RELATION : LESS | LESS_OR_EQUAL | EQUALS | NOT_EQUAL | GREATER_OR_EQUAL | GREATER;

%%

yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
  if(!yyparse()) fprintf(stderr, "\tNo errors!\n");
}