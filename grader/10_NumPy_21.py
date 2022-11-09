import numpy as np


def sum_2_rows(M):
    return M[::2] + M[1::2]


def sum_left_right(M):
    return M[:, :len(M) // 2] + M[:, len(M) // 2:]


def sum_upper_lower(M):
    return M[:len(M) // 2] + M[len(M) // 2:]


def sum_4_quadrants(M):
    return M[:len(M) // 2, :len(M) // 2] + M[:len(M) // 2, len(M) // 2:] + M[len(M) // 2:, :len(M) // 2] + M[len(M) // 2:, len(M) // 2:]


def sum_4_cells(M):
    return sum_2_rows(M)[:, ::2] + sum_2_rows(M)[:, 1::2]


def count_leap_years(years):
    years -= 543
    return sum((years % 4 == 0) & (years % 100 != 0) | (years % 400 == 0))


exec(input().strip())
