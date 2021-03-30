import utils as ut
import integral_solve_symp
import numpy as np
import sys


def lnx(x):
    if x <= 0:
        raise ValueError
    else:
        return np.log(x)


def one_for_x(x):
    if x == 0:
        raise ValueError
    else:
        return 1 / x


def sinx_x(x):
    if x != 0:
        return np.sin(x) / x
    else:
        return 0


def x3_x2_div_x1(x):
    if x == 1:
        return 0
    return (x ** 3 - x ** 2) / (x - 1)


integral = u'\u222b'
integrals = ((integral + " x^2 dx", lambda x: x ** 2),
             (integral + " x^3 dx", lambda x: x ** 3),
             (integral + " sin(x) dx", lambda x: np.sin(x)),
             (integral + " x^3-x^2+3 dx", lambda x: x ** 3 - x ** 2 + 3),
             (integral + " 1/x dx", lambda x: one_for_x(x)),
             (integral + " ln(x) dx", lambda x: lnx(x)),
             (integral + " sin(x)/x dx", lambda x: sinx_x(x)),
             (integral + " (x^3-x^2)/(x-1) dx", lambda x: x3_x2_div_x1(x)))
print("Выберите какой интеграл посчитать")
integral_num = ut.choose_from_map(integrals)
section = ut.read_section("Введите интервал используя разделитель ;", ";")
epsilon = ut.read_float(0, 100, "Введите эпсилон")
try:
    result, inaccuracy, new_n = integral_solve_symp.solve_with_eps_sympson(section[0], section[1], 5,
                                                                           integrals[integral_num][1], epsilon)
    print("Результат работы метода Симпсона: " + str(result))
    print("Погрешность вычисления метода Симпсона: " + str(inaccuracy))
    print("n: " + str(new_n))
except ValueError as e:
    print("Произошла ошибка при вычислении значения функции на промежутке, Adios")
    sys.exit()
