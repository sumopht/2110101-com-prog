def intToChar(a):
    match a:
        case 1:
            return "A"
        case 2:
            return "B"
        case 3:
            return "C"
        case 4:
            return "D"
        case 5:
            return "E"
        case 6:
            return "F"
        case 7:
            return "G"
        case 8:
            return "H"
        case 9:
            return "I"
        case 10:
            return "J"


code = input()
n1 = code[3] + code[10] + code[17] + code[24] + code[31]
n2 = code[7] + code[12] + code[17] + code[22] + code[27]
n3 = int(n1) + int(n2) + 10000
if n3 < 10000:
    n4 = n3[0] + n3[1] + n3[2]
else:
    n4 = n3[1] + n3[2] + n3[3]
n5 = n4 % 10 + 1
n6 = intToChar(n5)
n7 = str(n4) + n6
print(n7)
