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
