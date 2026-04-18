# Задача 1: выводим числа списком
numbers = [3, 7, 2, 9]
for i in numbers:
    print(i) 

# Задача 2: выводим чётные числа
numbers = [3, 7, 2, 9, 4 ,6]
for i in numbers:
    if i % 2 == 0:
        print(i)

# Задача 3: считаем чётные числа
count = 0
numbers = [5, 8, 3, 10, 2, 7]
for i in numbers:
    if i % 2 == 0:
        count += 1
print(count)

# Задача 4: выводим числа, которые больше 5
numbers = [4, 9, 1, 12, 7, 6]
for i in numbers:
    if i > 5:
        print(i)

# Задача 5: считаем числа больше 10
count =  0
numbers = [5, 12, 18, 7, 3, 20]
for i in numbers:
     if i > 10:
        count += 1
print(count)

# Задача 6: выводим числа, которые больше 5 и при этом чётные 
numbers = [2, 6, 9, 10, 11, 14, 3]
for i in numbers:
    if i % 2 == 0 and i > 5:
        print(i)
