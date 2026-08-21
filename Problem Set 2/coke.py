total = 50
while True:
    print(f"Amount Due: {total}")
    money = int(input("Insert Coin: "))
    if money in (25, 10, 5):
        total = total - money
        if total <= 0:
            print(f"Change Owed: {abs(total)}")
            break
    else:
        pass
