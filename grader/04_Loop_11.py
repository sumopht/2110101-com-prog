a = input()
count = 0
print(a[0], end=" ")
for i in range(len(a)):
    try:
        if a[i] == a[i + 1]:
            count += 1
    except:
        count += 1
    try:
        if a[i] != a[i + 1]:
            count += 1
            print(count, end=" ")
            count = 0
            print(a[i + 1], end=" ")
    except:
        pass
print(count, end=" ")
