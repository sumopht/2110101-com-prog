# a = input()
# b = [*input()]
# sign = ['"', "(", ")", ",", ".", "'"]
# b.replace(sign[0], " ").replace(sign[1], " ").replace(sign[2], " ").replace(
#     sign[3], " "
# ).replace(sign[4], " ").replace(sign[5], " ")
# print(b)

a = input()
b = input()
check = False
sign = ['"', "(", ")", ",", ".", "'"]
for i in range(len(sign)):
    try:
        while 1:
            b.replace(sign[i], " ")
            print(i)
    except:
        pass
print("".join(b))
