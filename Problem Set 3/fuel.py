while True:
    try:
        fraction = input("Fraction: ").split("/")
        x = int(fraction[0])
        y = int(fraction[1])

        if x < 0 or y < 0:
            raise ValueError

        if x > y:
            raise ValueError
        
        total = round((x / y) * 100)

        if 0 <= total < 1:
            print("E")
            break
        elif 100 >= total > 99:
            print("F")
            break
        elif total > 100:
            raise ValueError
        else:
            print(f"{total:.0f}%")
            break
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
