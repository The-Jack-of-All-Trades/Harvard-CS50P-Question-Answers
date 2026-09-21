def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2:
        return False
    elif len(s) > 6:
        return False

    if not s[0:2].isalpha():
        return False

    for symbol in s:
        if symbol.isalpha() or symbol.isdigit():
            continue
        else:
            return False

    is_number = False
    for symbol in s:
        if symbol == "0" and is_number == False:
            return False
        if symbol.isdigit():
            is_number = True
        if is_number == True and symbol.isalpha():
            return False

    else:
        return True
    
        

if __name__ == "__main__":
    main()
