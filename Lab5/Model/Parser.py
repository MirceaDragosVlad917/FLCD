from Model.Grammar import Grammar


class Parser:
    def __init__(self):
        self.grammar = Grammar("Resources/first_follow.txt")
        self.first = {}
        self.follow = {}
        self.getFirst()
        self.getFollow()
        self.parserTable = {}
        self.numberedProductions = []
        self.number_productions()
        self.generate_parser_table()

    def FirstAlgorithm(self, non_terminal):
        """
        If x is a terminal, then FIRST(x) = { ‘x’ }
        If x-> Є, is a production rule, then add Є to FIRST(x).
        If X->Y1 Y2 Y3….Yn is a production,
            FIRST(X) = FIRST(Y1)
            If FIRST(Y1) contains Є then FIRST(X) = { FIRST(Y1) – Є } U { FIRST(Y2) }
            If FIRST (Yi) contains Є for all i = 1 to n, then add Є to FIRST(X).
        :param non_terminal:
        :return:
        """
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
        """
        1) FOLLOW(S) = { $ }   // where S is the starting Non-Terminal
        2) If A -> pBq is a production, where p, B and q are any grammar symbols,
           then everything in FIRST(q)  except Є is in FOLLOW(B).
        3) If A->pB is a production, then everything in FOLLOW(A) is in FOLLOW(B).
        4) If A->pBq is a production and FIRST(q) contains Є,
           then FOLLOW(B) contains { FIRST(q) – Є } U FOLLOW(A)
        :param non_terminal:
        :return:
        """
        follow = set()
        if non_terminal == self.grammar.startingSymbol:
            follow.add('$')
        for production in self.grammar.getProductionsContainingNonTerminal(non_terminal):
            print(production)
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

    def number_productions(self):
        index = 1
        for production in self.grammar.productions:
            start = production[0]
            rules = production[1]
            for rule in rules:
                self.numberedProductions.append(((start, rule), index))
                index += 1


