import numpy as np


def solve_with_eps_sympson(a, b, n, func, eps):
    I0 = solve_integral(a, b, n, func)
    n = n * 2
    I1 = solve_integral(a, b, n, func)
    while abs(I1 - I0) > eps:
        I0 = I1
        n = n * 2
        I1 = solve_integral(a, b, n, func)
    return I1, abs(I1 - I0) / 15, n


def solve_integral(a, b, n, func):
    x = np.linspace(a, b, n, True)
    y=[]
    for i in x:
        y.append(func(i))
    h = (b - a) / n
    return (h / 3) * (y[0] + 4 * (sum(y[1:len(x) - 2:2])) + 2 * (sum(y[2:len(x) - 3:2])) + y[len(y) - 1])
