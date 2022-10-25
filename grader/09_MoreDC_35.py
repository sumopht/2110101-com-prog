data = dict()
for i in range(int(input())):
    temp = input().split()
    data[temp[0]] = tuple(temp[1:])
key = input().split()
valid = list()
for person in data:
    if set(key).issubset(data[person]):
        valid.append([person] + list(data[person]))
if len(valid) == 0:
    print('Not Found')
else:
    [print(' '.join(x)) for x in sorted(valid)]
