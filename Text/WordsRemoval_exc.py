## Radoslaw Sajdak
filename = input("File to read: ")
words = input("Words to delete (space separated): ").split()

file = open(filename, "r")
text = file.read()
file.close()

file = open(filename, "w")
for w in words:
    print( w )
    text = text.replace(w, "")

file.write(text)
file.close()