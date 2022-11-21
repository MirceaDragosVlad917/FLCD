class Grammar:
    def __init__(self):
        self.nonTerminals = []
        self.terminals = set()
        self.productions = []
        self.startingSymbol = ""

    def getNonTerminals(self):
        return self.nonTerminals

    def getTerminals(self):
        return self.terminals

    def getProductions(self):
        return self.productions

    def getStartingSymbol(self):
        return self.startingSymbol

    def __str__(self) -> str:
        return "G =( " + str(self.nonTerminals) + ", " + str(self.terminals) + ", " + str(
            self.productions) + ", " + self.startingSymbol + " )"
