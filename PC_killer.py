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
