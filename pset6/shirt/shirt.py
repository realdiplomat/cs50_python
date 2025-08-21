#    2 CL arg: before csv (to read) and after csv (to write)
#    if the user does not specify exactly two command-line arguments,
#    if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
#    if the input’s name does not have the same extension as the output’s name, or
#    if the specified input does not exist.

import sys
from PIL import Image, ImageOps

extension = (".jpg", ".jpeg", ".png")

def main():
    shirt()

def shirt():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    #for python shirt.py before.ext after.ext
    else:
            file_before = sys.argv[1].lower()
            file_after = sys.argv[2].lower()

            beforeName, beforeExt = file_before.split(".")
            afterName, afterExt = file_after.split(".")

            if file_before.endswith(extension) and file_after.endswith(extension):

                if beforeExt != afterExt:
                    sys.exit("Input and output have different extensions")
                else:
                    pass
                
                try:

                    #to open the photo
                    with Image.open(file_before) as muppet, Image.open("shirt.png") as shirt:


                        #get shirt size
                        shirt_size = shirt.size

                        #image size to shirt size
                        muppet_shirt = ImageOps.fit(muppet, shirt_size)

                        #to paste the photo: Image.paste(im: Image, box: Image)
                        muppet_shirt.paste(shirt, shirt)

                        #to save
                        muppet_shirt.save(file_after)

                except FileNotFoundError:
                    sys.exit("Input does not exist")
            else:
                sys.exit("Invalid input")

if __name__ == "__main__":
    main()
