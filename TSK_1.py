from optparse import check_choice
from os import system
import random
import time

def CheckNumbers(param, total):
    while True:
        try:
            number = int(input(f"{param} "))
            if number > 0 and number <= total: return number
            else: print("Число введено неправильно.")
        except:
                print("Число введено неправильно.")

def CheckVariant(param, array):
    print(f"{param}\n")
    for i in array: print(i)
    while True:
        try:
            answer = int(input("\n"))
            if answer == 1 or answer == 2 or answer == 3: break
            else:
                print("Выберите вариант от 1 до 3.")
                continue
        except:
            print("Выберите вариант от 1 до 3.")
    if answer == 3:
        answer = random.randint(1, 2)
        print(f'\nВыбран вариант "{array[answer - 1]}".')
    return answer

def CheckDifficulty(param, array):
    print(f"{param}\n")
    for i in array: print(i)
    while True:
        try:
            answer = int(input("\n"))
            if answer == 1 or answer == 2 or answer == 3: return answer
            else:
                print("Выберите вариант от 1 до 3.")
                continue
        except:
            print("Выберите вариант от 1 до 3.")

def PvP(param):
    total = 100
    while True:
        print(f"На столе осталось {total} конфет.")
        if total >= 28:
            if param == 1:
                sweetsChoice = CheckNumbers("Ход первого игрока. Можно взять от 1 до 28 конфет:", 28)
                param = 2
            else:
                sweetsChoice = CheckNumbers("Ход второго игрока. Можно взять от 1 до 28 конфет:", 28)
                param = 1
        else:
            if param == 1:
                sweetsChoice = CheckNumbers(f"Ход первого игрока. Можно взять от 1 до {total} конфет:", total)
                param = 2
            else:
                sweetsChoice = CheckNumbers(f"Ход второго игрока. Можно взять от 1 до {total} конфет:", total)
                param = 1
        total -= sweetsChoice
        if total == 0:
            print("На столе пусто, однако...")
            if param == 1: print("\nПоздравляем игрока 2 с победой!")
            else: print("\nПоздравляем игрока 1 с победой!")
            break

def PvE(param1, param2):
    interception = True
    total = 100
    while True:
        print(f"На столе осталось {total} конфет.")
        if total > 28:
            if param1 == 1:
                sweetsChoice = CheckNumbers("Ваш ход. Можно взять от 1 до 28 конфет:", 28)
                param1 = 2
            else:
                print("Ход компьютера:", end = " ")
                if param2 == 1:    
                    time.sleep(2)
                    sweetsChoice = random.randint(1, 28)
                elif param2 == 2:
                    time.sleep(1)
                    if total == 100: sweetsChoice = 13
                    elif interception:
                        if total > 87:
                            chooseVariants = (random.randint(1, 13 - sweetsChoice), 13 - sweetsChoice)
                            sweetsChoice = random.choice(chooseVariants)
                        elif total < 87 and total > 71:
                            chooseVariants = (random.randint(1, 42 - sweetsChoice), 42 - sweetsChoice)
                            sweetsChoice = random.choice(chooseVariants)
                        interception = False
                    else:
                        chooseVariants = (random.randint(1, 29 - sweetsChoice), 29 - sweetsChoice)
                        sweetsChoice = random.choice(chooseVariants)
                else:
                    if total % 29 == 0:
                        sweetsChoice = random.randint(1, 28)
                        interception = False
                    elif interception:
                        if total == 100: sweetsChoice = 13
                        elif total > 87: sweetsChoice = 13 - sweetsChoice
                        elif total < 87 and total > 71: sweetsChoice = 42 - sweetsChoice
                        interception = False
                    else: sweetsChoice = 29 - sweetsChoice
                print(f"{sweetsChoice} конфет.")
                param1 = 1
        else:
            if param1 == 1:
                sweetsChoice = CheckNumbers(f"Ваш ход. Можно взять от 1 до {total} конфет:", total)
                param1 = 2
            else:
                print("Ход компьютера:", end = " ")
                if param2 == 1:    
                    time.sleep(2)
                    sweetsChoice = random.randint(1, total)
                elif param2 == 2:
                    time.sleep(1)
                    chooseVariants = (random.randint(1, total), total)
                    sweetsChoice = random.choice(chooseVariants)
                else: sweetsChoice = total
                print(f"{sweetsChoice} конфет.")
                param1 = 1
        total -= sweetsChoice
        if total == 0:
            print("\nНа столе пусто, однако...")
            if param1 == 2: print("\nПоздравляем Вас с победой!")
            else: print("\nЧто ж, в этот раз не повезло... Но, ничего, обязательно повезёт в следующий!")
            break

system('clear')
variants = ["1. Игра со вторым игроком", "2. Игра с компьютером", "3. Случайный выбор"]
move = ["1. Ваш ход", "2. Ход соперника", "3. Случайный выбор"]
difficulty = ["1. Легкий", "2. Средний", "3. Сложный"]
print('''Привет! Добро пожаловать на игру "Вытяни конфету"!

На столе лежит 100 конфет. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.\n''')

answer1 = CheckVariant('Чтобы начать игру, пожалуйста, напиши номер варианта игры из списка ниже:', variants)
if answer1 == 1:
    answer2 = CheckVariant('\nОтлично! Пожалуйста, напиши номер, кто будет ходить первым:', move)
    system('clear')
    time.sleep(0.5)
    print("Что ж, поехали! :)")
    PvP(answer2)
else:
    level = CheckDifficulty('\nЧто ж, давайте поиграем с компьютером. Но давайте выберем уровень сложности:', difficulty)
    answer2 = CheckVariant('\nОтлично! Пожалуйста, напиши номер, кто будет ходить первым:', move)
    system('clear')
    time.sleep(0.5)
    print("Что ж, поехали! :)")
    PvE(answer2, level)