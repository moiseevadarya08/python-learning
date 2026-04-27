# Задача 1: Найти максиммальное из чисел больше 5 и чётных
numbers = [4, 12, 7, 18, 9, 24, 3, 16, 11]
filtered = []
for i in numbers:
    if i > 5 and i % 2 == 0:
        filtered.append(i)
max_value = max(filtered)
print(max_value)

# Задача 2: Найти разницу между максиммальным и минимальным значениями 
numbers = [3, 22, 7, 18, 5, 26, 9, 12]
filtered = []
for i in numbers:
    if i > 10 and i % 2 == 0:
        filtered.append(i)
max_value = max(filtered)
min_value = min(filtered)
difference  = max(filtered) - min(filtered)
print(difference)

# Задача 3: Найти среднее значение отфитрованных чисел
numbers = [6, 15, 24, 9, 30, 12, 5, 18]
filtered = []
for i in numbers:
    if i > 10 and i % 2 == 0:
        filtered.append(i)
average = sum(filtered)/len(filtered)
print(average)

# Задача 4: Найти второе по величине число среди числе больше 10 и чётных 
numbers = [7, 14, 3, 22, 9, 18, 5, 26, 11]
filtered = []
for i in numbers:
    if i > 10 and i % 2 == 0:
        filtered.append(i)
filtered.sort()
filtered[-2]
print(filtered[-2])

# Задача 5: Фильтрация + сумма + условная корректировка результата
numbers = [4, 12, 7, 18, 9, 24, 3, 16, 11, 20, 5]
filtered = []
for i in numbers:
    if i > 6 and i % 2 == 0:
        filtered.append(i)
total = sum(filtered)
if total > 50:
    filtered.remove(min(filtered))
    total = sum(filtered)
print(total)

