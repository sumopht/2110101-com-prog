# I'm a hard coding enthusiast
def order(n):
    return n//2


def find_bot_right(n):
    n = order(n)
    val = 1
    for i in range(1, n + 1):
        val += 8 * i
    return val


def change_direction(list_of_directions, direction_index):
    direction_index += 1
    if direction_index > 3:
        direction_index = 0
    return list_of_directions[direction_index], direction_index


def out_of_map(x, y, n):
    if 0 <= x <= n-1 and 0 <= y <= n-1:
        return False
    else:
        return True


def spiral_square(n):
    bot_right = find_bot_right(n)
    dirs = ('left', 'up', 'right', 'down')
    dir_index = 0
    dir = dirs[dir_index]
    l = [[0 for i in range(n)] for j in range(n)]
    val = bot_right
    x = n - 1
    y = n - 1
    while val > 0:
        l[y][x] = val
        while val > 1:
            if dir == 'left':
                if l[y][x-1] == 0:
                    x -= 1
                    break
                else:
                    dir, dir_index = change_direction(dirs, dir_index)
            elif dir == 'up':
                if l[y-1][x] == 0:
                    y -= 1
                    break
                else:
                    dir, dir_index = change_direction(dirs, dir_index)
            elif dir == 'right':
                if not out_of_map(x+1, y, n) and l[y][x+1] == 0:
                    x += 1
                    break
                else:
                    dir, dir_index = change_direction(dirs, dir_index)
            else:
                if l[y+1][x] == 0:
                    y += 1
                    break
                else:
                    dir, dir_index = change_direction(dirs, dir_index)
        val -= 1
    return l


def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))


exec(input().strip())
