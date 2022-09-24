a = [*input()]
check = 0
a.replace('(', '[')
# while 1:
#     if a.find('(') == -1:
#         check += 1
#         print('1')
#     else:
#         a.replace('(', '[')
#         print(a)
#     if a.find('[') == -1:
#         check += 1
#     else:
#         a.replace('[', '(')
#     if a.find(')') == -1:
#         check += 1
#     else:
#         a.replace(')', ']')
#     if a.find(']') == -1:
#         check += 1
#     else:
#         a.replace(']', ')')
#     if check == 4:
#         break
print(a)
