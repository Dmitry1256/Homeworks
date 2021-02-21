# Урок 4. Задание 6
from itertools import count
from itertools import cycle

# from sys import argv
#
# _, n1, n2 = argv
# print('Нижняя граница ', n1)
# print('Верхняя граница ', n2)

n1 = int(input('Нижняя граница '))
n2 = int(input('Верхняя граница '))


def generator():
    for el in count(n1):
        if el < n2 + 1:
            yield el


for n in generator():
    print(f'Число {n}')
