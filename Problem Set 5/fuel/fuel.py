def main():
    while True:
        try:
            fraction = input("Fraction: ").split("/")
            percentage = convert(fraction)
            answer = gauge(percentage)
            print(answer)
            break

        except ValueError:
            continue
        except ZeroDivisionError:
            continue

def convert(fraction):
    x = int(fraction[0])
    y = int(fraction[1])

    if x < 0 or y < 0:
        raise ValueError

    if x > y:
        raise ValueError

    percentage = round((x / y) * 100)

    return percentage

def gauge(percentage):
    if 0 <= percentage < 1:
        return "E"
    
    elif 100 >= percentage > 99:
        return "F"
    
    elif percentage > 100:
        raise ValueError
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
