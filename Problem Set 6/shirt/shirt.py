import sys
from PIL import Image, ImageOps
import os

def main():
    if len(sys.argv) > 3: # Checks if there is more than three command line arguments
        sys.exit("Too many command-line arguments")

    if len(sys.argv) < 3: # Checks if there is less than three command line arguments
        sys.exit("Too few command-line arguments")

    root1, extension1 = os.path.splitext(sys.argv[1].lower()) # Uses "os.path.splitext()" to split the second command line argument at the "dot" part (like ".png" or ".jpg") into two different strings, the only one we care about is the extention "extension1"
    root2, extension2 = os.path.splitext(sys.argv[2].lower()) # Uses "os.path.splitext()" to split the third command line argument at the "dot" part (like ".png" or ".jpg") into two different strings, the only one we care about is the extension "extension2"

    if not extension1 in (".jpeg", ".png", ".jpg") or not extension2 in (".jpeg", ".png", ".jpg"): # Checks if the extension of the second and third command line arguments are one of these extensions
        sys.exit("Invalid input")

    if not extension1 == extension2: # Checks if the extensions of the second and third command line arguments are equal
        sys.exit("Input and output have different extensions")

    try:

        image1 = Image.open(sys.argv[1]) # Opens the second command line argument image as "image1"

        shirt = Image.open("shirt.png").convert("RGBA") # Opens the shirt png image as "shirt" and converts it to "RGBA" so that parts of it can be see through

        shirtsize = shirt.size # Stores the size of the "shirt" image as "shirtsize" which is a tuple of "(width, height)"

        imagecrop = ImageOps.fit(image1, shirtsize) # Crops "image1" to be the size of "shirt" using the tuple "shirtsize" and stores it as "imagecrop"

        imagecrop.paste(shirt, (0,0), mask=shirt) # Pastes the "shirt" image over "imagecrop" with a mask of "shirt" to preserve it's transparency

        imagecrop.save(sys.argv[2]) # Saves "imagecrop" with the newly added "shirt" pasted over it, and names the newly created image as the third command line argument
    
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
