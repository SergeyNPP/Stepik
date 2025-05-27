# Численный треугольник 2
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21

n = int(input())
count = 0
for i in range(1, n + 1):
    for j in range(i):
        count += 1
        print(count, end=" ")
    print()

# Численный треугольник 3
# 1
# 121
# 12321
# 1234321
# 123454321

n = int(input())
for j in range(1, n + 1):
    k = n - (n - j)
    for i in range(1, k + 1):
        print(i, end="")
    if k == i:
        for i in range(k - 1, 0, -1):
            print(i, end="")
    print()
