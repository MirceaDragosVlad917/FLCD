
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton interface for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     ID = 258,
     CONST = 259,
     BOOL = 260,
     CHAR = 261,
     INT = 262,
     ARRAY = 263,
     NUMBER = 264,
     OF = 265,
     FLOAT = 266,
     PLUS = 267,
     MINUS = 268,
     EQUALS = 269,
     MUL = 270,
     DIV = 271,
     ASSIGN = 272,
     LESS = 273,
     GREATER = 274,
     LESS_OR_EQUAL = 275,
     GREATER_OR_EQUAL = 276,
     NOT_EQUAL = 277,
     NOT = 278,
     AND = 279,
     OR = 280,
     MOD = 281,
     CURLY_BRACKET_OPEN = 282,
     CURLY_BRACKET_CLOS = 283,
     SQUARE_BRACKET_OPEN = 284,
     SQUARE_BRACKET_CLOSE = 285,
     CLOSED_PARENTHESIS = 286,
     OPENED_PARENTHESIS = 287,
     SEMI_COLON = 288,
     ENUMERATION_SIGN = 289,
     COMMA = 290,
     FOR = 291,
     IN = 292,
     RANGE = 293,
     IF = 294,
     ELSE = 295,
     DO = 296,
     READ = 297,
     PRINT = 298,
     THEN = 299,
     WHILE = 300
   };
#endif
/* Tokens.  */
#define ID 258
#define CONST 259
#define BOOL 260
#define CHAR 261
#define INT 262
#define ARRAY 263
#define NUMBER 264
#define OF 265
#define FLOAT 266
#define PLUS 267
#define MINUS 268
#define EQUALS 269
#define MUL 270
#define DIV 271
#define ASSIGN 272
#define LESS 273
#define GREATER 274
#define LESS_OR_EQUAL 275
#define GREATER_OR_EQUAL 276
#define NOT_EQUAL 277
#define NOT 278
#define AND 279
#define OR 280
#define MOD 281
#define CURLY_BRACKET_OPEN 282
#define CURLY_BRACKET_CLOS 283
#define SQUARE_BRACKET_OPEN 284
#define SQUARE_BRACKET_CLOSE 285
#define CLOSED_PARENTHESIS 286
#define OPENED_PARENTHESIS 287
#define SEMI_COLON 288
#define ENUMERATION_SIGN 289
#define COMMA 290
#define FOR 291
#define IN 292
#define RANGE 293
#define IF 294
#define ELSE 295
#define DO 296
#define READ 297
#define PRINT 298
#define THEN 299
#define WHILE 300




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;


