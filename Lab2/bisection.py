def set_c(c):
    # print("(бисекция)Очередное приближение с = "+str(c))
    return c


def bisection_method(function, a, b, eps):
    print("Поиск на промежутке ["+str(a)+";"+str(b)+"]")
    f_a = function(a)
    while b - a >= 2 * eps:
        if f_a == 0:
            return set_c(a)
        if function(b) == 0:
            return set_c(b)
        c = set_c((a + b) / 2)
        f_c = function(c)
        if f_c == 0:
            return c
        if f_a * f_c > 0:
            a = c
        else:
            b = c
    c = set_c((a + b) / 2)
    return c
