from Model.Grammar import Grammar


class Parser:
    def __init__(self):
        self.grammar = Grammar("Resources/g1.txt")
        self.first = []
        self.follow = []

    def getFirst(self, non_terminal):
        first = set()
        if non_terminal in self.grammar.terminals:
            first.add(non_terminal)
            return first
        for production in self.grammar.productionsForNonTerminal(non_terminal):
            if production[0] in self.grammar.terminals or production[0] == 'epsilon':
                first.add(production[0])
            else:
                for i in range(len(production)):
                    rule = production[i]
                    if rule in self.grammar.nonTerminals:
                        flag = True
                        for j in range(i):
                            if 'epsilon' not in self.getFirst(production[j]):
                                flag = False
                        if flag is True:
                            for elem in self.getFirst(rule):
                                first.add(elem)
        return first


