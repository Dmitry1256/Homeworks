# Подготовка к заданию 1
def wage(piecework, hours):
    bonus = piecework * hours * 0.1
    total = piecework * hours + bonus
    return print(f' Всего {total}')


wage(piecework=int(input('Ставка  ')), hours=int(input('часы  ')))
