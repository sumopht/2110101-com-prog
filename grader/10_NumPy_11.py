import numpy as np


def get_column_from_bottom_to_top(A, c):
    return A[::-1, c]


def get_odd_rows(A):
    return A[1::2]


def get_even_column_last_row(A):
    return A[-1, ::2]


def get_diagonal1(A):
    temp = np.array([])
    for i in range(len(A)):
        temp = np.append(temp, A[i, i])
    return temp.astype(int)


def get_diagonal2(A):
    temp = np.array([])
    for i, j in zip(range(len(A)), range(len(A))[::-1]):
        temp = np.append(temp, A[i, j])
    return temp.astype(int)


exec(input().strip())
