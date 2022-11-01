import numpy as np


def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data


def report_lower_than_mean(weight, data):
    scores = np.array(data[:, 1:] * weight)
    weighted_scores = np.sum(scores, axis=1)
    mean = sum(weighted_scores) / len(data)
    lower = []
    for i in range(len(weighted_scores)):
        if weighted_scores[i] < mean:
            lower.append(str(data[i][:1]).lstrip('[').rstrip(']'))
    print('None') if len(lower) == 0 else print(', '.join(lower))


exec(input().strip())
