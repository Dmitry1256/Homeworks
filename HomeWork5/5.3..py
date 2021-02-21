# Задача 3 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open("file_3.txt", encoding='UTF-8') as my_f:
    list_1 = my_f.read().split()

income = list_1[1:len(list_1):2]  # список з/п
names = list_1[:len(list_1):2]  # список Фамилий
income_1 = [float(x) for x in income]  # список з/п в числах

for i, income in enumerate(income_1):
    if income < 20000:
        print(f'Зарплату меньше 20000.00 рублей получает - {names[i]} ({income} руб.)')

print(f'Средняя зарплата: {round(sum(income_1) / len(income_1),2)} руб.')
