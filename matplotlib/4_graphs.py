import matplotlib.pyplot as plt
import numpy as np


def grapher():
    plt.title('Графики sin(x), cos(x), x^2, 2/x')
    plt.xlabel('x')
    plt.xlabel('y')
    plt.grid()

    ax = plt.gca()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    x = np.linspace(-2, 2, 100)
    y = np.sin(x)
    y2 = np.cos(x)
    y3 = x ** 2
    x4 = np.linspace(0.01, 2, 100)
    y4 = 2 / x4
    x5 = np.linspace(-2, -0.01, 100)
    y5 = 2 / x5
    ax.plot(x, y, label='sin(x)')
    ax.plot(x, y2, label='cos(x)')
    ax.plot(x4, y4, color='r')
    ax.plot(x5, y5, color='r', label='2/x')

    ax.legend()
    plt.show()

grapher()