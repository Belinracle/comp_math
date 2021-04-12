import numpy as np
import utils
import runge_kutta_4th_order_method as runge
import spline
import matplotlib.pyplot as plt


def show(x, y, b, c, d, function):
    points = []
    k = 1
    spline_y = []
    fun_x = np.arange(x[0], x[len(x) - 1], (x[len(x) - 1] - x[0]) / 1000)
    fun_y = function(fun_x)
    plt.plot(fun_x, fun_y, label="Выбранная функция")
    for i in fun_x:
        if i <= x[k]:
            spline_value = y[k] + b[k] * (i - x[k]) + c[k] * (i - x[k]) ** 2 + d[k] * (i - x[k]) ** 3
            spline_y.append(spline_value)
        else:
            spline_value = y[k] + b[k] * (i - x[k]) + c[k] * (i - x[k]) ** 2 + d[k] * (i - x[k]) ** 3
            spline_y.append(spline_value)
            k = k + 1
    for i in range(len(x)):
        plt.scatter(x[i], y[i])
    for point in points:
        plt.scatter(point[0], point[1])
    plt.plot(fun_x, spline_y, label='Вычисленная функция')
    plt.grid()
    plt.legend()
    plt.hlines(0, x[0], x[len(x) - 1], color="black")
    if x[0] * x[1] <= 0:
        plt.vlines(0, plt.ylim()[0], plt.ylim()[1], color="black")
    plt.show()


functions = (("y'-2(x^2+y=0)", lambda x, y: 2 * (x * x + y)),
             )
functions_integral = (("y'-2(x^2+y=0)", lambda x: (3 / 2) * np.exp(2 * x) - x * x - x - 0.5),
                      )

if __name__ == '__main__':
    x, y = runge.calculate_data_set(0.0, 1, 1.0, functions[0][1], functions_integral[0][1], 0.1)
    a, b, c, d = spline.get_coefficients(x, y)
    show(x, y, b, c, d, functions_integral[0][1])
