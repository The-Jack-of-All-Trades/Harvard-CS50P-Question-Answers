import tabulate
import sys
import csv

def main():
    if len(sys.argv) > 2: # Checks if there is more than two command line arguments
        print("Too many command-line arguments")
        sys.exit()

    if len(sys.argv) < 2: # Checks if there is less than two command line arguments
        print("Too few command-line arguments")
        sys.exit()

    if not sys.argv[1].endswith(".csv"): # Checks if the second command line argument does not end in ".csv"
        print("Not a CSV file")
        sys.exit()

    program = sys.argv[1]

    try:
        menu = []
        with open(program) as file: # Opens the second command line argument and reads over it 

            reader = csv.reader(file)

            for line in reader: # Adds a smaller list to the list called "menu"
                menu.append(line)

            header = menu[0] # Assigns the first list in "menu" as a variable called "header"

            table = menu[1:] # Assigns all of the other lists after the first list as a variable called "table"

            print(tabulate.tabulate(table, header, tablefmt="grid")) # Uses the "tabuate" function in the module "tabulate" to print a grid format with the headers being at the very top

    except FileNotFoundError:
        print("File does not exist")
        sys.exit()

if __name__ == "__main__":
    main()
