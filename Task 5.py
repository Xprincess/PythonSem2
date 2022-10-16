# Реализуйте алгоритм перемешивания списка.

import random


def input_num():
    while True:
        try:
            n = int(input("Введите длину списка: "))
            return n
        except:
            print("Неправильный ввод, попробуйте снова")


def create_random_lst(size):
    lst = []
    while True:
        try:
            iMin = int(input("Введите минимальное рандомное число: "))
            iMax = int(input("Введите максимальное рандомное число: "))
            break
        except:
            print("Неправильный ввод, попробуйте снова")

    for i in range(size):
        lst.append(random.randint(iMin, iMax))
    return lst


def shuffle_lst(lst):
    for i in range(len(lst)):
        rnd = random.randint(0, len(lst))
        lst[i], lst[rnd] = lst[rnd], lst[i]
        return lst


my_list = create_random_lst(input_num())
print(f'Рандомный список выглядит так: {my_list}')

print(f'Перемешанный список выглядит так: {shuffle_lst(my_list)}')