a = input()
b = [*input()]
check = False
sign = ['"', "(", ")", ",", ".", "'"]
for i in range(len(sign)):
    try:
        while 1:
            b.remove(sign[i])
    except:
        pass
b = "".join(b).split()
print(b)
count = 0
for i in b:
    if a == i:
        count += 1
print(count)
