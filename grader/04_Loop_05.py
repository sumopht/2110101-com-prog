a = input()
b = input()
sign = ['"', "(", ")", ",", ".", "'"]
for i in range(len(sign)):
    b = b.replace(sign[i], " ")
b = "".join(b).split()
count = 0
for i in b:
    if a == i:
        count += 1
print(count)
