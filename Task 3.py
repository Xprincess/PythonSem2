# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def input_num():
    while True:
        try:
            n = int(input("Insert number: "))
            return n
        except:
            print("Wrong. Try again")


def sequence_number(n):
    lst = []
    for i in range(1, n + 1):
        num = ((1 + 1 / i) ** i)
        lst.append(round(num, 2))
    return lst


print(sequence_number(input_num()))