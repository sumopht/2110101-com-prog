def f1(a, b, c):
    min = 1001
    if a > 0:
        min = a
    if b > 0:
        if b < min:
            min = b
    if c > 0:
        if c < min:
            min = c
    return min


def f2(a, b, c):
    max = -1001
    if a < 0:
        max = a
    if b < 0:
        if b > max:
            max = b
    if c < 0:
        if c > max:
            max = c
    return max


def f3(a, b, c):
    sum = a + b + c
    if sum < 0:
        sum = sum * -1
    sum2 = str(sum)
    return int(sum2[0])


def f4(a, b, c):
    sum = a + b + c
    if sum < 0:
        sum = sum * -1
    sum2 = str(sum)
    return int(sum2[-1])


def main():
    s1, s2, a, b, c = [int(e) for e in input().split()]
    if s1 == 0 and s2 == 0:
        print(f1(a, b, c))
    elif s1 == 0 and s2 == 1:
        print(f2(a, b, c))
    elif s1 == 1 and s2 == 0:
        print(f3(a, b, c))
    elif s1 == 1 and s2 == 1:
        print(f4(a, b, c))
    else:
        print('Error')


exec(input().strip())  # DON'T remove this line
