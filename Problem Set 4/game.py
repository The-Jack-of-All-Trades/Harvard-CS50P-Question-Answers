from random import randint

def levels():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                continue
            else:
                break
        except ValueError:
            continue

    secret_number = randint(0, level)

    return secret_number

def guess(secret_number):
    while True:
        try:
            userguess = int(input("Guess: "))
            if userguess < 0:
                continue
            else:
                if userguess == secret_number:
                    print("Just Right!")
                    return
                elif userguess > secret_number:
                    print("Too Large!")
                    continue
                elif userguess < secret_number:
                    print("Too Small!")
                    continue
        except ValueError:
            continue

def main():
    secret_number = levels()
    guess(secret_number)

main()
