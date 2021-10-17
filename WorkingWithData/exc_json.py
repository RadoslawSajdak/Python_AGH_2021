## Radosław Sajdak

import json

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