# Урок 4. Задание 6а
from itertools import count
from itertools import cycle

from sys import argv

_, nn1, nn2 = argv

print('Нижняя граница: ', nn1)
print('Верхняя граница ', nn2)

# generator


for n in count(nn1):

    if n > nn2:
        break
    # else:
    print(f'Число  {int(n)}')


# def generator():
#     for el in count(n1):
#         if el < n2 + 1:
#             yield el
#
#
# for n in generator():
#     print(f'Число {n}')




# # Урок 4. Задание 6в
# list_1 = input('Введите элементы ')
# max_el = int(input('Введите максимальное число элементов '))
# nn = 0
# for el in cycle(list_1):
#     if nn > max_el:
#         break
#     print(el)
#     nn += 1
