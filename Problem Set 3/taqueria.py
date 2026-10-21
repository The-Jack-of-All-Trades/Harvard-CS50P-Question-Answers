menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        item = input("Item: ").lower().title() # Sets the users input to lowercase then only capitalizes the first letter

        if item in menu: # If the item is in the dictionary "menu" from line 1, then get the value of that item, convert it to a float, add it to the price, then print the total to 2 decimal places
            price = menu.get(item)
            price = float(price)
            total += price
            print(f"Total: ${total:.2f}")
    except EOFError: # Once the user has pressed ctrl-d, then prompting the user will stop and the program will end
        break
