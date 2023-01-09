from Model.Grammar import Grammar
from Model.Parser import Parser
from Model.ParserOutput import ParserOutput


def menu():
    print("\n")
    print("0. Exit")
    print("1. Print the non-terminals")
    print("2. Print the terminals")
    print("3. Print the productions")
    print("4. Print the productions for a given non-terminal")
    print("5. Check CFG")
    print("6. Print First")
    print("7. Print Follow")
    print("8. Print the parsing table")
    print("9. Print parsing tree to screen and file")

def run():
    try:
        grammar = Grammar("Resources/first_follow.txt")
        parser = Parser()
        parserOutput = ParserOutput(parser, "id + id", "Resources/parser_output.txt")
        grammar.readGrammar()
        while 1:
            menu()
            try:
                option = int(input("What is your choice? -> "))
            except ValueError as ve:
                option = 100
            match option:
                case 0:
                    return
                case 1:
                    grammar.printNonTerminals()
                case 2:
                    grammar.printTerminals()
                case 3:
                    grammar.printProductions()
                case 4:
                    non_terminal = input("Please enter the non-terminal: ")
                    grammar.productionsForNonTerminal(non_terminal)
                case 5:
                    print(grammar.checkCFG())
                case 6:
                    parser.printFirst()
                case 7:
                    parser.printFollow()
                case 8:
                    parser.printParsingTable()
                case 9:
                    parserOutput.printParsingTree()
                    parserOutput.printParsingTreeToFile()
                case _:
                    print("Invalid choice!")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    run()
