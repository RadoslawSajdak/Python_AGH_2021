## Radoslaw Sajdak

saved_code = 0

while True:
    try:
        saved_code = int(input("Set your code: "))
        print( "Your code is: ", saved_code )
        break

    except ValueError:
        print("You should use digits only!")

while True:
    try:
        temp_code = int(input("Pass your code: "))
        if saved_code == temp_code:
            print( "Code passed properly!" )
            break
        else:
            print( "Wrong password!" )

    except ValueError:
        print("You should use digits only!")