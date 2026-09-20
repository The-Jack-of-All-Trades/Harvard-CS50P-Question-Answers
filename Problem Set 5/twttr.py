def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")


def shorten(word):
    output = ""
    for letter in word:
        if letter.lower() in ("a", "e", "i", "o", "u"):
            pass
        else:
            output = f"{output}{letter}"
    return output


if __name__ == "__main__":
    main()
