import math


def is_perfect_square(n):
    # Функция проверяет, является ли число полным квадратом
    return math.isqrt(n) ** 2 == n


def count_quadratic_numbers(limit):
    count = 0
    max_k = int(math.sqrt(limit))  # Максимальное значение k для проверки

    # Перебираем все возможные k
    for k in range(1, max_k + 1):
        k_square = k**2

        # Проверяем все возможные m
        for m in range(1, k + 1):
            m_square = m**2

            # Проверяем оба возможных случая
            if k_square - m_square > 0 and k_square - m_square <= limit:
                count += 1
            if k_square + m_square <= limit:
                count += 1

    return count


# Выводим результат
limit = 16 * 10**12
print(f"Количество квадратичных чисел до {limit}: {count_quadratic_numbers(limit)}")
