x = [int(e) for e in input().split()]
k = int(input())
count = 0
dup = []
for i in range(len(x)):
    if i == 0:
        count += 1
    else:
        if x[i] == x[i - 1]:
            count += 1
        else:
            if count >= k:
                for j in range(count):
                    dup.append(x[i - 1])
            count = 1
        if i == len(x) - 1:
            if count >= k:
                for j in range(count):
                    dup.append(x[i - 1])
for i in dup:
    x.remove(i)
print(sum(x))
