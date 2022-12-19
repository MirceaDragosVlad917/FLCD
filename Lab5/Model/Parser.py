from Model.Grammar import Grammar


class Parser:
    def __init__(self):
        self.grammar = Grammar("Resources/first_follow.txt")
        self.first = {}
        self.follow = {}
        self.getFirst()
        self.getFollow()

    def FirstAlgorithm(self, non_terminal):
        if non_terminal in self.grammar.terminals:
            return set(non_terminal)
        first = set()
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
                            for e in self.FirstAlgorithm(rule):
                                first.add(e)
        return first

    def getFirst(self):
        for non_term in self.grammar.nonTerminals:
            self.first[non_term] = self.FirstAlgorithm(non_term)

    def printFirst(self):
        for elem in self.first.keys():
            print(elem, ' : ', self.first[elem])

    def FollowAlgorithm(self, non_terminal):
        follow = set()
        if non_terminal == self.grammar.startingSymbol:
            follow.add('$')
        for production in self.grammar.getProductionsContainingNonTerminal(non_terminal):
            start = production[0][0]
            rule = production[1]
            for i in range(len(rule)):
                term = rule[i]
                if term == non_terminal:
                    if i < (len(rule) - 1):
                        first_next = self.FirstAlgorithm(rule[i + 1])
                        for e in first_next:
                            if e != 'epsilon':
                                follow.add(e)
                        if 'epsilon' in first_next:
                            for f in self.FollowAlgorithm(start):
                                follow.add(f)
                    else:
                        if start != non_terminal:
                            for f in self.FollowAlgorithm(start):
                                follow.add(f)
        return follow

    def getFollow(self):
        for non_term in self.grammar.nonTerminals:
            self.follow[non_term] = self.FollowAlgorithm(non_term)

    def printFollow(self):
        for elem in self.follow.keys():
            print(elem, ' : ', self.follow[elem])


