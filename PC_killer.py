# Цифровым корнем числа n называется число, получающееся следующим образом: вычисляется сумма цифр числа n,
# затем сумма цифр у получившегося числа и так далее, пока не получится однозначное число. Например, цифровой корень числа
# 9875 равен 2:
# 9+8+7+5=29
# 2+9=11
# 1+1=2

n = int(input())
a = 0
flag = True
while flag:
    a = 0
    while n > 0:
        a += n % 10
        n = n // 10
    if n == 0:
        n = a
        if a < 10:
            flag = False
print(a)
