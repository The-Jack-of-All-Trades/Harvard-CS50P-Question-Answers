import sys
names = []

def nameprint(names):
    total = 0

    print("\nAdieu, adieu, to", end="") # This will cause the print to not create a new line (end=\n) leading to the name to be places after "to"
    for thenames in names: # For however many names the user input, run the loop that many times
        total += 1
        if total != len(names): # If the total is not equal to the last name in the list, print the name with a comma after it
            print(f" {thenames},", end="")
        elif total == len(names) and len(names) == 1: # If the total is the last name of the list, and the only name in the list, print the name
            print(f" {thenames}")
        elif total == len(names): # If the total is equal to the last name of the list, then print "and" before the name, this runs after line 12 so that it can check line 12 that there is only one of the name in the list
            print(f" and {thenames}", end="") 


def ending(names):
    nameprint(names)
    sys.exit() # Instantly terminate/end the program

while True:
    try:
        name = input("Name: ") 
        names.append(name) # Add the user input to the list from line 2
    except EOFError: # Once the user presses ctrl-d, then the program will break out of the "while True" loop
        break
        
if __name__ == "__main__": # Only run this code if you are running the file directly, not importing it into another file
    ending(names)
