history = []

while True:
    operation = input("Введите операцию (+, -, *, /)")
    if operation  == "exit": 
        break
    if operation == "history":
        for item in history:
            print(item)
        continue

    num1 = int(input("Введите число 1:"))
    num2 = int(input("Введите число 2:"))
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("На 0 делить нельзя")
            continue
        result = num1 / num2
    else:
        print("Неверная операция")
        continue

    print("Результат:", result)

    history.append(f"{num1} {operation} {num2} = {result}")
