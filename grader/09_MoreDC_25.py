def row_number(t, e):
    for list in t:
        if e in list:
            return t.index(list)


def flatten(t):
    flattened_list = []
    for list in t:
        for element in list:
            if element == 0:
                continue
            flattened_list.append(element)
    return flattened_list


def inversions(x):
    inversion = 0
    for index in range(len(x)):
        for element in x[index:]:
            if x[index] > element:
                inversion += 1
    return inversion


def solvable(t):
    if len(t) % 2 == 0:
        if inversions(flatten(t)) % 2 == 0:
            if row_number(t, 0) % 2 == 0:
                return False
            else:
                return True
        else:
            if row_number(t, 0) % 2 == 0:
                return True
            else:
                return False
    else:
        if inversions(flatten(t)) % 2 == 0:
            return True
        else:
            return False


exec(input().strip())
