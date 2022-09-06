def cut(a):
    before = []
    after = []
    for i in range(len(a)):
        if i <= len(a) / 2 - 1:
            before.append(a[i])
        else:
            after.append(a[i])
    a = after + before
    return a


def shuffle(a):
    amount = len(a)
    half = amount / 2
    temp = []
    for i in range(0, int(half)):
        temp.append(a[i])
        temp.append(a[i + int(half)])
    return temp


orders = input().split()
process = input()
for i in process:
    if i == 'C':
        orders = cut(orders)
    elif i == 'S':
        orders = shuffle(orders)
    else:
        continue
print(' '.join(orders))
