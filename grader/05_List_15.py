a = [int(x) for x in input().split()]
a.sort()
b = []
count = 0
for i in a:
    if count == 0:
        b.append(i)
        count += 1
    if i == b[count - 1]:
        continue
    else:
        b.append(i)
        count += 1
print(len(b))
print(b[0:10])
