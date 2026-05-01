Мини-проект: анализ цифр в строке 
text = "a5b2c8d1e9f4g7"
filtered = []
for i in text:
    if i.isdigit():
        filtered.append(int(i))
print(filtered)
total = sum(filtered)
count = len(filtered)
max_value=max(filtered)
min_value=min(filtered)
average = total / count

print("Цифры:", filtered)
print("Количество:", count)
print("Сумма:",total)
print("Максимум:", max_value)
print("Минимум:", min_value)
print("Среднее:", average)
