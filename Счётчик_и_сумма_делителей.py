# На вход программе подаются два натуральных числа a и b (a< b). Напишите программу, которая находит натуральное число из отрезка
# [a;b] (от a до b включительно) с максимальной суммой делителей.
# Если чисел с максимальной суммой делителей несколько, то искомым числом является наибольшее из них.
# Ваша программа должна выводить ответ в следующем формате:
# <число с максимальной суммой делителей> <сумма делителей этого числа>
a = int(input())
b = int(input())
max_sum = -1
# count = 0
for i in range(a, b + 1):
    sum = 0
    if (
        i % 2 == 0 or i % 3 == 0
    ):  # Проверка условия на натуралльность, чтобы откинуть ненужные расчеты
        for j in range(1, b + 1):
            if i % j == 0:
                #    count += 1 # Счетчик делителей
                sum += j
        if max_sum <= sum:
            max_sum = sum
            max_i = i
#        count = 0
print(max_i, max_sum)
# 716352
