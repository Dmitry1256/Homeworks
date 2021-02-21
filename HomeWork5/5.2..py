# Задача 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

print('Вариант 1а- Определение количества строк')

number_lines = open("file_2.txt", "r", encoding='UTF-8')
print(f'Количество строк в файле file_2.txt : {len(list(number_lines))}')  # Количество строк
number_lines.close()


print('Вариант 1б- Определение количества строк')
number_lines = open("file_2.txt", "r", encoding='UTF-8')
count1 = number_lines.readlines()
print(f'Всего строк в файле file_2.txt : {len(count1)}')
number_lines.close()

print('Вариант 2-Определение общего количестов слов')
with open("file_2.txt", "r", encoding='UTF-8') as file:
    lines = len(file.read().split())
    print(f'Всего слов во всех строках:  {lines}')


print('Вариант 2а -Определение количества слов в каждой  в строке')
number_lines = open("file_2.txt", "r", encoding='UTF-8')
n = 0
for line in number_lines:
    if line != '':
        n += 1
        numbers = len(line.split())
        print(f'Количество слов в строке № {n} равно: {numbers}')

number_lines.close()


print('Вариант 2в--Определение количества строк и слов в каждой  в строке')

with open("file_2.txt", encoding='UTF-8') as file:
    num = len(list(file))
    print(f'Всего строк в файле file_2.txt  : {num}')

print('--------------')
n = 1
with open("file_2.txt", encoding='UTF-8') as file:
    for lines in file:
        num = len(lines.split())
        print(f'В строке № {n} всего слов: {num}')
        n += 1
