import math


def isLeapYear(year):
    year = year - 543  # convert form B.E. to A.D.
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 100 != 0 and year % 4 == 0:
        return True
    return False


def countRed(d, m, y):
    if m == 1:
        if isLeapYear(y):
            return (
                335 + (31 - d) + 1
            )  # days(2th month to 12th month) + days before 1st month end
        else:
            return 334 + (31 - d) + 1
    elif m == 2:
        if isLeapYear(y):
            return 306 + (29 - d) + 1
        else:
            return 306 + (28 - d) + 1
    elif m == 3:
        return 275 + (31 - d) + 1
    elif m == 4:
        return 245 + (30 - d) + 1
    elif m == 5:
        return 214 + (31 - d) + 1
    elif m == 6:
        return 184 + (30 - d) + 1
    elif m == 7:
        return 153 + (31 - d) + 1
    elif m == 8:
        return 122 + (31 - d) + 1
    elif m == 9:
        return 92 + (30 - d) + 1
    elif m == 10:
        return 61 + (31 - d) + 1
    elif m == 11:
        return 31 + (30 - d) + 1
    else:
        return 0 + (31 - d) + 1


def countBlack(by, y):
    return 365 * (y - by - 1)


def countBlue(d, m, y):
    if m == 1:
        return d - 1
    elif m == 2:
        return d + 31 - 1
    elif m == 3:
        if isLeapYear(y):
            return d + 60 - 1
        else:
            return d + 60 - 1 - 1
    elif m == 4:
        if isLeapYear(y):
            return d + 91 - 1
        else:
            return d + 91 - 1 - 1
    elif m == 5:
        if isLeapYear(y):
            return d + 121 - 1
        else:
            return d + 121 - 1 - 1
    elif m == 6:
        if isLeapYear(y):
            return d + 152 - 1
        else:
            return d + 152 - 1 - 1
    elif m == 7:
        if isLeapYear(y):
            return d + 182 - 1
        else:
            return d + 182 - 1 - 1
    elif m == 8:
        if isLeapYear(y):
            return d + 213 - 1
        else:
            return d + 213 - 1 - 1
    elif m == 9:
        if isLeapYear(y):
            return d + 244 - 1
        else:
            return d + 244 - 1 - 1
    elif m == 10:
        if isLeapYear(y):
            return d + 274 - 1
        else:
            return d + 274 - 1 - 1
    elif m == 11:
        if isLeapYear(y):
            return d + 305 - 1
        else:
            return d + 305 - 1 - 1
    elif m == 12:
        if isLeapYear(y):
            return d + 335 - 1
        else:
            return d + 335 - 1 - 1


bd, bm, by, d, m, y = [int(e) for e in input().split()]

days = countRed(bd, bm, by) + countBlack(by, y) + countBlue(d, m, y)
physical = math.sin((2 * math.pi * days) / (23))
emotional = math.sin((2 * math.pi * days) / (28))
intellectual = math.sin((2 * math.pi * days) / (33))
print(
    days,
    "{:.2f}".format(physical),
    "{:.2f}".format(emotional),
    "{:.2f}".format(intellectual),
)
