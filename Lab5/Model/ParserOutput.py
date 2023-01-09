import sys


class Node:
    def __init__(self, father, sibling, right_side, index, value):
        self.father = father
        self.sibling = sibling
        self.right_side = right_side
        self.value = value
        self.index = index


class ParserOutput:
    def __init__(self, parser, sequence, output_file=""):
        self.root = None
        self.parser = parser
        self.node_number = 1
        self.node_list = []
        self.output = output_file
        self.productions = parser.sequenceAnalyzer(sequence)
        self.generateParsingTree()

    def generateParsingTree(self):
        node_stack = []
        prod_index = 0

        node = Node(0, 0, False, self.node_number, self.parser.grammar.startingSymbol)
        self.node_number += 1
        node_stack.append(node)
        self.node_list.append(node)
        self.root = node
        while len(node_stack) > 0 and prod_index < len(self.productions):
            top_of_node_stack = node_stack[len(node_stack) - 1]
            if top_of_node_stack.value in self.parser.grammar.terminals or 'epsilon' in top_of_node_stack.value:
                while len(node_stack) > 0 and node_stack[len(node_stack) - 1].right_side is False:
                    node_stack.pop()
                if len(node_stack) > 0:
                    node_stack.pop()
                else:
                    break
                continue

            production = self.productions[prod_index][0]
            self.node_number += len(production) - 1
            for i in range(len(production) - 1, -1, -1):
                if i == 0:
                    sibling = 0
                else:
                    sibling = self.node_number - 1
                child = Node(top_of_node_stack.index, sibling, i != len(production) - 1, self.node_number, production[i])
                self.node_number -= 1
                node_stack.append(child)
                self.node_list.append(child)

            self.node_number += len(production) + 1
            prod_index += 1

    def printParsingTree(self):
        try:
            sorted_nodes = sorted(self.node_list, key=lambda x: x.index)
            for node in sorted_nodes:
                print("Node(" + str(node.index) + "," + node.value + "," + str(node.father) + "," + str(
                    node.sibling) + ")")
        except Exception as e:
            print(e)

    def printParsingTreeToFile(self):
        try:
            original_stdout = sys.stdout
            with open(self.output, 'w') as f:
                sys.stdout = f
                sorted_nodes = sorted(self.node_list, key=lambda x: x.index)
                for node in sorted_nodes:
                    print("Node(" + str(node.index) + "," + node.value + "," + str(node.father) + "," + str(
                        node.sibling) + ")")
                sys.stdout = original_stdout
        except Exception as e:
            print(e)
