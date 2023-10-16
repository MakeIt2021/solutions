import matplotlib.pyplot as plt
from random import randint


def grapher():
    plt.title('Столбчатая диаграмма')
    plt.ylabel('values')
    plt.xlabel('fields')
    plt.grid()

    fields = [0, 1, 2, 3, 4, 5, 6]
    values = []
    for _ in fields:
        values.append(randint(1, 100))
    plt.bar(fields, values)

    plt.show()

grapher()
