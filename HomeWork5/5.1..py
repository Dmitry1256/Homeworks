# Задача 1 1.
# Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

print('Вариант 1')
n = 1
with open('file_1.txt', 'a', encoding='UTF-8') as data_1:
    while True:
        data = input('Введите данные или пробел: ')
        if data == ' ':
            data_1.write(f'Строка {n} -- Данные не введены. Набор завершен\n')
            print('Данные не введены. Набор завершен')
            break
        else:
            data_1.write(f'Строка {n} -- {data}\n')
        n += 1

#######################

print('Вариант 2')
while True:
    file = open('file_1.txt', 'a', encoding='UTF-8')
    data = input('Введите данные или "Ввод" для завершения: ')
    if data == '':
        file.close()
        break
    file.write(f'{data}\n')


########################
print('Вариант 3')
while True:
    file = open('file_1.txt', 'a', encoding='UTF-8')
    data = input('Введите данные или "Ввод" для завершения: ')
    if data != '':
        file.write(f'{data}\n')
    else:
        print('Данные не введены. Набор завершен')
        file.close()
        break


############################
print('Вариант 4')

with open('file_1.txt', 'a', encoding=' UTF-8') as data_1:
    while True:
        data = input('Введите данные или "Ввод" для завершения: ')
        if data == '':
            data_1.write(f' {data}\n')
            print('Данные не введены. Набор завершен')
            break


