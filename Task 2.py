# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def input_num():
    while True:
        try:
            n = int(input("Insert number: "))
            return n
        except:
            print("Wrong. Try again")


def sum_list(num):
    lst = []
    res = 1
    for i in range(1, num + 1):
        res = res * i
        lst.append(res)
    return lst


print(sum_list(input_num()))

