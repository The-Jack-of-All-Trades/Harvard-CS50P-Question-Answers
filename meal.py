camel_case = input("camelCase: ")

snake_case = ""
for letter in camel_case:
    if letter.isupper() == True:
        snake_case = f"{snake_case}_{letter.lower()}"
    else:
        snake_case = f"{snake_case}{letter}"
        pass

print(f"snake_case: {snake_case}")