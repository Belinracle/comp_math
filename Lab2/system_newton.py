from scipy.linalg import solve


def make_der_matrix(df, x):
    matrix = []
    for i in df:
        row = []
        for a in range(len(df)):
            row.append(i[a](*x))
        matrix.append(row)
    return matrix


def solve_system(f, df, x, epsilon):
    print("Уточнение корня: " + str(x))
    while True:
        prev = x
        b = []
        for i in range(len(f)):
            b.append(f[i](*x))
        matrix = make_der_matrix(df, prev)
        x = prev - solve(matrix, b)
        if all(i < epsilon for i in abs(x - prev)):
            break
    return x
