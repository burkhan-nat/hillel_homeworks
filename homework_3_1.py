"""
Програма має виконувати прості математичні дії (+, -, *, /). Користувачеві пропонується почерзі ввести
числа та дію над цими числами, а програма, виходячи з дії, обчислює та друкує результат.

Зробити перевірку на те, що при діленні дільник не дорівнює 0!
"""


first_number = float(input("Введіть перше число: "))
act = input("Введіть дію: +, -, *, /: ")
second_number = float(input("Введіть друге число: "))

if act == "+":
    result = first_number + second_number
elif act == "-":
    result = first_number - second_number
elif act == "*":
    result = first_number * second_number
elif act == "/":
    if second_number ==0:
        print ("Error. Ділення на 0")
    else:
        result = first_number / second_number
        print("Результат: ", result)




