# 100/100 but not usable!

student1 = input().split()
student2 = input().split()

if student1[2] != "A":
    if student2[2] != "A":
        print("None")
    else:
        if (student2[3] == "D" or student2[3] == "F") or (
            student2[4] == "D" or student2[4] == "F"
        ):
            print("None")
        else:
            print(student2[0])
    exit()
else:
    if student2[2] != "A":
        print(student1[0])
        exit()

if (student1[3] == "D" or student1[3] == "F") or (
    student1[4] == "D" or student1[4] == "F"
):
    if (student2[3] == "D" or student2[3] == "F") or (
        student2[4] == "D" or student2[4] == "F"
    ):
        print("None")
    else:
        print(student2[0])
    exit()
else:
    if (student2[3] == "D" or student2[3] == "F") or (
        student2[4] == "D" or student2[4] == "F"
    ):
        print(student1[0])
        exit()

if student1[1] == student2[1]:
    if student1[3] == student2[3]:
        if student1[4] == student2[4]:
            print("Both")
        else:
            if student1[4] < student2[4]:
                print(student1[0])
            else:
                print(student2[0])
    else:
        if student1[3] < student2[3]:
            print(student1[0])
        else:
            print(student2[0])
else:
    if student1[1] > student2[1]:
        print(student1[0])
    else:
        print(student2[0])
