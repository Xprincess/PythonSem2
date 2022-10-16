# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def numberssum():
    sum = 0
    for elem in input("Введите вещественное число: "):
        if elem == "." or elem == "-":
            continue
        else:
            sum = int(elem) + sum
    return sum

while True:
    try:
        print(f"Сумма вещественных чисел: {numberssum()}")
        break
    except:
        print("Неправильный ввод, попоробуйте снова")

