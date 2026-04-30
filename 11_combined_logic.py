# Задача 1: Найти сумму цифр больше 4 в строке 
text = "a3b8c1d6e9f2"
filtered = []
total = 0
for i in text:
    if i.isdigit():
        if int(i) > 4:
            filtered.append(i)
            total += int(i)
print(total)

# Задача 2: Найти максиммальную цифру больше 3 в строке:
text = "p4y7t1h9o2n8"
filtered = []
for i in text:
    if i.isdigit():
        if int(i) > 3:
            filtered.append(i)
max_value = max(filtered)
print(max_value)

# Задача 3: Сумма чётных цифр из строки 
text = "a1b2c3d4e5f6g7h8"
total = 0
for i in text:
    if i.isdigit():
        if int(i) % 2 == 0:
            total += int(i)
print(total)

# Задача 4: Сложная фильтрация: сумма цифр > 3 и чётных 
text = "a3b8c1d6e9f2g7h4"
total = 0
for i in text:
    if i.isdigit():
        if int(i) > 3 and int(i) % 2 == 0:
            total += int(i)
print(total)

# Задача 5: Посчитать среднее число от суммы и количества четных цифр больше 3 в строке
text = "a5b2c9d8e1f6g3h7i4j0"
total = 0
count = 0
for i in text:
    if i.isdigit():
        if int(i) > 3 and int(i) % 2 == 0:
            total += int(i)
            count += 1
average = total / count
print(average)

# Задача 6: Разница между суммой и количеством нечётных цифр больше 4
text = "b7a2c9d4e1f8g3h6i5j0k7"
total = 0
count = 0
for i in text:
    if i.isdigit():
        if int(i) > 4 and int(i) % 2 != 0:
            total += int(i)
            count += 1
result = total - count
print(result)


