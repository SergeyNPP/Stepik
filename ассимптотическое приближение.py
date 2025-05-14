import math

n = int(input())
sm = 0
for i in range(n):
    sm += 1 / (i + 1)
sm -= math.log(n)
print(sm)
