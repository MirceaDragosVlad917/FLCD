from Model.FA import FA


def menu():
    print("\n")
    print("0. Exit")
    print("1. Print the states")
    print("2. Print the alphabet")
    print("3. Print the initial state")
    print("4. Print the final states")
    print("5. Print the transitions")
    print("6. Check DFA sequence \n")


def run():
    fa = FA("Resources/fa.in")
    fa.readFA()
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
                fa.printStates()
            case 2:
                fa.printAlphabet()
            case 3:
                fa.printInitialState()
            case 4:
                fa.printFinalStates()
            case 5:
                fa.printTransitions()
            case 6:
                string = input("    Please enter a sequence to be checked: ")
                flag = fa.checkDFA(string)
                if flag is False:
                    print("The DFA sequence is not accepted by FA!")
                else:
                    print("The DFA sequence is accepted by FA!")
            case _:
                print("Invalid choice!")


if __name__ == "__main__":
    run()
