ans = [*input()]
key = [*input()]
if len(ans) != len(key):
    print("Incomplete answer")
else:
    score = 0
    for i in range(len(ans)):
        if ans[i] == key[i]:
            score += 1
    print(score)
