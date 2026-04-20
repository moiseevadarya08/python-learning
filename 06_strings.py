# Задача 1: подсчёт символа 
count = 0
text = "banana" 
for i in text:
    if i == "a":
        count += 1
print(count)

# Задача 2: вывод символа по условию
text = "hello world"
for i in text:
    if i == "o":
        print(i)

# Задача 3: подсчёт гласных букв
text = "python programming" 
count = 0
for i in text:
    if i in "aeiou":
        count += 1
print(count)

# Задача 4: подсчёт цифр
text = "python123"
count = 0
for i in text:
    if i in "0123456789":
        count += 1 
print(count)

# Задача 5: подсчёт согласных букв 
text = "hello world"
count = 0
for i in text:
    if i.isalpha() and i not in "aeiou":
        count += 1
print(count)

# Задача 6: подсчёт уникальных гласных
text = "hello world"
vowels_found = set ()
for i in text:
    if i in "aeiou":
        vowels_found.add(i)
print(len(vowels_found))


