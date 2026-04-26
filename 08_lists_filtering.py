# Задача 1: Создать новый список из чисел больше 10
numbers = [3, 12, 5, 18, 7, 20]
result = []
for i in numbers:
     if i > 10:
         result.append(i)
print(result)

# Задача 2: Создать новый список из чётных чисел
numbers = [2, 7, 10, 15, 18, 21]
result = []
for i in numbers:
    if i % 2 == 0:
        result.append(i)
print(result)

# Задача 4: Создать новый список из чисел больше 5 и чётных
numbers = [2, 11, 8, 15, 20, 3]
result = []
for i in numbers:
    if i > 5 and i % 2 == 0:
         result.append(i)
print(result)

# Задача 5: Фильтрация + сумма + корректировка результата
numbers = [5, 12, 7, 18, 3, 20, 11, 8, 16]
filtered = []
total = 0
for i in numbers:
    if i > 6 and i % 2 == 0:
        filtered.append(i)
        total += i
if total > 40:
     max_value = max(filtered)
     total -= max_value
print(total)

# Задача 6: Поиск первого числа больше 10 и чётного
numbers = [8, 3, 15, 6, 14, 2, 11, 20, 5]
result = None
for i in numbers:
    if i > 10 and i % 2 == 0:
        result = i
        break
print(result)
