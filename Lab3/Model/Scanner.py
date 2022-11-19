import re
from Model.SymbolTable import SymbolTable


class Scanner:
    def __init__(self, program, tokens):
        self.program = program
        self.tokens = tokens
        self.symTable = SymbolTable()
        self.pif = []
        self.index = 0
        self.line = 1
        self.faultToken = ""

    def skipSpace(self):
        """
        This function skips the white spaces or the new lines in the program.
        :return: True, if a character was skipped
                 False, if nothing was skipped
        """
        flag = False
        while self.index < len(self.program) and (self.program[self.index] == ' ' or self.program[self.index] == '\n'):
            if self.program[self.index] == '\n':
                self.line = self.line + 1
                flag = True
            self.index = self.index + 1
        return flag

    def skipComment(self):
        """
        This function skips the comments in the program, that begin with "/*", until  it reaches a new line.
        :return: True, if any comments were skipped
                 False, if nothing was skipped
        """
        flag = False
        if self.program.startswith("/*", self.index):
            flag = True
            while self.index < len(self.program) and self.program[self.index] != '\n':
                self.index = self.index + 1
        return flag

    def isStringConstant(self):
        """
        This function checks if the parts of the program are string constants using a regex.
        The regex searches for strings that begin and end  with quotation marks and only contain letters, digits, underscores or spaces.
        If any matches are found, the string is added to the constants symbol table and to the pif and the program continues from the end of the string.
        If the regex has no matches, we check if the quotation marks are used correctly, and if they are, we raise an exception for invalid characters inside the string.
        If the quotation marks are not closed, we raise an exception that string is not closed.
        :return: True, if a match was found
                 False, if no matches were found
        :raise: Exception, if the regex has no matches, and the quotation marks are used correctly
                Exception, if the regex has no matches, but the quotation marks are not used correctly
        """
        strReg = re.findall("^\"([a-zA-z0-9_ ]*)\"", self.program[self.index:])
        if strReg:
            token = strReg[0]
            self.pif.append(["strConst", -2])
            self.symTable.addToStrConstTable("\"" + token + "\"")
            self.index = self.index + len(token) + 2
            print("Found string constant: " + token)
            return True

        strReg = re.findall("^\".*\"$", self.program[self.index:])
        if strReg:
            raise Exception("Lexical error: Invalid characters inside string on line " + str(self.line))

        strReg = re.findall("^\"", self.program[self.index:])
        if strReg:
            raise Exception("Lexical error: String not closed on line " + str(self.line))
        return False

    def isIntConstant(self):
        """
        This function checks if the parts of the program are int constants using a regex.
        The regex searches for integers or for number 0.
        If there are any matches, the integer is added to the int symbol table and to the pif and the program continues from the end of the integer.
        :return: True, if a match was found
                 False, if no matches were found
        """
        intReg = re.findall("^([-]?[1-9]\\d*|0)", self.program[self.index:])
        if self.program[self.index] == '0':
            intReg = ['0']
        if intReg:
            token = intReg[0]
            if len(self.pif) > 0:
                pifLast = self.pif[len(self.pif) - 1][1]
                if (token[0] == '+' or token[0] == '-') and (pifLast == -1 or pifLast == -2):
                    return False
                ex = self.program[self.index + len(token) - 1]
                if not self.tokens.__contains__(ex) and not ex.isdigit():
                    return False
                print("Found int constant: " + token)
            self.pif.append(["intConst", -1])
            self.symTable.addToIntConstTable(token)
            self.index = self.index + len(token)
            return True
        return False

    def tokenFromList(self):
        """
        This function checks if a part of the program starts with an element from the tokens list, and if it does, the program continues from the end of the token.
        :return: True, if the token is in the list
                 False, if the token is not in the tokens list
        """
        for token in self.tokens:
            if self.program.startswith(token, self.index):
                self.pif.append([token, 0])
                self.index = self.index + len(token)
                print("Found token from list: " + token)
                return True
        return False

    def isIdentifier(self):
        """
        This function checks if the parts of the program are identifiers using a regex.
        The regex searches for strings that begin with a letter and contain letters, digits or underscores.
        If there are any matches, the string is added to the pif, together with its position in the symbol table, and the program continues from the end of the string.
        :return: True, if a match was found
                 False, if no matches were found
        """
        idReg = re.findall("^([a-zA-Z_][a-zA-Z0-9_]*)", self.program[self.index:])
        if idReg:
            token = idReg[0]
            print("Found identifier " + token)
            self.symTable.addToIdTable(token)
            self.pif.append(["id", self.symTable.getIdTable().find(token)])
            # if self.symTable.addToIdTable(token):
            #     self.pif.append(["id", self.symTable.getIdTable().find(token)])
            self.index = self.index + len(token)
            return True
        return False

    def nextToken(self):
        """
        This function parses the next token in the program by skipping the white spaces and the comments.
        The function checks if the token is a string constant, int constant, identifier or token, and if it is the case, it is added to the pif.
        If the token is neither of the above, it raises an exception, lexical error having the token and the line it is found
        :return: -
        """
        while True:
            if not self.skipSpace() and not self.skipComment():
                break
        if self.index == len(self.program):
            return
        if self.isStringConstant() or self.isIntConstant() or self.tokenFromList() or self.isIdentifier():
            return
        faultToken = ""
        while self.index < len(self.program) and (not self.program[self.index] == " " and not self.program[
                                                                                                  self.index] == "\n") and not self.tokens.__contains__(
            self.program[self.index] + ""):
            faultToken = faultToken + self.program[self.index]
            self.index = self.index + 1
        self.faultToken = self.faultToken + faultToken
        raise Exception("Lexical error: Cannot classify token " + self.faultToken + " on line " + str(self.line))

    def scanProgram(self):
        """
        This function scans the program (takes the next token)
        :return: -
        """
        while self.index < len(self.program):
            self.nextToken()

    def printToSTFile(self):
        """
        This function prints the symbol table to a file.
        :return: -
        """
        with open('Resources/ST.out', 'w') as f:
            f.write(str(self.symTable))

    def printToPIFFile(self):
        """
        This function prints the pif to a file.
        :return: -
        """
        pif = ""
        for elem in self.pif:
            pif = pif + str(elem[0]) + " -> " + str(elem[1]) + '\n'
        with open('Resources/PIF.out', 'w') as f:
            f.write(pif)
