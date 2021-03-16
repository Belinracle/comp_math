import utils as ut
import integral_solve_symp
import numpy as np

integral = u'\u222b'
integrals = ((integral + "x^2 dx", lambda x: x ** 2),
             (integral + "x^3 dx", lambda x: x ** 3),
             (integral + "sin(x) dx", lambda x: np.sin(x)),
             (integral + "x^3-x^2+3 dx", lambda x: x ** 3 - x ** 2 + 3))
print("Выберите какой интеграл посчитать")
integral_num = ut.choose_from_map(integrals)
section = ut.read_section("Введите интервал используя разделитель ;", ";")
epsilon = ut.read_float(0, 100, "Введите эпсилон")
result, inaccuracy, new_n = integral_solve_symp.solve_with_eps_sympson(section[0], section[1], 5,
                                                                       integrals[integral_num][1], epsilon)
print("Результат работы метода Симпсона: " + str(result))
print("Погрешность вычисления метода Симпсона: " + str(inaccuracy))
print("n: " + str(new_n))
5
