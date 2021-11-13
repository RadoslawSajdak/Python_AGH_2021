## Radosław Sajdak

import json


with open('file.json') as json_file:
    data = json.load(json_file)
print(json.dumps(data, indent = 2))
    
result = int(input("0. Remove 1. Write\n"))

## Removing ##
if( 0 == result):
    element = int(input("Element to remove (0-n):"))
    try:
        data.pop(element)
    except IndexError:
        print("Index out of range!")

    with open('file.json', 'w') as outfile:
        json.dump(data, outfile, indent = 2)

    print(data)
## Adding ##
elif( 1 == result ):
    print("Adding")
    data.append({})
    data[-1]["name"] = input("Name: ")
    data[-1]["surname"] = input("Surname: ")
    data[-1]["age"] = int(input("Age: "))
    data[-1]["student"] = bool(input("Student (True/False): "))
    data[-1]["Skills"] = input("Skills (separated with ','): ").split(',')
    print(data[-1])

    with open('file.json', 'w') as outfile:
        json.dump(data, outfile, indent = 2)
else:
    print("Wrong input!")