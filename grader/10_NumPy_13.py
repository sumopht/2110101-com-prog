import math
import numpy as np


def p(X):
    return 1 / (1 + math.e ** (-1 * (-3.98 + (np.array([0.1, 0.5]) * np.array(X)).sum(axis=1))))


exec(input().strip())
