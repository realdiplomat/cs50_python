import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

#list_of_all_fonts
fonts = figlet.getFonts()




# either no arg or 2 arg i.e figlet.py -f/--font <font name>
# if no arg then select random font

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fonts))
elif len(sys.argv) == 3 and sys.argv[1] in ["-f","--font"] and sys.argv[2] in fonts:
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

Input = input("Input: ")
print(figlet.renderText(Input))
