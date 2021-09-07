while True:
    ex = input("нажмите Y, для продолжения, а для выхода любую кнопку: ")
    if ex.lower() == "y":
        print('Программа  "Калькулятор"')
    else:
        break
    onenumber = int(input("Введите первое число: "))
    twonumber = int(input("Введите второе число: "))
    znak = input("Введите один из знаков: +; -; *; /; ")
    if znak == "+":
        print(onenumber + twonumber)
    else:
        if znak == "-":
            print(onenumber - twonumber)
        else:
            if znak == "*":
                print(onenumber * twonumber)
            else:
                if znak == "/":
                    print(onenumber / twonumber)
                else:
                    print("Неизвестная операция")