import math


def less(a, b):
    if a < b:
        return a
    else:
        return b


par = []
stroke = []
status = []
for i in range(9):
    par_temp, stroke_temp, status_temp = [int(x) for x in input().split()]
    par.append(par_temp)
    stroke.append(stroke_temp)
    status.append(status_temp)
stroke_fix = []
for i in range(9):
    if status[i]:
        stroke_fix.append(less(stroke[i], par[i] + 2))
handicap = math.floor(0.8 * (1.5 * sum(stroke_fix) - sum(par)))
score = sum(stroke) - handicap
print(sum(stroke))
print(handicap)
print(score)
