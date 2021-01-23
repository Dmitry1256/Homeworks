# 5. Реализовать формирование списка, используя функцию range()
# и возможности генератора. В список должны войти четные числа
# от 100 до 1000 (включая границы). Необходимо получить результат
# вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce

print('Вариант 1')


def list_1(prev_n, n):
    return prev_n * n


print(reduce(list_1, [el for el in range(100, 1001, 2)]))  # Вычисление
print([el for el in range(100, 1001, 2)])  # Список числел

print('Вариант 2')


def list_2(prev_n, n):
    return prev_n * n


my_list = [el for el in range(100, 1000, 2)]  # Список числел
print(reduce(list_2, my_list))  # Вычисление в 2 сроки
print(my_list)  # Список числел
