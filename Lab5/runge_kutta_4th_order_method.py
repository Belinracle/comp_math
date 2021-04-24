def calculate_h(x0, y0, fxy, fx, c_integral, inaccuracy):
    h = 8
    while abs(calculate_next_y(x0, y0, fxy, h) - fx(x0 + h, c_integral)) > inaccuracy:
        h = h / 2
    # print("h in iter : " + str(h))

    return h


def calculate_next_y(x, y, fxy, h):
    k1 = h * fxy(x, y)
    k2 = h * fxy(x + 0.5 * h, y + 0.5 * k1)
    k3 = h * fxy(x + 0.5 * h, y + 0.5 * k2)
    k4 = h * fxy(x + h, y + k3)
    y_next = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    return y_next


def calculate_data_set(x0, y0, x_last, fxy, fx, c_integral, inaccuracy):
    x = []
    y = []
    x.append(x0)
    y.append(y0)
    while x[len(x) - 1] < x_last:
        h = calculate_h(x[len(x) - 1], fx(x[len(x) - 1], c_integral), fxy, fx, c_integral, inaccuracy)
        x.append(x[len(x) - 1] + h)
        y.append(calculate_next_y(x[len(x) - 2], y[len(y) - 1], fxy, h))
    x.pop(len(x) - 1)
    y.pop(len(y) - 1)
    x.append(x_last)
    y.append(calculate_next_y(x[len(x) - 2], y[len(y) - 1], fxy, x_last - x[len(x) - 2]))
    print(x)
    print(y)
    return x, y



