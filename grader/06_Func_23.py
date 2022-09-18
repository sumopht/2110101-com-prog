def make_int_list(x):
    a = x.split()
    return [int(r) for r in a]


def is_odd(e):
    if e % 2 == 1:
        return True
    else:
        return False


def odd_list(alist):
    blist = []
    for i in alist:
        if is_odd(i):
            blist.append(i)
    return blist


def sum_square(alist):
    sum = 0
    for i in alist:
        sum = sum + i ** 2
    return sum


exec(input().strip())
