def q(grade):
    if grade == "F":
        grade = "D"
    elif grade == "D":
        grade = "D+"
    elif grade == "D+":
        grade = "C"
    elif grade == "C":
        grade = "C+"
    elif grade == "C+":
        grade = "B"
    elif grade == "B":
        grade = "B+"
    else:
        grade = "A"
    return grade


ids = []
grades = []
while 1:
    try:
        id, grade = input().split()
    except:
        break
    ids.append(id)
    grades.append(grade)
uids = input().split()
for uid in uids:
    index = ids.index(uid)
    grades[index] = q(grades[index])
temp_grades = {}
for i in range(len(ids)):
    temp_grades[ids[i]] = grades[i]
ordered_grades = sorted(temp_grades.items())
for i in ordered_grades:
    print(" ".join(i))
