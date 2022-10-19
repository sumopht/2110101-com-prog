n = int(input())
data = {}
reversed_data = {}
for i in range(n):
    first, last, value = input().split()
    key = first + ' ' + last
    data[key] = value
    reversed_data[value] = key
n = int(input())
for i in range(n):
    string = input()
    if string in data:
        print(string, '-->', data[string])
    elif string in reversed_data:
        print(string, '-->', reversed_data[string])
    else:
        print(string, '-->', 'Not found')
