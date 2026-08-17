import emoji

emoji_input = input("Input: ").strip()

def output(emoji_input):
    output = emoji.emojize(emoji_input, language= "alias")
    print(output)


output(emoji_input)