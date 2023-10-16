import matplotlib.pyplot as plt
import numpy as np


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
y4 = 2 / x

ax.plot(x, y, label='sin(x)')
ax.plot(x, y2, label='cos(x)')
ax.plot(x, y3, label='x^2')
ax.plot(x, y4, label='x/2')

ax.legend()
plt.show()
