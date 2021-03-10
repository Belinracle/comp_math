import utils as ut
import bisection
import simple_iter
import numpy as np
import matplotlib.pyplot as plt
import system_newton

FIRST = "x^2-7x+1"
SECOND = "x^3-x-1"
THIRD = "3x^2-4+1/x"
FOURTH = "sin(x^2+1)-x"

S_FIRST = "|x^3-x^2+2-y \n" + "   |x^2-y"
S_SECOND = "|sin(x)-x \n" + "   |cos(x)"

types = ["Выбрать нелинейное уравнение", "Выбрать систему нелинейных уравнений"]
equations = [(FIRST, lambda x: x * x - 7 * x + 1),
             (SECOND, lambda x: x ** 3 - x - 1),
             (THIRD, lambda x: 3 * x ** 2 - 4 + 1 / x),
             (FOURTH, lambda x: np.sin(x ** 2 + 1) - x)]
equations_sections = {
    FIRST: (0, 1),
    SECOND: (0.5, 2),
    THIRD: (0.1, 0.5),
    FOURTH: (0.5, 1)
}
equations_x = {
    FIRST: 0,
    SECOND: 1.2,
    THIRD: 0.2,
    FOURTH: 0.7
}
equations_equals = {
    FIRST: lambda x: (x * x + 1) / 7,
    SECOND: lambda x: (x + 1) ** (1 / 3),
    THIRD: lambda x: 1 / (-3 * x ** 2 + 4),
    FOURTH: lambda x: np.sin(x ** 2 + 1)
}
systems = [(S_FIRST, (lambda x, y: x ** 3 - x ** 2 + 2 - y,
                      lambda x, y: x ** 2 - y)),
           (S_SECOND, (lambda x, y: np.sin(x) - x - y,
                       lambda x, y: np.cos(x) - y))]

der_system = {
    S_FIRST: ((lambda x, y: 3 * x ** 2 - 2 * x, lambda x, y: -1),
              (lambda x, y: 2 * x, lambda x, y: -1)),
    S_SECOND: ((lambda x, y: np.cos(x) - 1, lambda x, y: -1),
               (lambda x, y: -1 * np.sin(x), lambda x, y: -1))
}
system_x = {
    S_FIRST: (-0.5, 0.5),
    S_SECOND: (-1.5, 0.5)
}
systems_sections = {
    S_FIRST: (-1, 0),
    S_SECOND: (-2, -1)
}

system_plots = {
    S_FIRST: (lambda x: x ** 3 - x ** 2 + 2, lambda x: x ** 2),
    S_SECOND: (lambda x: np.sin(x) - x, lambda x: np.cos(x))
}


def show_equation(function, a, b, points):
    x = np.arange(a, b, (b - a) / 1000)
    y = function(x)
    plt.plot(x, y)
    plt.grid()
    for point in points:
        plt.scatter(point, 0)
    plt.hlines(0, x.min(), x.max(), color="black")
    if a * b <= 0:
        plt.vlines(0, y.min(), y.max(), color="black")
    plt.show()


def show_system(functions, section, point):
    plots = []
    x = np.arange(section[0], section[1], (section[1] - section[0]) / 1000)
    for f in functions:
        plots.append(x)
        plots.append(f(x))
    plt.plot(*plots)
    plt.scatter(point[0], point[1])
    plt.grid()
    plt.hlines(0, x.min(), x.max(), color="black")
    plt.show()


choose = ut.choose_from_list(types)
if choose == 0:
    epsilon = ut.read_float(0.00000000001, 10000000000, "Укажите точность")
    results = []
    equation_num = ut.choose_from_map(equations)
    equation_as_str = equations[equation_num][0]
    equation_section = equations_sections[equation_as_str]
    bisection_result = bisection.bisection_method(equations[equation_num][1], equation_section[0], equation_section[1],
                                                  epsilon)
    simple_iter_result = simple_iter.iter_method(equations_equals[equation_as_str], epsilon,
                                                 equations_x[equation_as_str])
    results.append(bisection_result)
    results.append(simple_iter_result)
    print("Результат выполнения метода бисекции: " + str(bisection_result))
    print("Результат выполнения метода простых итераций: " + str(simple_iter_result))
    print("Разность точности их выполнения: " + str(abs(bisection_result - simple_iter_result)))
    show_equation(equations[equation_num][1], equation_section[0], equation_section[1], results)
elif choose == 1:
    epsilon = ut.read_float(0.00000000001, 10000000000, "Укажите точность")
    system_num = ut.choose_from_map(systems)
    system_as_str = systems[system_num][0]
    point = system_newton.solve_system(systems[system_num][1], der_system[system_as_str], system_x[system_as_str],
                                       epsilon)
    print("Результат выполнения метода Ньютона " + str(point))
    show_system(system_plots[system_as_str], systems_sections[system_as_str], point)
