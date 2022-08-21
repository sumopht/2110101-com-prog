from itertools import count


for i in count(0):
    n = input()
    if n == "Zig-Zag" or n == "Zag-Zig":
        if n == "Zig-Zag":
            print(min_x1y2, max_y1x2)
        else:
            print(min_y1x2, max_x1y2)
        break
    else:
        if i % 2 == 0:
            x1y2, y1x2 = n.split()
            x1y2 = int(x1y2)
            y1x2 = int(y1x2)
        elif i % 2 == 1:
            y1x2, x1y2 = n.split()
            x1y2 = int(x1y2)
            y1x2 = int(y1x2)
    if i > 0:
        if max_x1y2 < x1y2:
            max_x1y2 = x1y2
        if min_x1y2 > x1y2:
            min_x1y2 = x1y2

        if max_y1x2 < y1x2:
            max_y1x2 = y1x2
        if min_y1x2 > y1x2:
            min_y1x2 = y1x2
    else:
        max_x1y2 = x1y2
        min_x1y2 = x1y2

        max_y1x2 = y1x2
        min_y1x2 = y1x2
