def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        pass
    else:
        return False

    if s[0].isalpha() and s[1].isalpha():
        pass
    elif s[0].isdigit() or s[1].isdigit():
        return False

    for symbol in s:
        if symbol.isdigit() == False and symbol.isalpha() == False:
            return False

    for symbol in s:
        if symbol.isdigit() and symbol != "0":
            break
        elif symbol == "0":
            return False

    number_started = False

    for symbol in s:
        if symbol.isdigit():
            number_started = True
        if number_started == True and symbol.isalpha():
            return False

    
    return True


main()
