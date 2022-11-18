from Model.Scanner import Scanner


def main():
    try:
        with open("Resources/p3.in", "r") as f:
            program = ""
            next_line = f.readline().strip('\n')
            while next_line:
                program = program + next_line + '\n'
                next_line = f.readline().strip('\n')
        with open("Resources/token.in") as f:
            tokens = []
            next_line = f.readline().strip('\n')
            while next_line:
                tokens.append(next_line)
                next_line = f.readline().strip('\n')

        scanner = Scanner(program, tokens)
        try:
            scanner.scanProgram()
        except Exception as e:
            print(e)
            scanner.printToSTFile()
            scanner.printToPIFFile()
            return
        scanner.printToSTFile()
        scanner.printToPIFFile()
        print("Lexically correct")
    except FileNotFoundError:
        print("Source file not found")
    except IOError:
        print("Can not write output")


if __name__ == "__main__":
    main()
