while True:
    ex = input("Press y to continue: ")
    if ex.lower() == "y":
        print('Welcome')
    else:
        break
    try:
        onenumber = int(input("Enter the first number: "))
    except ValueError:
        print("You must enter a number!")
        continue
    try:
        twonumber = int(input("Enter the second number: "))
    except ValueError:
        print("You must enter a number!")
        continue
    znak = input("+; -; *; /; Select arithmetic operation: ")
    if znak == "+":
        print(onenumber + twonumber)
    elif znak == "-":
        print(onenumber - twonumber)
    elif znak == "/":
        try:
            print(onenumber / twonumber)
        except ZeroDivisionError:
            print("Cannot be divided by zero")
            continue
    elif znak == "*":
        print(onenumber * twonumber)
    elif znak == "**":
        print(onenumber ** twonumber)
    else:
        print("Unknown arithmetic operation")
