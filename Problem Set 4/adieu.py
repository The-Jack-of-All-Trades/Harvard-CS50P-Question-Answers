import sys
names = []

def nameprint(names):
    total = 0

    print("\nAdieu, adieu, to", end="")
    for thenames in names:
        total += 1
        if total != len(names):
            print(f" {thenames},", end="")
        elif total == len(names) and len(names) == 1:
            print(f" {thenames}")
        elif total == len(names):
            print(f" and {thenames}", end="")


def ending(names):
    nameprint(names)
    sys.exit()

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break
if __name__ == "__main__":
    ending(names)
