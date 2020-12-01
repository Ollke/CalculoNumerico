def GaussSeidel4V(f1, f2, f3, f4, e):
    x0 = 0
    y0 = 0
    z0 = 0
    w0 = 0

    while True:
        # calculo dos novos valores
        x1 = f1(x0, y0, z0, w0)
        y1 = f2(x1, y0, z0, w0)
        z1 = f3(x1, y1, z0, w0)
        w1 = f4(x1, y1, z1, w0)

        # erro
        erro1 = abs(x1 - x0)
        erro2 = abs(y1 - y0)
        erro3 = abs(z1 - z0)
        erro4 = abs(w1 - w0)

        # atribuição dos novos valores
        x0 = x1
        y0 = y1
        z0 = z1
        w0 = w1

        if erro1 < e and erro2 < e and erro3 < e and erro4 < e:
            break

    return [x0, y0, z0, w0]


def GaussSeidel3V(f1, f2, f3, e):
    x0 = 0
    y0 = 0
    z0 = 0

    while True:
        # calculo dos novos valores
        x1 = f1(x0, y0, z0, w0)
        y1 = f2(x1, y0, z0, w0)
        z1 = f3(x1, y1, z0, w0)

        # erro
        erro1 = abs(x1 - x0)
        erro2 = abs(y1 - y0)
        erro3 = abs(z1 - z0)

        # atribuição dos novos valores
        x0 = x1
        y0 = y1
        z0 = z1

        if erro1 < e and erro2 < e and erro3 < e:
            break

    return [x0, y0, z0]


f1 = lambda x, y, z, w: (-(7.89 * y) - (4.95 * z) - (6.36 * w) + 32.67) / 23.21
f2 = lambda x, y, z, w: (-(8.05 * x) - (5.05 * z) - (1.25 * w) + 22.27) / 14.7
f3 = lambda x, y, z, w: (-(2.02 * x) - (7.77 * y) - (6.72 * w) + 29.84) / 23.04
f4 = lambda x, y, z, w: (-(0.32 * x) - (6.05 * y) - (4.77 * z) + 19.67) / 14.78
e = 10 ** -4

r = GaussSeidel4V(f1, f2, f3, f4, e)

print(f"x = {r[0]}")
print(f"y = {r[1]}")
print(f"z = {r[2]}")
print(f"w = {r[3]}")