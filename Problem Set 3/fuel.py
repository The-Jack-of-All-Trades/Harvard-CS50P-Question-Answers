while True: 
    try:
        fraction = input("Fraction: ").split("/") # This will forever ask the user (due to the while True loop) until the user inputs correct values
        x = int(fraction[0]) # This is the first value in the list from the ".split()" method
        y = int(fraction[1]) # This is the second value in the list from the ".split()" method

        if x < 0 or y < 0:
            raise ValueError # This will cause the program to immediately jump to line 26 with the except block to catch (raise) the error

        if x > y:
            raise ValueError # This will cause the program to immediately jump to line 26 with the except block to catch (raise) the error
        
        total = round((x / y) * 100) # "round()" will round it to the nearest integer because there is no second argument

        if 0 <= total < 1:
            print("E")
            break
        elif 100 >= total > 99:
            print("F")
            break
        elif total > 100:
            raise ValueError
        else:
            print(f"{total:.0f}%") # :.0f will round to the nearest whole number (integer)
            break
    except (ValueError, ZeroDivisionError): # Corresponds with the "try" block, it will catch errors and continue back to the top of the program to input the user
        continue
