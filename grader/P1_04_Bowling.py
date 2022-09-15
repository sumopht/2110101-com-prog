def convert(c):
    return 10 if not ("0" <= c <= "9") else int(c)


s = input()
n = int(input())
score = [0 for e in range(10)]
inx = 0
i = 0
total = 0
while (i < len(s)):
    if inx == 9:
        for j in range(i, len(s)):
            score[inx] += convert(s[j])
            if (s[j] == '/'):
                score[inx] -= convert(s[j-1])
        for j in score:
            total += j
        break
    else:
        if s[i] == 'X':
            score[inx] = 10 + convert(s[i+1]) + convert(s[i+2])
            if s[i+2] == '/':
                score[inx] -= convert(s[i+1])
            inx += 1
            i += 1
        else:
            score[inx] += convert(s[i]) + convert(s[i+1]) + (convert(s[i+2]) if s[i+1] == '/' else 0)
            if s[i+1] == '/':
                score[inx] -= convert(s[i])
            inx += 1
            i += 2

print("{}".format(score[n-1] if 1 <= n <= 10 else total))
