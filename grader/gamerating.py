player = {}
for i in range(int(input())):
    data = input().split(' | ')
    mode = data[0]
    if mode[0] == 'Play':
        song = data[1]
        lvl = float(data[2])
        score = float(data[3])
        rating = 25 * (lvl + 1) * (score / 10 ** 7)
        if song not in player:
            player[song] = [lvl, score]
        else:
            if player[song][0] > lvl or player[song][1] > score:

    else:
        if len(data) == 2:
            song = data[1]
        else:
