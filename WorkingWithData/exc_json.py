## Radosław Sajdak

import json

FIRST_WRITE = False
if FIRST_WRITE:
    x = {
        "name": "Piotr",
        "surname": "Kalias",
        "age": 21,
        "student": True,
        "skills": ("C++", "Python"),
        "favourites": [
            {"fruit": "Banana"},
            {"color": "Green"}
        ]
    }

    print(json.dumps(x, indent = 4))
    with open('file.json', 'w') as outfile:
        json.dump(x, outfile, indent = 4)
else:
    with open('file.json') as json_file:
       data = json.load(json_file)
    print(json.dumps(data, indent = 2))