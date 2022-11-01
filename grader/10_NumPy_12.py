import math
import numpy as np


def toCelsius(f):
    return (f - 32) * 5 / 9


def BMI(wh):
    temp = np.array([])
    for i in wh:
        temp = np.append(temp, i[0] / (i[1] / 100) ** 2)
    return temp


def distanceTo(p, Points):
    temp = np.array([])
    for i in Points:
        temp = np.append(temp, math.sqrt((p[0] - i[0]) ** 2 + (p[1] - i[1]) ** 2))
    return temp


exec(input().strip())
