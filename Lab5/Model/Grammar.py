class Grammar:
    def __init__(self, file_name):
        self.file_name = file_name
        self.nonTerminals = set()
        self.terminals = set()
        self.productions = []
        self.startingSymbol = ""
        self.readGrammar()

    def getNonTerminals(self):
        return self.nonTerminals

    def getTerminals(self):
        return self.terminals

    def getProductions(self):
        return self.productions

    def getStartingSymbol(self):
        return self.startingSymbol

    def readFromFile(self, line):
        """
        This function transforms the line that is read from file into a list of strings
        :param line: string, the line read from file
        :return: the line as a list of elements
        """
        line = line.split()
        line = line[-1]
        line = line[1:-1].split(",")
        return line

    def readGrammar(self):
        """
        This function reads the grammar from a file, line by line, transforming the lines into lists of strings
        In the file, on the first line we have the non-terminals, on the second one the terminals, on the third one the starting symbol, and from line 4 to the end of the file, the productions
        :return: -
        """
        file = open(self.file_name, 'r')
        content = file.readlines()
        index = 0
        for line in content:
            if index == 0:
                self.nonTerminals = self.readFromFile(line)
            if index == 1:
                self.terminals = self.readFromFile(line)
            if index == 2:
                startingSymbol = line.replace(" ", "").strip().split("=")[-1]
                if startingSymbol not in self.nonTerminals:
                    raise Exception("The starting symbol is not in the list of non-terminals!")
                self.startingSymbol = startingSymbol
            index = index + 1
        index = 4
        while index < len(content):
            line = content[index].strip().split("->")
            left = line[0].strip().split(" ")
            for elem in left:
                if elem not in self.nonTerminals and elem not in self.terminals:
                    raise Exception(elem + " is not in the list of non-terminals or terminals!")
            productions = line[1].split("|")
            right = []
            for elem in productions:
                elem = elem.strip().split(" ")
                right.append(elem)
            for element in right:
                for elem in element:
                    if elem not in self.nonTerminals and elem not in self.terminals:
                        raise Exception(elem + " is not in the list of non-terminals or terminals!")
            production = (left, right)
            if production in self.productions:
                return
            self.productions.append(production)
            index = index + 1

    def productionsForNonTerminal(self):
        """
        This function prints the productions for a given non-terminal that is read from keyboard
        In case the string read from keyboard is not in the list of non-terminals, a message is displayed on the screen
        :return:
        """
        non_terminal = input("Please enter the non-terminal: ")
        if non_terminal not in self.nonTerminals:
            print("The non-terminal is not in the list of non terminals!")
            return
        for elem in self.productions:
            if ' '.join(elem[0]) == non_terminal:
                print("Productions for the given non-terminal: " + str(elem[1]))
                return
        print("There are no productions for the given non-terminal!")

    def checkCFG(self):
        """
        This function checks if the grammar is context free
        :return: string, a corresponding message
        """
        for elem in self.productions:
            if len(elem[0]) > 1:
                message = "The grammar is not a context free grammar!"
                return message
        message = "The grammar is a context free grammar!"
        return message

    def printNonTerminals(self):
        print("The non-terminals are: " + str(self.nonTerminals))

    def printTerminals(self):
        print("The terminals are: " + str(self.terminals))

    def printProductions(self):
        print("The productions are: " + str(self.productions))

    def __str__(self) -> str:
        return "G =( " + str(self.nonTerminals) + ", " + str(self.terminals) + ", " + str(
            self.productions) + ", " + self.startingSymbol + " )"
