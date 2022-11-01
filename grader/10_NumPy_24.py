import numpy as np


def peak_indexes(x):
    l_shift = np.concatenate((x[1:], [999999]))
    r_shift = np.concatenate(([999999], x[:-1]))
    peaks = (x > l_shift) & (x > r_shift)
    return np.arange(len(x))[peaks]


def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")


exec(input().strip())
