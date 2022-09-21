a, b, c, d = [int(x) for x in input().split()]
if a > b:
    a, b = b, a
    if d >= a:
        if c > d:
            c = c - a
    else:
        c = c + a
    b = a + c + d
else:
    if c > a and a >= b:
        d = d + a
    if d > c:
        b = b + 2
    else:
        b = 2 * b
print(a, b, c, d)
