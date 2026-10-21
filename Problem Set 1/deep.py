answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower() # Converts this to lowercase if it is convertable into lowercase (like a letter)

if answer in ("42", "forty-two", "forty two"):
    print("Yes")
else:
    print("No")
