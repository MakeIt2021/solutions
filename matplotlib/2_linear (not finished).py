import matplotlib.pyplot as plt
# не решено до конца

def grapher(x1, x2, y1, y2, x1_2, y1_2, x2_2, y2_2):
    plt.plot([x1, x2], [y1, y2])
    plt.plot([x1_2, x2_2], [y1_2, y2_2])
    plt.show()


# первая функция
x = 0
st1 = input("Пожалуйста, введите функцию вида y=k*x+b: ")
exec(st1)
x1 = x
y1 = y
x = 5
exec(st1)
x2 = x
y2 = y


# вторая функция
x = 0
st2 = input("Пожалуйста, введите функцию вида y=k*x+b: ")
exec(st2)
x1_2 = x
y1_2 = y
x = 5
exec(st2)
x2_2 = x
y2_2 = y


grapher(x1, y1, x2, y2, x1_2, y1_2, x2_2, y2_2)