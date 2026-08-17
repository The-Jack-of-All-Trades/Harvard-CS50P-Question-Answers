x_str, operator, y_str = input("Expression: ").strip().split()


x = int(x_str)
y = int(y_str)


if operator == "+":
    result = x + y
elif operator == "-":
    result = x - y
elif operator == "*":
    result = x * y
elif operator == "/":
    result = x / y

print(f"{result:.1f}")
