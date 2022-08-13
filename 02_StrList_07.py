def intToChar(a):
    if a == 1:
        return "A"
    if a == 2:
        return "B"
    if a == 3:
        return "C"
    if a == 4:
        return "D"
    if a == 5:
        return "E"
    if a == 6:
        return "F"
    if a == 7:
        return "G"
    if a == 8:
        return "H"
    if a == 9:
        return "I"
    if a == 10:
        return "J"


code = input()
n1 = code[3] + code[10] + code[17] + code[24] + code[31]
n2 = code[7] + code[12] + code[17] + code[22] + code[27]
n3 = str(int(n1) + int(n2) + 10000)
if int(n3) < 10000:
    n4 = int(n3[0]) + int(n3[1]) + int(n3[2])
    n4_string = n3[0] + n3[1] + n3[2]
elif int(n3) >= 100000:
    n4 = int(n3[2]) + int(n3[3]) + int(n3[4])
    n4_string = n3[2] + n3[3] + n3[4]
else:
    n4 = int(n3[1]) + int(n3[2]) + int(n3[3])
    n4_string = n3[1] + n3[2] + n3[3]
n5 = n4 % 10 + 1
n6 = intToChar(n5)
n7 = str(n4_string) + n6
print(n7)
