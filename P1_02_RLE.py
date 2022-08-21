a = input()
if a == "str2RLE":
    b = input()
    count = 0
    print(b[0], end=" ")
    for i in range(len(b)):
        try:
            if b[i] == b[i + 1]:
                count += 1
        except:
            count += 1
        try:
            if b[i] != b[i + 1]:
                count += 1
                print(count, end=" ")
                count = 0
                print(b[i + 1], end=" ")
        except:
            pass
    print(count, end=" ")
elif a == "RLE2str":
    b = input().split()
    # print(b)
    for i in range(len(b)):
        if i % 2 == 0:
            character = b[i]
        else:
            n = int(b[i])
            for i in range(n):
                print(character, end="")
else:
    print("Error")
