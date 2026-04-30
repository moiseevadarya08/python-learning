# Задача 1: Добавление в список
result = []
result.append(5)
result.append(10)
print(result)

# Задача 2: Собрать чётные числа
numbers = [1, 2, 3, 4, 5, 6]
filtered = []
for i in numbers:
    if i % 2 == 0:
        filtered.append(i)
print(filtered)

# Задача 3: Собрать числа больше 5
numbers = [2, 8, 1, 9, 4]
filtered = []
for i in numbers:
    if i > 5:
        filtered.append(i)
print(filtered)
