grocery_dict = {}
while True:
    try:
        item = input().lower()
        if item in grocery_dict:
            grocery_dict[item] += 1
        else:
            grocery_dict[item] = 1
    except EOFError:
        break
alpha_grocery = dict(sorted(grocery_dict.items()))
for groceryitem in alpha_grocery:
    print(f"{alpha_grocery.get(groceryitem)} {groceryitem.upper()}")
