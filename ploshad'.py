import math

# n*a*a/(4*tan(pi/n))

n = int(input())  # Натуральное число (Сторон)
a = float(input())  # Действительное число (Длина)
S = (
    n * pow(a, 2) / (4 * math.tan(math.pi / n))
)  #  с длиной стороны a и количеством сторон n
print(S)
