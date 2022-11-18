class FA:
    def __init__(self, file_name):
        self.file_name = file_name
        self.states = []
        self.alphabet = []
        self.initial_state = []
        self.final_states = []
        self.transitions = []
        self.readFA()

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

    def readFA(self):
        """
        This function reads the finite automata from a file, line by line, transforming the lines into lists of strings
        In the file, on the first line we have the states, on the second one the alphabet, on the third one the initial state, on the 4th one the final states, and from line 6 to the end of the file, the transitions
        :return: -
        """
        f = open(self.file_name, "r")
        content = f.readlines()
        index = 0
        for line in content:
            if index == 0:
                self.states = self.readFromFile(line)
            if index == 1:
                self.alphabet = self.readFromFile(line)
            if index == 2:
                self.initial_state = line.replace(" ", "").strip().split("=")[-1]
            if index == 3:
                self.final_states = self.readFromFile(line)
            index = index + 1

        index = 5
        while index < len(content):
            line = content[index].strip().replace(" ", "").split("->")

            first = line[0]
            tokens = first[1:-1].split(",")

            second = line[1]
            res = second[1:-1].split(",")

            self.transitions.append((tokens[0], tokens[1], res))
            index = index + 1

    def printStates(self):
        print("The states are: " + str(self.states))

    def printAlphabet(self):
        print("The alphabet is: " + str(self.alphabet))

    def printInitialState(self):
        print("The initial state is: " + str(self.initial_state))

    def printFinalStates(self):
        print("The final states are: " + str(self.final_states))

    def printTransitions(self):
        print("The transitions are: " + str(self.transitions))

    def getNextState(self, init_state, tran):
        """
        This function returns the next state of the finite automata
        :param init_state: string, representing the initial state
        :param tran: string, representing the transition
        :return: string, representing the next state
        """
        for elem in self.transitions:
            if elem[0] == init_state:
                if elem[1] == tran:
                    return elem[2]
        return None

    def checkDFA(self, string):
        """
        This function checks if a DFA sequence is accepted by the finite automata
        :param string: string, the sequence to be checked
        :return: True, if the sequence is accepted by the finite automata
                 False, if the sequence is not accepted by the finite automata
        """
        init_state = self.initial_state
        for elem in string:
            state = self.getNextState(init_state, elem)
            if state is None:
                return False
            if len(state) != 1:
                return False
            init_state = state[0]
        if init_state in self.final_states:
            return True
        return False
