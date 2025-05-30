a = int(input())
b = int(input())
for i in range(a, b + 1):
    count = 0
    if i == 1:
        continue
    for j in range(2, b + 1):
        if i % j == 0:
            count += 1
    if count < 2:
        print(i)


a, b = int(input()), int(input())

if a == 1:
    a += 1
for num in range(a, b + 1):
    for d in range(2, num):
        if num % d == 0:
            break
    else:
        print(num)