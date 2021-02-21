# Задача 7
from math import factorial

print('Вариант 1')
my_number = int(input('Введите число : '))


def fact():
    for el in range(my_number):
        yield el + 1


for el in fact():
    print(f'Факториал числа {el}! = {factorial(el)}')
print('--------------------------------')

print('Вариант 2')
my_num = int(input('Введите число : '))


def fact(my_num):  # можно fact()
    for el in range(my_num + 1):
        yield factorial(el)


for el in fact(my_num):  # можно fact()
    print(f'Факториал числа {my_num}! = {el}')

print('--------------------------------')
print('Вариант 3')

my_num = int(input('Введите число : '))
list = list(range(my_num + 1))


def fact():
    for index, el in enumerate(list):
        yield (el, factorial(el))


for el in fact():
    print(f'Пара: (число,факториал) - {el}')
