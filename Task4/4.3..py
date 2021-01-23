#3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.

# Решение в одну строку
print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

# Решение в 2 строки и меньше скобок
list_1 = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(list_1)

print('++++++++++++++')

# Тоже нормальный вариант
for n in range(20, 241):
    if n % 20 == 0 or n % 21 == 0:
        print(n)

print('---------------')


# Использование функции
def numbers():
    for n in range(20, 241):
        if n % 20 == 0 or n % 21 == 0:
            yield n


for n in numbers():
    print(n)
