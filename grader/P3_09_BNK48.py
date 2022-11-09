votes = []
while 1:
    temp = input().split()
    try:
        votes.append([temp[0], temp[1], int(temp[2])])
    except:
        form = int(temp[0])
        break
if form == 1:
    members = {}
    for vote in votes:
        if vote[1] in members:
            members[vote[1]] += vote[2]
        else:
            members[vote[1]] = vote[2]
    scores = []
    sorted_members = []
    for member in members:
        scores.append(members[member])
        sorted_members.append(member)
    scores.sort(reverse=True)
    sorted_members.sort()
    out = []
    for score in scores:
        for member in sorted_members:
            if members[member] == score:
                out.append(member)
                sorted_members.remove(member)
                break
    print(', '.join(out[:3]))
elif form == 2:
    members = {}
    counts = set()
    for vote in votes:
        counts.add((vote[1], vote[0]))
    for count in counts:
        if count[0] in members:
            members[count[0]] += 1
        else:
            members[count[0]] = 1
    scores = []
    sorted_members = []
    for member in members:
        scores.append(members[member])
        sorted_members.append(member)
    scores.sort(reverse=True)
    sorted_members.sort()
    out = []
    for score in scores:
        for member in sorted_members:
            if score == members[member]:
                out.append(member)
                sorted_members.remove(member)
                break
    print(', '.join(out[:3]))
else:
    otas = {}
    kamis = {}
    for vote in votes:
        if vote[0] not in otas:
            otas[vote[0]] = {vote[1]: vote[2]}
        else:
            if vote[1] in otas[vote[0]]:
                otas[vote[0]][vote[1]] += vote[2]
            else:
                otas[vote[0]][vote[1]] = vote[2]
        kamis[vote[1]] = 0
    for ota in otas:
        scores = []
        sorted_members = []
        for member in otas[ota]:
            scores.append(otas[ota][member])
            sorted_members.append(member)

        scores.sort(reverse=True)
        sorted_members.sort()
        find_again = False
        for score in scores:
            for member in sorted_members:
                if score == otas[ota][member]:
                    if member in kamis:
                        kamis[member] += 1
                        break
                    else:
                        kamis[member] = 1
                        break
            break
    sorted_members = []
    scores = []
    for kami in kamis:
        scores.append(kamis[kami])
        sorted_members.append(kami)
    scores.sort(reverse=True)
    sorted_members.sort()
    out = []
    for score in scores:
        for member in sorted_members:
            if score == kamis[member]:
                out.append(member)
    print(', '.join(out[:3]))
