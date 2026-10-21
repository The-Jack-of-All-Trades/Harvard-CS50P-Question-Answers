grocery_dict = {} # A blank dictionary
while True:
    try:
        item = input().lower() # The lowercase of the users input
        if item in grocery_dict: # If the item already exists in "grocery_dict" then add another one of it to the value
            grocery_dict[item] += 1 
        else: # If the item does not exist in "grocery_dict" then it creates a key value pair of key = "item" and value = 1
            grocery_dict[item] = 1 
    except EOFError: # Once the user presses ctrl-d, then the loop will break
        break
alpha_grocery = dict(sorted(grocery_dict.items())) # Makes the items a key and value pari, then sorts the items by first letter, then converts the sorted items into another dictionary
for groceryitem in alpha_grocery: # Prints the value of the item first, then the item in uppercase after
    print(f"{alpha_grocery.get(groceryitem)} {groceryitem.upper()}")
