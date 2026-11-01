import csv
import sys

if len(sys.argv) > 3: # Check if there is more than 3 command line arguments
    print("Too many command-line arguments")
    sys.exit()

if len(sys.argv) < 3: # Check if there is less than 3 command line arguments
    print("Too few command-line arguments")
    sys.exit()

if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"): # Checks if the second command line argument and the first are both ".csv" files
    print("Command-line arguments must end in .csv")
    sys.exit()

try:
    after = []
 
    with open(sys.argv[1]) as file: # Opens the second command line argument
        reader = csv.DictReader(file) # Makes a reader containing all of the data as key value pairs based off of the first line in "sys.argv[1]"
   
        for row in reader: # Loops over each dictionary and adds the value into the after list so it becomes a list of dictionaries while also stripping off whitespace from the splitted name
            last, first = row['name'].split(",")
            after.append({'first': first.strip(), 'last': last.strip(), 'house': row['house']})
     
    with open(sys.argv[2], "w") as file: # Opens the third command line argument in write mode
        fieldnames = ['first','last','house']
        writer = csv.DictWriter(file, fieldnames=fieldnames) # Uses "DictWriter" and set the top key rows in a list called "fieldnames"

        writer.writeheader() # Writes the "fieldnames to the first line of the csv file"
   
    for dict in after: # Loops over the "after" list and writes the dictionaries on the csv file
        writer.writerow({'first': dict['first'],'last': dict['last'],'house': dict['house']})
   
except FileNotFoundError:
    print(f"Could not read {sys.argv[1]}")
    sys.exit()
