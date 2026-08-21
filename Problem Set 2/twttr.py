phrase = input("Input: ")

output = ""
for letter in phrase:
    if letter.lower() in ("a", "e", "i", "o", "u"):
        pass
    else:
        output = f"{output}{letter}"

print(f"Output: {output}")
