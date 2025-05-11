import math  # импортирую модуль math

# На вход программе подаются три действительных числа a≠0,b,c каждое на отдельной строке.
a = float(input())
b = float(input())
c = float(input())
if a == 0:  # проверка условия на неравеноство
    print("Нет корней")
else:
    D = math.pow(b, 2) - 4 * a * c  # Вычисление дискриминанта
    if D < 0:
        print("Нет корней")
    elif D == 0:
        x = (-b) / 2 / a  # Вычисление одиночного корня
        print(x)
    else:
        # Вычисление корней
        x1 = ((-b) - math.sqrt(D)) / 2 / a
        x2 = ((-b) + math.sqrt(D)) / 2 / a
        # Упорядочевание корней в порядке возрастания
        if x1 > x2:
            max = x1
            min = x2
        else:
            max = x2
            min = x1
        print(min, max, sep="\n")
