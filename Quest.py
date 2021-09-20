
import random
import time
def main():
    inv = []
    while True:
        hp = 100
        choice1 = input("Для того что бы их выбрать, напишите, куда хотите пойти\n(Прямо, налево, направо)\n")
        if choice1.lower() == "Прямо".lower():
            hp-=random.randint(1, 20)
            if "Факел" not in inv:
                print("Зайдя в дверь, вы провалились под пол, и попали на нижний уровень")
                print("Оглядевшись, вы замечаете зажжённый факел, брать ли его? (y/n)")
                while True:
                    choice2up = input('')
                    if choice2up == "y":
                        inv.append("Факел")
                        print("Вы получили факел!")
                        print("Ваш инвентарь:", inv)
                        break
                    if choice2up == 'n':
                        print("Вы решили не брать факел, однако из-за темноты в коридоре")
                        print("вы не заметили ловушку. Вас хорошо приложило бревном")
                        hp-=random.randint(1, 30)
                        print("Ваше здоровье:", hp)
                        break
            else:
                print("Вы тут уже были")

        elif choice1.lower() == "Налево".lower():
            print("Повернув налево, вы вышли к коридорам")
            print ("Оглядевшись, вы увидели две двери")
            while True:
                choice2l = input("Куда вы хотите пойти(направо, налево, назад): ")
                if choice2l.lower() == "Налево".lower():
                    if "Факел" in inv:
                        if "Ключ" not in inv:
                            inv.append("Ключ")
                            print("Похоже, это какой то ключ")
                            print("Ваш инвентарь:", inv)
                        else:
                            print("Вы уже здесь были")
                    else:
                        print("Слишком темно, без факела там делать нечего")

                elif choice2l.lower() == "Назад".lower():
                    print("Вы возвратились назад")
                    break

                elif choice2l.lower() == "Направо".lower():
                    if "Ключ" in inv:
                        print("Наконец-то свобода!")
                        print("Вы прошли квест!")
                        time.sleep(5)
                        inv.remove
                        return None
                    else:
                        print("Закрыто")
                else:
                    print("Такого хода тут нету")

        elif choice1.lower() == "Направо".lower():
            print("Повернув направо, вы угодили в ловушку, что моментально убила вас")
            hp-=hp
            print("Ваше здоровье", hp)
            print("Игра окончена")
            time.sleep(5)
            break
        else:
            print("Похоже, такого хода нету...")
main()