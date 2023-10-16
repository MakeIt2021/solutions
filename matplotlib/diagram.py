import matplotlib.pyplot as plt
from random import randint


def diagram(n):
    plt.title('Круговая диаграмма')
    plt.grid()

    values = []
    for _ in range(n - 1):
        val = randint(1, int(100 / n))
        values.append(val)
    values.append(100 - sum(values))

    plt.pie(values)
    plt.show()

diagram(6)