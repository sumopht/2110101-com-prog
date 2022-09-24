a = input()
b = a.replace('+', ' ').replace('-', ' ').split()
c = []
for i in a:
    if i == '+' or i == '-':
        c.append(i)
value = 0
if len(c) == len(b):
    for i in range(len(b)):
        value = value + int((c[i]) + b[i])
else:
    for i in range(len(b)):
        if i == 0:
            value = value + int(b[i])
        else:
            value = value + int((c[i - 1]) + b[i])
print(value)
