## Radosław Sajdak

import os
indent = " " * 3

for subdir, dir, file in os.walk( os.getcwd() ):
    dir_lvl = subdir.replace( os.getcwd(), "").count(os.sep)
    print("{}{}/".format( indent*dir_lvl, os.path.basename(subdir) ))
    for f in file:
        print("{}{}{}".format( indent * (dir_lvl + 1),"|", f ))