#  Задача 4 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
file_read = 'file_4_read.txt'
file_write = 'file_4_write.txt'
dic = {'One': 'Один',
       'Two': 'Два',
       'Three': 'Три',
       'Four': 'Четыре'
       }

with open(file_read, 'r', encoding='UTF-8') as f_1:
    eng = f_1.readlines()
    new = [f'{dic[line.split(" — ")[0]]} - {line.split(" — ")[-1]}' for line in eng]

    # for line in eng:
    #     new = [dic[line.split(" — ")[0]], '-', line.split(" — ")[-1]] #Выводит последнее значение
    #     print(new)

    with open(file_write, 'w', encoding='UTF-8') as f_2:
        f_2.writelines(new)
