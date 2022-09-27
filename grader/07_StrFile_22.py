str1 = input().split()
str2 = input().split()
chars1 = []
for word in str1:
    for char in word:
        chars1.append(char)
chars2 = []
for word in str2:
    for char in word:
        chars2.append(char)
if len(chars1) != len(chars2):
    print('NO')
    exit()
for i in chars2:
    if i.lower() in chars1 or i.upper() in chars1:
        try:
            chars1.remove(i.lower())
        except:
            chars1.remove(i.upper())
    else:
        print('NO')
        exit()
print('YES')
