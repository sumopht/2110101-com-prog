def isLeapYear(year):
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 100 != 0 and year % 4 == 0:
        return True
    return False


def BEtoAD(year):
    return year - 543


def count(date, month, year):
    if month == 1:
        return date
    elif month == 2:
        return date + 31
    elif month == 3:
        if isLeapYear(BEtoAD(year)):
            return date + 60
        else:
            return date + 60 - 1
    elif month == 4:
        if isLeapYear(BEtoAD(year)):
            return date + 91
        else:
            return date + 91 - 1
    elif month == 5:
        if isLeapYear(BEtoAD(year)):
            return date + 121
        else:
            return date + 121 - 1
    elif month == 6:
        if isLeapYear(BEtoAD(year)):
            return date + 152
        else:
            return date + 152 - 1
    elif month == 7:
        if isLeapYear(BEtoAD(year)):
            return date + 182
        else:
            return date + 182 - 1
    elif month == 8:
        if isLeapYear(BEtoAD(year)):
            return date + 213
        else:
            return date + 213 - 1
    elif month == 9:
        if isLeapYear(BEtoAD(year)):
            return date + 244
        else:
            return date + 244 - 1
    elif month == 10:
        if isLeapYear(BEtoAD(year)):
            return date + 274
        else:
            return date + 274 - 1
    elif month == 11:
        if isLeapYear(BEtoAD(year)):
            return date + 305
        else:
            return date + 305 - 1
    elif month == 12:
        if isLeapYear(BEtoAD(year)):
            return date + 335
        else:
            return date + 335 - 1


date = int(input())
month = int(input())
year = int(input())

print(count(date, month, year))
