from Model.Grammar import Grammar


def menu():
    print("\n")
    print("0. Exit")
    print("1. Print the non-terminals")
    print("2. Print the terminals")
    print("3. Print the productions")
    print("4. Print the productions for a given non-terminal")
    print("5. Check CFG \n")

def run():
    try:
        grammar = Grammar("Resources/g2.txt")
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
                    grammar.productionsForNonTerminal()
                case 5:
                    print(grammar.checkCFG())
                case _:
                    print("Invalid choice!")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    run()
