import spline
import numpy as np
import matplotlib.pyplot as plt


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


def show(x, y, a, b, c, d, function):
    k = 1
    spline_y = []
    fun_x = np.arange(x[0], x[len(x) - 1], (x[len(x) - 1] - x[0]) / 1000)
    fun_y = function(fun_x)
    plt.plot(fun_x, fun_y)
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
    plt.plot(fun_x, spline_y)
    plt.grid()
    plt.show()


# def show(x, y, a, b, c, d):
#     k = 1
#     # print(x)
#     # print(y)
#     spline_y = []
#     fun_x = np.arange(x[0], x[len(x) - 1] + (x[len(x) - 1] - x[0]) / 100, (x[len(x) - 1] - x[0]) / 100)
#     for i in fun_x:
#         if i <= x[k]:
#             spline_value = y[k] + b[k] * (i - x[k]) + c[k] * (i - x[k]) ** 2 + d[k] * (i - x[k]) ** 3
#             spline_y.append(spline_value)
#         else:
#             spline_value = y[k] + b[k] * (i - x[k]) + c[k] * (i - x[k]) ** 2 + d[k] * (i - x[k]) ** 3
#             spline_y.append(spline_value)
#             k = k + 1
#     for i in range(len(x)):
#         plt.scatter(x[i], y[i])
#     plt.plot(fun_x, spline_y)
#     plt.grid()
#     plt.show()


def main():
    x, y = read_data("sin.txt")
    a, b, c, d = spline.get_coefficients(x, y)
    show(x, y, a, b, c, d, lambda val: np.sin(val))


def create_date_set(function, x, filename):
    f = open(filename, "w")
    y = function(x)
    for i in range(len(x)):
        f.write(str(x[i]) + " " + str(y[i]) + "\n")
    f.close()


if __name__ == "__main__":
    create_date_set(lambda x: np.sin(x), np.arange(0, 10 * np.pi, 4), "sin.txt")
    main()
