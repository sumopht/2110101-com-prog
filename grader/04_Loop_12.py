n = int(input())
for row in range(n):
    for i in reversed(range(n - (row + 1))):
        print('.', end="")
    print('*', end='')
    if row == n - 1:
        print('*' * (2 * n - 2), end='')
        break
    if row > 0:
        print('.' * (2 * row - 1), end='')
        print('*', end='')
    print()
