def splt(s):
    after_splt = []
    previous = -1
    for i in range(len(s)):
        if s[i] == '/':
            after_splt.append(s[previous + 1:i])
            previous = i
    if s[-1] != '/':
        after_splt.append(s[previous + 1:])
    else:
        after_splt.append('')

    return after_splt


def check(a, b):
    if len(a) != len(b):
        return False
    else:
        for i in range(len(a)):
            if a[i] == '?':
                continue
            elif a[i].lower() != b[i].lower():
                return False
    return True


folder = input()
name = input()
new_name = input()
f = open(folder, 'r')
for line in f:
    words = splt(line)
    for index in range(len(words)):
        if check(name, words[index]) == True:
            try:
                if words[index + 1] != None:
                    words[index] = new_name
            except:
                pass
    for count in range(len(words)):
        print(words[count], end='')
        if count != len(words) - 1:
            print('/', end='')
