# Заняття 2.
# Завдання 1. Квадрат числа
your_number = float(input("Визначення квадрата числа. Введіть число: "))
print("Квадрат числа = ", your_number ** 2)



# Завдання 2. Середнє трьох чисел
first_number = float(input("Визначення середнього. Введіть перше число: "))
second_number = float(input("Введіть друге число: "))
third_number = float(input("Введіть третє число: "))
print("Середнє арифметичне = ", (first_number + second_number + third_number) / 3)


# Завдання 3. Пететворення хвилит в години
minutes = int(input("Перетворення хвилин в години. Введіть кількість хвилин: "))
hours = minutes // 60
minutes_rem = minutes % 60
print (hours, "годин", minutes_rem, "хвилин")


# Завдання 4. Розрахунок знижки
price = float(input("Розрахунок знижки. Введіть ціну: "))
discount = float(input("Введіть знижку (%): "))
print ("Ціна зі знижкою: ", ((100-discount)*price) / 100)


# Завдання 5. Остання цифра числа
your_number = int(input("Остання цифра числа. Введіть число: "))
last_digit = your_number % 10
print("Остання цифра: ", last_digit)


# Завдання 6. Периметр прямокутника
length = float(input("Периметр прямокутника. Введіть довжину: "))
width = float(input("Введіть ширину: "))
print("Периметр: ", (length + width) * 2)


# Завдання 7. Виведення числа в стовбчик
your_number = int(input("Виведення числа в стовбчик. Введіть 4-х значне число: "))
digit_1 = your_number // 1000
digit_2 = your_number // 100 % 10
digit_3 = your_number // 10 % 10
digit_4 = your_number % 10

print(digit_1)
print(digit_2)
print(digit_3)
print(digit_4)

print("PR")