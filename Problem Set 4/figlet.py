import sys
import pyfiglet
import random

def invalid_usage():
    print("Invalid Usage")
    sys.exit()

command = sys.argv[1:]
if len(command) != 0 and len(command) != 2:
    invalid_usage()

if len(command) == 2:
    font = command[0]
    method = command[1]
    if font != "-f" and font != "--font":
        invalid_usage()
elif len(command) == 0:
    pass

phrase = input("Input: ").strip()

if len(command) == 2:
    words = pyfiglet.figlet_format(f"{phrase}", font=f"{method}")
elif len(command) == 0:
    all_fonts = pyfiglet.FigletFont.getFonts()
    random_font = random.choice(all_fonts)
    words = pyfiglet.figlet_format(f"{phrase}", font=f"{random_font}")

print(words)
