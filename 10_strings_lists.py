# Задача 1: Собрать только буквы из строки 
text = "python123code456"
filtered = []
for i in text:
  if i.isalpha():
    filtered.append(i)
print(filtered)

# Задача 2: Собрать только цифры из строки
text = "abc123xyz456"
filtered = []
for i in text:
    if i.isdigit():
        filtered.append(i)
print(filtered)

# Задача 3: Найти сумму цифр в строке
text = "python123code456"
total = 0
for i in text:
    if i.isdigit():
         total += int(i)
print(total)

# Задача 4: Собрать только цифры и найти максимальную
text = "a1b2c3d4e5"
filtered = []
for i in text:
    if i.isdigit(): 
        filtered.append(i)
max_value = max(filtered)
print(max_value)

# Задача 5: Найти сумму цифр больше 4 в строке 
text  = "a1b2c3d4e5f6g7h8"
total = 0
for i in text:
    if i.isdigit():
        if int(i) > 4:
             total += int(i)
print(total)
