def main():
    expression = input("Expression: ")

    expression_list = expression.split(" ")

    x = int(expression_list[0])
    y = expression_list[1]
    z = int(expression_list[2])

    if y == "+":
        answer = x + z
        print(f"{answer:.1f}")
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
