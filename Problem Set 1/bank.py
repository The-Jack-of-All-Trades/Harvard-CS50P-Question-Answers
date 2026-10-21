def main():
    greeting = input("Greeting: ").strip().lower() # The users input will be in lowercase and have no whitespace

    if greeting.startswith("hello"): # This is before .startswith("h") so that the program can check for hello before it checks for it just starting with "h"
        print("$0")

    elif greeting.startswith("h") and greeting != "hello": # Makes sure the value is not hello but also starts with "h"
        print("$20")

    else:
        print("$100")


main()
