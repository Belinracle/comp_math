import numpy as np
import utils
import runge_kutta_4th_order_method as runge
import spline
import matplotlib.pyplot as plt

functions = (("y'-2(x^2+y)=0", lambda x, y: 2 * (x * x + y)),
             ("y'-2x=0", lambda x, y: 2 * x),
             ("x^2 * y' = 2xy + 3", lambda x, y: (2 * x * y + 3) / (x * x))
             )
functions_integral = (("y'-2(x^2+y=0)", lambda x, c: c * np.exp(2 * x) - x * x - x - 0.5),
                      ("y'-2x=0", lambda x, c: x * x + c),
                      ("x^2 * y' = 2xy + 3", lambda x, c: c * x * x - 1 / x)
                      )
functions_c = (("y'-2(x^2+y=0)", lambda x, y: (y + 0.5 + x + x * x) / np.exp(2 * x)),
               ("y'-2x=0", lambda x, y: y - x * x),
               ("x^2 * y' = 2xy + 3", lambda x, y: (y + 1 / x) / (x * x)))


def show(x, y, b, c, d, function, c_integral):
    points = []
    k = 1
    spline_y = []
    fun_x = np.arange(x[0], x[len(x) - 1], (x[len(x) - 1] - x[0]) / 1000)
    fun_y = function(fun_x, c_integral)
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


if __name__ == '__main__':
    func_num = utils.choose_from_map(functions)
    x0, x_last = utils.read_section("Введите промежуток используя ;", ";")
    inaccuracy = utils.read_float(0, 100, "Введите точность, с которой будет вычислено значение")
    y0 = utils.read_float(-1000.0, 1000.0, "Введите значение у0 в левой границе отрезка")
    try:
        c_integral = functions_c[func_num][1](x0, y0)
        x, y = runge.calculate_data_set(x0, y0, x_last, functions[func_num][1], functions_integral[func_num][1],
                                        c_integral, 0.1)
        # print(x)
        # print(y)
        a, b, c, d = spline.get_coefficients(x, y)
        show(x, y, b, c, d, functions_integral[func_num][1], c_integral)
    except Exception:
        print("Произошла ошибка при вычислении функции либо не хватает данных для использования метода сплайнов")
