import spline
import numpy as np
import matplotlib.pyplot as plt
import utils

functions = (("sin(x)", lambda x: np.sin(x)),
             ("cos(x)-x/2", lambda x: np.cos(x) - x / 2)
             )


def show(x, y, b, c, d, function):
    points = []
    while True:
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
            plt.vlines(0, min(fun_y), max(fun_y), color="black")
        plt.show()
        x_i = utils.read_float(x[0], x[len(x) - 1],
                               "Введите х в котором хотите подсчитать значение функции интерполяции")
        for k in range(1, len(x)):
            if x[k - 1] <= x_i <= x[k]:
                y_i = y[k] + b[k] * (x_i - x[k]) + c[k] * (x_i - x[k]) ** 2 + d[k] * (x_i - x[k]) ** 3
                print("Значение функции интерполяции в указанной точке: " + str(y_i))
                points.append((x_i, y_i))
                break


def create_date_set(function, x, filename):
    f = open(filename, "w")
    y = function(x)
    for i in range(len(x)):
        f.write(str(x[i]) + " " + str(y[i]) + "\n")
    f.close()


def read_data(filename):
    x = []
    y = []
    f = open(filename, 'r')
    data_lines = f.readlines()
    for line in data_lines:
        line_data = line.split(" ")
        x.append(float(line_data[0]))
        y.append(float(line_data[1]))
    return x, y


def main():
    # create_date_set(lambda x: np.sin(x), np.linspace(0, 10, 10, endpoint=True), "sin.txt")
    # x, y = read_data("sin.txt")
    # a, b, c, d = spline.get_coefficients(x, y)
    # show(x, y, b, c, d, lambda t: np.sin(t))
    func_num = utils.choose_from_map(functions)
    section = utils.read_section("Введите интервал, используя разделитель ;", ";")
    n = utils.read_int(0, 100, "Укажите количество узлов для вычисления уравнения сплайнов")
    x = np.linspace(section[0], section[1], n, endpoint=True)
    y = functions[func_num][1](x)
    a, b, c, d = spline.get_coefficients(x, y)
    show(x, y, b, c, d, functions[func_num][1])


if __name__ == "__main__":
    main()
