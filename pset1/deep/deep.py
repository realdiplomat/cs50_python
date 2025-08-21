x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

if x in "42" or x in "forty-two" or x in "forty two" or x in "Forty Two" :
    print("Yes")
else:
    print("No")
