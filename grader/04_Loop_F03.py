def grade_mcq(sol, ans):
    if len(sol) != len(ans):
        return -1
    score = 0
    for i in range(len(sol)):
        if sol[i] == ans[i]:
            score += 1
    return score


exec(input())
