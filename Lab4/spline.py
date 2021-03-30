def get_coefficients(x, y):
    n = len(x)
    h = [None] * n
    l = [None] * n
    delta = [None] * n
    lamb = [None] * n
    b = [None] * n
    d = [None] * n
    c = [None] * n
    for i in range(1, n):
        h[i] = x[i] - x[i - 1]
        if h[i] == 0:
            return ValueError
        l[i] = (y[i] - y[i - 1]) / h[i]
    delta[1] = - h[2] / (2 * (h[1] + h[2]))
    lamb[1] = 1.5 * (l[2] - l[1]) / (h[1] + h[2])
    for i in range(3, n):
        delta[i - 1] = - h[i] / (2 * h[i - 1] + 2 * h[i] + h[i - 1] * delta[i - 2])
        lamb[i - 1] = (3 * l[i] - 3 * l[i - 1] - h[i - 1] * lamb[i - 2]) / (
                2 * h[i - 1] + 2 * h[i] + h[i - 1] * delta[i - 2])
    c[0] = 0
    c[n - 1] = 0
    for i in range(n - 1, 1, -1):
        c[i - 1] = delta[i - 1] * c[i] + lamb[i - 1]
    for i in range(1, n):
        d[i] = (c[i] - c[i - 1]) / (3 * h[i])
        b[i] = l[i] + (2 * c[i] * h[i] + h[i] * c[i - 1]) / 3
    return y, b, c, d
