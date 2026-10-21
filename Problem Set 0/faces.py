def main():
    phrase = input().replace(":)", "🙂").replace(":(", "🙁") # Replaces strings with strings
    convert(phrase)

# Prints the users input
def convert(phrase):
    print(phrase)

main()
