def main():
    expression = input("Expression: ")

    expression_list = expression.split(" ") # Splits the input expression at the blank spaces

    x = int(expression_list[0]) # Sets x to the integer of the first number in the input
    y = expression_list[1] # Sets z to the arithemetic operator in the middle ("+", "-", "/", "*")
    z = int(expression_list[2]) # Sets x to the integer of the second number in the input

    if y == "+":
        answer = x + z
        print(f"{answer:.1f}") # The :.1f will round the answer to 1 decimal place
    elif y == "-":
        answer = x - z
        print(f"{answer:.1f}")
    elif y == "*":
        answer = x * z
        print(f"{answer:.1f}")
    elif y == "/":
        answer = x / z
        print(f"{answer:.1f}")


main()
