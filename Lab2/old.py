import sys
import matplotlib.pyplot as plt
import numpy as np
import utils
import bisection
import simple_iter

functions = [("x^2-9", lambda x: x * x - 9), ("sin(x)-1/x", lambda x: np.sin(x) - 1 / x)]
functions_forms = [("x^2-4x+3", lambda x: (x ** 2 + 3) / 4), ("sin(x)-1/x", lambda x: 1 / (np.sin(np.pi * x / 180)))]


def choose_function():
    print("Выберите нелинейное уравнение")
    counter = 0
    for pair in functions:
        print(str(counter) + ": " + pair[0])
        counter += 1
    num = utils.read_int(0, len(functions) - 1, "Выберите номер уравнения")
    return num


def choose_epsilon():
    return utils.read_float(0, sys.float_info.max, "Введите эпсилон")


def choose_section():
    left = utils.read_float(-sys.float_info.max, sys.float_info.max, "Введите левую границу а")
    while True:
        right = utils.read_float(-sys.float_info.max, sys.float_info.max, "Введите правую границу b")
        if right < left:
            print("Извините, правая граница не может быть левее левой границы")
            continue
        else:
            break
    return left, right


def show(function_num, section, epsilon):
    function = functions[function_num][1]
    x = np.arange(section[0], section[1] + 0.1, 0.5)
    y = function(x)
    plt.plot(x, y)
    plt.grid()
    if utils.section_checker(function, section[0], section[1]):
        c = bisection.bisection_method(function, section[0], section[1], epsilon)
        iter_x = simple_iter.iter_method(functions_forms[function_num][1], section[0], section[1], eps)
        print("бисекция Приближенное значение корня с заданной точностью равно: " + str(c))
        print("итерации Приближенное значение корня с заданной точностью равно: " + str(iter_x))
        plt.scatter(c, 0)
        plt.scatter(iter_x, 0)
        plt.hlines(0, x.min(), x.max(), color="black")
    else:
        print("На указанном промежутке корней нет")
    if section[0] * section[1] <= 0:
        plt.vlines(0, y.min(), y.max(), color="black")
    plt.show()


func = choose_function()
sect = choose_section()
eps = choose_epsilon()
show(func, sect, eps)
