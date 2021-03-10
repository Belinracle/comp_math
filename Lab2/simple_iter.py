def set_x(x):
    # print("(итерации)Очередное приближение x = " + str(x))
    return x


def iter_method(function, eps, x):
    print("Уточнение корня в районе "+str(x))
    rez = x
    x = set_x(function(rez))
    while abs(x-rez) > eps:
        rez = x
        x = set_x(function(x))
    return x
