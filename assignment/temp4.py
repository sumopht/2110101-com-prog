RESET = '\033[0m'
RED = '\033[;31m'
GREEN = '\033[;32m'
BLUE = '\033[;34m'
HIGHLIGHT = '\033[;103m'

t = 'ACdeFGAhiJKLNoDOGpqRStUvWYz'
w = ['a', 'U', 'Z', 'vw', 'dog']
t_lower = t.lower()
w_lower = [x.lower() for x in w]
index = []
for i in w_lower:
    last_index = -1
    while 1:
        current_index = t_lower.find(i, last_index + 1)
        if current_index == -1:
            break
        index.append([current_index, len(i)])
        last_index = current_index
for i, char in enumerate(t):
    for order in index:
        if order[0] == i:
            print(HIGHLIGHT, end='')
            current_index = i
            reset_index = i + order[1]
    if i == reset_index:
        print(RESET, end='')
    print(char, end='')
print(RESET)
