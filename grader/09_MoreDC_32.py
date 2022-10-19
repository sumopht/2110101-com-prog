def first_fit(L, e):
    is_append = False
    for l in L:
        if sum(l) + e <= 100:
            l.append(e)
            is_append = True
            break
    if not is_append:
        L.append([e])
    return L


def best_fit(L, e):
    best_index = -1
    previous_sum = 0
    for index, l in enumerate(L):
        current_sum = sum(l) + e
        if current_sum <= 100 and current_sum > previous_sum:
            best_index = index
            previous_sum = current_sum
    if best_index != -1:
        L[best_index].append(e)
    else:
        L.append([e])
    return L


def partition_FF(D):
    part = []
    for num in D:
        part = first_fit(part, num).copy()
    return part


def partition_BF(D):
    part = []
    for num in D:
        part = best_fit(part, num).copy()
    return part


exec(input().strip())
