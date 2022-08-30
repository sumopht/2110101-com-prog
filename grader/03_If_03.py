def findMax(scores):
    max = scores[0]
    for i in range(len(scores)):
        if max < scores[i]:
            max = scores[i]
    return max


def findMin(scores):
    min = scores[0]
    for i in range(len(scores)):
        if min > scores[i]:
            min = scores[i]
    return min


scores = [float(x) for x in input().split()]
scores.remove(findMax(scores))
scores.remove(findMin(scores))
print(round(sum(scores) / 2, 2))
