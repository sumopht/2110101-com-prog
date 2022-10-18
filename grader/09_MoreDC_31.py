import math


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_coprime(a, b, c):
    if gcd(gcd(a, b), c) == 1:
        return True
    else:
        return False


def is_integer(n):
    if n / int(n) == 1:
        return True
    else:
        return False


def primitive_Pythagorean_triples(max_len):
    triple = []
    peri = []
    for c in range(1, max_len):
        for a in range(1, c):
            b = math.sqrt(c ** 2 - a ** 2)
            if is_integer(b) and (a + b + c) not in peri and is_coprime(a, b, c):
                triple.append([a, int(b), c])
                peri.append(a + b + c)
    return triple


exec(input().strip())
