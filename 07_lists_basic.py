# Задача 1: Подсчет чисел больше 5
numbers = [4, 7, 2, 9, 12, 3]
count = 0
for i in numbers:
    if i > 5:
        count += 1 
print(count)

# Задача 2: Сумма чисел, которые больше 10
numbers = [10, 4, 8, 15, 2, 20]
total = 0
for i in numbers:
    if i > 10:
        total += i
print(total)

# Задача 3: Найти самое большое число
numbers = [5, 12, 7, 18, 3, 20]
max_number = numbers [0]
for i in numbers:
    if i > max_number:
        max_number = i
print(max_number)

# Задача 4: Найти минимальное число 
numbers = [5, 12, 7, 18, 3, 20]
min_number = numbers [0]
for i in numbers:
    if i < min_number:
        min_number = i
print(min_number)

# Задача 5: Посчитать количество чётных чисел
numbers = [3, 10, 15, 2, 8, 20]
count = 0
for i in numbers:
    if i % 2 == 0:
        count += 1
print(count)

# Задача 6: Посчитать сумму чётных чисел
numbers = [1, 5, 8, 12, 3, 7]
total = 0
for i in numbers:
    if i % 2 == 0:
         total += i
print(total)

# Задача 7: Посчитать сумму чисел, которые больше 5 и чётные
numbers = [4, 9, 2, 7, 10, 15]
total = 0
for i in numbers:
    if i > 5 and i % 2 == 0:
        total += i
print(total)
