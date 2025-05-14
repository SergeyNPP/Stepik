import math

m = int(input())
p = int(input())
n = int(input())

for i in range(n):
    c = m * math.pow((1 + p / 100), i)
    print(i + 1, c)
# range(start, stop, step)
