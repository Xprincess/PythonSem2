# Реализуйте алгоритм перемешивания списка.

import random


def input_num():
    while True:
        try:
            n = int(input("Insert the length of the list: "))
            return n
        except:
            print("Wrong. Try again")


def create_random_lst(size):
    lst = []
    while True:
        try:
            iMin = int(input("Insert min number: "))
            iMax = int(input("Insert max number: "))
            break
        except:
            print("Wrong. Try again")

    for i in range(size):
        lst.append(random.randint(iMin, iMax))
    return lst


def shuffle_lst(lst):
    for i in range(len(lst)):
        rnd = random.randint(0, len(lst))
        lst[i], lst[rnd] = lst[rnd], lst[i]
        return lst


my_list = create_random_lst(input_num())
print(f'Random list: {my_list}')

print(f'Mixed list: {shuffle_lst(my_list)}')