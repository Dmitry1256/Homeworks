# Урок 4. Задание 6а
from itertools import count
from itertools import cycle

from sys import argv

_, = argv

n1 = int(input('Нижняя граница '))
n2 = int(input('Верхняя граница '))
# generator


for n in count(n1):

    if n > n2:
        break
    # else:
    print(f'Число  {int(n)}')


# Урок 4. Задание 6в
list_1 = input('Введите элементы ')
max_el = int(input('Введите максимальное число элементов '))
nn = 0
for el in cycle(list_1):
    if nn > max_el-1:
        break
    print(el)
    nn += 1
