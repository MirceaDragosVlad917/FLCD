from Model.Grammar import Grammar


class Parser:
    def __init__(self):
        self.grammar = Grammar("Resources/g1.txt")
        self.first = {}
        self.follow = {}
        self.getFirst()

    def FirstAlgorithm(self, non_terminal):
        first = set()
        if non_terminal in self.grammar.terminals:
            first.add(non_terminal)
            return first
        for production in self.grammar.getProductionsForNonTerminal(non_terminal):
            if production[0] in self.grammar.terminals or production[0] == 'epsilon':
                first.add(production[0])
            else:
                for i in range(len(production)):
                    rule = production[i]
                    if rule in self.grammar.nonTerminals:
                        flag = True
                        for j in range(i):
                            if 'epsilon' not in self.FirstAlgorithm(production[j]):
                                flag = False
                        if flag is True:
                            for elem in self.FirstAlgorithm(rule):
                                first.add(elem)
        return first

    def FollowAlgorithm(self, non_terminal):
        follow = set()
        if non_terminal == self.grammar.startingSymbol:
            follow.add('$')
        for production in self.grammar.getProductionsContainingNonTerminal(non_terminal):
            rule = production[1]
            for i in range(len(rule)):
                term = rule[i]
                if term == non_terminal:
                    if i < (len(rule) - 1):
                        first_next = self.FirstAlgorithm(rule[i + 1])
                        for e in first_next:
                            if e != 'epsilon':
                                follow.add(e)
        return follow

    def getFirst(self):
        for non_term in self.grammar.nonTerminals:
            self.first[non_term] = self.FirstAlgorithm(non_term)

    def printFirst(self):
        for key in self.first.keys():
            print(key, ' : ', self.first[key])
