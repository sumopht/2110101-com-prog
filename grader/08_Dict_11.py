def reverse(d):
    re = {}
    for key in d:
        re[d[key]] = key
    return re


def keys(d, v):
    ans = []
    for key in d:
        if d[key] == v:
            ans.append(key)
    return ans


exec(input().strip())
