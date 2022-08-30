def choose(stu1, stu2):
    id1 = str(stu1[0])
    id2 = str(stu2[0])
    gpax1 = float(stu1[1])
    gpax2 = float(stu2[1])
    comp1 = str(stu1[2])
    comp2 = str(stu2[2])
    cal11 = str(stu1[3])
    cal12 = str(stu2[3])
    cal21 = str(stu1[4])
    cal22 = str(stu2[4])
    if (comp1 != "A" or cal11 > "C" or cal21 > "C") and (
        comp2 != "A" or cal12 > "C" or cal22 > "C"
    ):
        return []
    elif (comp1 != "A" or cal11 > "C" or cal21 > "C") and (
        comp2 == "A" and cal12 <= "C" and cal22 <= "C"
    ):
        return [id2]
    elif (comp1 == "A" and cal11 <= "C" and cal21 <= "C") and (
        comp2 != "A" or cal12 > "C" or cal22 > "C"
    ):
        return [id1]
    else:
        if gpax1 == gpax2:
            if cal11 == cal12:
                if cal21 == cal21:
                    return [id1, id2]
                else:
                    if cal21 < cal22:
                        return [id1]
                    else:
                        return [id2]
            else:
                if cal11 < cal12:
                    return [id1]
                else:
                    return [id2]
        else:
            if gpax1 > gpax2:
                return [id1]
            else:
                return [id2]


exec(input())  # DON'T remove this line
