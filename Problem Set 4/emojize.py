from emoji import emojize

words = emojize(input("Input: "), language='alias') # "language='alias'" is an argument in the imported function emojize, which tells it to accept shorted alias names
print(f"Output: {words}")
