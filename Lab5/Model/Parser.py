from Model.Grammar import Grammar


class Parser:
    def __init__(self):
        self.grammar = Grammar("Resources/first_follow.txt")
        self.first = {}
        self.follow = {}
        self.getFirst()
        self.getFollow()
        self.parsingTable = {}
        self.numberedProductions = []
        self.indexProductions()
        self.generateParsingTable()

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
            left = production[0][0]
            right = production[1]
            for index in range(len(right)):
                elem = right[index]
                if elem == non_terminal:
                    if index < (len(right) - 1):
                        firstOfNext = self.FirstAlgorithm(right[index + 1])
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

    def indexProductions(self):
        """
        This function indexes the productions and adds them to a list
        :return: -
        """
        index = 1
        for production in self.grammar.productions:
            left = production[0]
            right = production[1]
            for elem in right:
                self.numberedProductions.append(((left, elem), index))
                index += 1

    def generateParsingTable(self):
        """
        This function generates the parsing table following the rules:
        -if an element from the set of terminals is epsilon, we will insert "acc" on the table at the key corresponding to that element and pop otherwise
        :return:
        """
        for k in self.grammar.terminals:
            if k == 'epsilon':
                result = 'acc'
            else:
                result = 'pop'
            self.parsingTable[(k, k)] = result
        # print(self.numberedProductions)
        for production in self.numberedProductions:
            prod = production[0]
            # print(prod[0][0])
            index = production[1]
            print(self.getConcatenatedFirst(prod[1]))
            for elem in self.getConcatenatedFirst(prod[1]):
                if isinstance(elem, list):
                    elem = tuple(elem)
                if (prod[0][0], elem) in self.parsingTable.keys():
                    print("Conflict! M(" + prod[0][0] + "," + elem + ")")
                if elem != 'epsilon':
                    self.parsingTable[(prod[0][0], elem)] = (prod[1], index)

            if 'epsilon' in self.getConcatenatedFirst(prod[1]):
                for element in self.FollowAlgorithm(prod[0][0]):
                    if isinstance(element, list):
                        element = tuple(element)
                    if (prod[0][0], element) in self.parsingTable.keys():
                        print("Conflict! M(" + prod[0][0] + "," + elem + ")")
                    self.parsingTable[(prod[0][0], element)] = (prod[1], index)

    def sequenceAnalyzer(self, sequence):
        input_stack = []
        working_stack = []
        output = []
        input_stack.append("$")
        sequence = sequence.split(" ")

        for elem in reversed(sequence):
            input_stack.append(elem)

        working_stack.append("$")
        working_stack.append(self.grammar.startingSymbol)

        while input_stack[len(input_stack) - 1] != "$" or working_stack[len(working_stack) - 1] != "$":
            topInputStack = input_stack[len(input_stack) - 1]
            topWorkingStack = working_stack[len(working_stack) - 1]
            if (topWorkingStack, topInputStack) in self.parsingTable.keys():
                value = self.parsingTable[(topWorkingStack, topInputStack)]
                if isinstance(value, tuple) is False and value == "pop":
                    input_stack.pop()
                    working_stack.pop()
                    continue
                else:
                    working_stack.pop()
                    if value[0] != ['epsilon']:
                        production = value[0]
                        for prod in reversed(production):
                            working_stack.append(prod)
                output.append(self.parsingTable[(topWorkingStack, topInputStack)])
            else:
                print("Error for " + topInputStack + " , " + topWorkingStack)
                return output
        return output

    def getConcatenatedFirst(self, target_list):
        concatenated_first = set()
        index = 0
        flag = True
        while flag:
            element = target_list[index]
            if element in self.grammar.terminals:
                concatenated_first.add(element)
                break
            firstList = self.first[element]
            for elem in firstList:
                concatenated_first.add(elem)
            if 'epsilon' not in firstList:
                flag = False
            index += 1
        return concatenated_first

    def printParsingTable(self):
        for key in self.parsingTable.keys():
            if self.parsingTable[key] == 'pop' or self.parsingTable[key] == 'acc':
                print("M( " + key[0] + " , " + key[1] + " ) = " + self.parsingTable[key])
            else:
                print("M( " + key[0] + " , " + key[1] + " ) = " + ' '.join(self.parsingTable[key][0]) + "," + str(
                    self.parsingTable[key][1]))
