import sys

if len(sys.argv) > 2: # Checks to see if the number of command line arguments is greater than two
    print("Too many command-line arguments")
    sys.exit()

if len(sys.argv) < 2: # Checks to see if the number of command line arguments is less than two
    print("Too few command-line arguments")
    sys.exit()

if not sys.argv[1].endswith(".py"): # Checks to see if the second command line argument ends with ".py"
    print("Not a Python file")
    sys.exit()

program = sys.argv[1]

try:
    with open(program) as file: # Opens the second command line arugment file in "r" or "read mode"
        total = 0
     
        for line in file: # Loops over ever line of the file, adding to the total variable as long the line is not just a comment or is just whitespace
         
            if line.lstrip().startswith("#"):
                continue
           
            if line.isspace() or line == "":
                continue
           
            total += 1

    print(total)
 
except FileNotFoundError:
    print("File does not exist")
    sys.exit()
