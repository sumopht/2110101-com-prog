<<<<<<< HEAD
def splitt(s):
    data = []
    previous = -1
    for i in range(len(s)):
        if s[i] == '/':
            data.append(s[previous + 1:i])
            previous = i
    if s[-1] != '/':
        data.append(s[previous + 1:len(s) - 1])
    return data


# print(splitt('c:/temp/exam.py'))
file = input()
name = input()
new_name = input()
f = open(file, 'r')
for line in f:
    data = splitt(line)
    for i in range(len(data)):
        if data[i].lower() == name.lower():
            data[i] = name
    ans = ''
    for i in data:
        ans += '/' + i
    print(ans)


# print('c:/Python/exam.py')
# print('d:/abc/Python/doc/temp.txt')
# print('/Python/doc/Python/quiz.xls')
# print('Python/temp.py')
# print('temp')
# print('/temp')
# print('/Python/')
# c:/Python/exam.py
# d:/abc/Python/doc/temp.txt
# /Python/doc/Python/quiz.xls
# Python/temp.py
# temp
# /temp
# /Python/
=======
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
>>>>>>> de3ee685011f337bcd3ee9b68a2508ccd0b4a81b
