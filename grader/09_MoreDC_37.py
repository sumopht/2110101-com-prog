major = dict()
for i in range(int(input())):
    temp = input().split()
    major[temp[0]] = int(temp[1])
student = dict()
for i in range(int(input())):
    temp = input().split()
    student[float(temp[1])] = temp[0], temp[2:]
sortedScore = sorted(student, reverse=True)
ans = []
for score in sortedScore:
    for mj in student[score][1]:
        if major[mj] != 0:
            ans.append([student[score][0], mj])
            major[mj] -= 1
            break
        else:
            continue
[(print(' '.join(x))) for x in sorted(ans)]
