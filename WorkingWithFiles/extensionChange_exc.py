## Radosław Sajdak

import os
filename = input("file to convert: ")

base = os.path.splitext(filename)[0]
os.rename(filename, base + ".png")
