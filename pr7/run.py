import numpy as np
from Apriori import *

# TODO: заполните матрицу X исходными данными, используя таблицу, приведенную в методических указаниях.
# каждая строка в матрице X - это отдельная транзакция.
# Транзакция соответствует часу наблюдения за обезьянкой.
# В столбцах - события. Первый столбец соответствует событию "есть",
# второй - "играть", третий - "спать", четвертый - "чистить шерстку".
# Например, строка 1 0 1 1 означает, что в течение наблюдаемого часа
# обезьянка ела, спала и чистила шерстку.
# X = np.array([...])

X = np.array([
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 0]
])


actions = ['ест', 'играет', 'спит', 'чистит шёрстку']

# минимальная поддержка - событие должно встречаться минимум в 40% транзакций
sup = 0.4

# поиск ассоциативных правил
# функция вовзращает матрицу обнаруженных ассоциативных правил
# каждая строка описывает отдельное правило. Правило описывается сочетанием событий
# и его поддержкой. Например, правило "играет и спит" с поддержкой 55% будет
# выглядеть так: [0 1 1 0 0.55], а правило "ест и спит" с поддержкой 70% так: [1 0 1 0 0.7]
rules = apriori(X, sup)

# отображение результатов
for rule in rules:
    for i, item in enumerate(rule[0: -1]):
        if item == 1:
            print('%s\t' % actions[i], end='')
    print('-> %f' % rule[-1])
