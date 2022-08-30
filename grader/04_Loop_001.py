p = float(input())
k = 1
t = 1
while 1:
    t = (t * (365 - (k - 1))) / 365
    if 1 - t >= p:
        break
    else:
        k += 1
print(k)
