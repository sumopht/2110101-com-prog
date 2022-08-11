from cmath import sqrt
import math


n = float(input())
print(
    (
        sqrt(2 * math.pi)
        * (n ** (n + (1 / 2)))
        * (math.e ** (-n + (1 / ((12 * n) + 1))))
    ).real
)
print(
    (sqrt(2 * math.pi) * (n ** (n + (1 / 2))) * (math.e ** (-n + (1 / (12 * n))))).real
)
