
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
     CONSTVAR = 259,
     NEW_LINE = 260,
     TYPE = 261,
     INTEGER = 262,
     INT = 263,
     BOOL = 264,
     STRING = 265,
     PLUS = 266,
     MINUS = 267,
     EQUALS = 268,
     MUL = 269,
     DIV = 270,
     ASSIGN = 271,
     LESS = 272,
     GREATER = 273,
     LESS_OR_EQUAL = 274,
     GREATER_OR_EQUAL = 275,
     NOT_EQUAL = 276,
     NOT = 277,
     AND = 278,
     OR = 279,
     MOD = 280,
     CURLY_BRACKET_OPEN = 281,
     CURLY_BRACKET_CLOSE = 282,
     SQUARE_BRACKET_OPEN = 283,
     SQUARE_BRACKET_CLOSE = 284,
     CLOSED_PARENTHESIS = 285,
     OPENED_PARENTHESIS = 286,
     SEMI_COLON = 287,
     ENUMERATION_SIGN = 288,
     COMMA = 289,
     FOR = 290,
     IN = 291,
     RANGE = 292,
     IF = 293,
     ELSE = 294,
     DO = 295,
     READ = 296,
     PRINT = 297,
     THEN = 298,
     WHILE = 299
   };
#endif
/* Tokens.  */
#define ID 258
#define CONSTVAR 259
#define NEW_LINE 260
#define TYPE 261
#define INTEGER 262
#define INT 263
#define BOOL 264
#define STRING 265
#define PLUS 266
#define MINUS 267
#define EQUALS 268
#define MUL 269
#define DIV 270
#define ASSIGN 271
#define LESS 272
#define GREATER 273
#define LESS_OR_EQUAL 274
#define GREATER_OR_EQUAL 275
#define NOT_EQUAL 276
#define NOT 277
#define AND 278
#define OR 279
#define MOD 280
#define CURLY_BRACKET_OPEN 281
#define CURLY_BRACKET_CLOSE 282
#define SQUARE_BRACKET_OPEN 283
#define SQUARE_BRACKET_CLOSE 284
#define CLOSED_PARENTHESIS 285
#define OPENED_PARENTHESIS 286
#define SEMI_COLON 287
#define ENUMERATION_SIGN 288
#define COMMA 289
#define FOR 290
#define IN 291
#define RANGE 292
#define IF 293
#define ELSE 294
#define DO 295
#define READ 296
#define PRINT 297
#define THEN 298
#define WHILE 299




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;


