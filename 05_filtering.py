# Задача 1: Числа больше 5 и чётные
numbers = [2, 7, 10, 15, 18, 21]
filtered = []
for i in numbers:
    if i > 5 and i % 2 == 0:
        filtered.append(i)
print(filtered)

# Задача 2: Найти максимум после фильтрации
numbers = [4, 9, 12, 3, 18, 7]
filtered = []
for i in numbers:
    if i > 5:
        filtered.append(i)
print(max(filtered))

# Задача 3: Найти минимум после фильтрации
numbers = [5, 14, 2, 19, 8, 30]
filtered = []
for i in numbers:
    if i > 5 and i % 2 == 0:
        filtered.append(i)
print(min(filtered))
