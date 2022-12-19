from Model.Grammar import Grammar


class Parser:
    def __init__(self):
        self.grammar = Grammar("Resources/first_follow.txt")
        self.first = {}
        self.follow = {}
        self.getFirst()
        self.getFollow()
        # self.parserTable = {}
        # self.numberedProductions = []
        # self.number_productions()
        # self.generate_parser_table()

    def FirstAlgorithm(self, non_terminal):
        if non_terminal in self.grammar.terminals:
            return set(non_terminal)
        first = set()
        for production in self.grammar.getProductionsForNonTerminal(non_terminal):
            if production[0] in self.grammar.terminals or production[0] == 'epsilon':
                first.add(production[0])
            else:
                for index in range(len(production)):
                    right = production[index]
                    if right in self.grammar.nonTerminals:
                        flag = True
                        for j in range(index):
                            if 'epsilon' not in self.FirstAlgorithm(production[j]):
                                flag = False
                        if flag is True:
                            for elem in self.FirstAlgorithm(right):
                                first.add(elem)
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
            left = production[0][0]
            right = production[1]
            for i in range(len(right)):
                elem = right[i]
                if elem == non_terminal:
                    if i < (len(right) - 1):
                        firstOfNext = self.FirstAlgorithm(right[i + 1])
                        for e in firstOfNext:
                            if e != 'epsilon':
                                follow.add(e)
                        if 'epsilon' in firstOfNext:
                            for f in self.FollowAlgorithm(left):
                                follow.add(f)
                    else:
                        if left != non_terminal:
                            for f in self.FollowAlgorithm(left):
                                follow.add(f)
        return follow

    def getFollow(self):
        for non_term in self.grammar.nonTerminals:
            self.follow[non_term] = self.FollowAlgorithm(non_term)

    def printFollow(self):
        for elem in self.follow.keys():
            print(elem, ' : ', self.follow[elem])

    