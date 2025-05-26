# 12 месяцев
# Решите уравнение в натуральных числах

# 28*n + 30*k + 31*m = 356
for n in range(1, 14):
    for k in range(1, 13):
        for m in range(1, 13):
            if 28 * n + 30 * k + 31 * m == 365:
                print(n)
                print(k)
                print(m)
                print()
