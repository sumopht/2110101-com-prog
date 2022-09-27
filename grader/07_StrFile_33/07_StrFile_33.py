file_name = input().strip().split()
students = []
for name in file_name:
    infile = open(f"grader/07_StrFile_33/{name}", "r")  # this file path only work in this repo
    for line in infile:
        sid, gpa = line.strip().split()
        gpa = float(gpa)
        students.append([sid, gpa])
    infile.close()
faculties = []
fsstudents = []  # faculty separated students
for student in students:
    if student[0][8:] not in faculties:
        faculties.append(student[0][8:])
faculties.sort()
fac_dic = dict()
for index in range(len(faculties)):
    fsstudents.append([])
    fac_dic[faculties[index]] = index
for student in students:
    for fac_index in range(len(faculties)):
        if student[0][8:] == faculties[fac_index]:
            fsstudents[fac_index].append(student)
for faculty in fsstudents:
    faculty.sort()
    for student in faculty:
        print(student[0], "{:.2f}".format(student[1]))
