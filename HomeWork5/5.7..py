'''
Задача 7
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
 Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее
в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''
import json

for_read_file = '5.7.txt'
for_write_file = '5.7.json'

with open(for_read_file, 'r', encoding='UTF-8') as file_1:
    lines = file_1.readlines()
    sum_income = 0
    res = {}

    for l in lines:
        name, form, income, outcome = l.split()
        profit = int(income) - int(outcome)
        res[name] = profit
        if profit > 0:
            sum_income += profit

res['aver_prof'] = sum_income / len(lines)

with open(for_write_file, 'w', errors='UTF-8') as file_2:
    json.dump(res, file_2)
