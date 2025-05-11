import math

a = float(input())
b = float(input())
c = float(input())
if a == 0:
    print("Нет корней")
else:
    D = math.pow(b, 2) - 4 * a * c
    if D < 0:
        print("Нет корней")
    elif D == 0:
        x = (-b) / 2 / a
        print(x)
    else:
        x1 = ((-b) - math.sqrt(D)) / 2 / a
        x2 = ((-b) + math.sqrt(D)) / 2 / a
        if x1 > x2:
            max = x1
            min = x2
        else:
            max = x2
            min = x1
        print(min, max, sep="\n")
