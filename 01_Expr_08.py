import math


def sqrt_n_times(x, n):
    for i in range(n):
        x = math.sqrt(x)
    return x


def cube_root(y):
    a = sqrt_n_times(y, 2)
    b = sqrt_n_times(a, 2)
    c = sqrt_n_times(a * b, 4)
    d = sqrt_n_times(a * b * c, 8)
    e = sqrt_n_times(a * b * c * d, 16)
    f = sqrt_n_times(a * b * c * d * e, 32)
    return a * b * c * d * e * f


def main():
    q = float(input())
    print(cube_root(q))


exec(input())  # DON'T remove this line
