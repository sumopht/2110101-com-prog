n = int(input())
a = []
for i in range(n):
    a.append(set(input().split()))
try:
    print(len(set.union(*a)))
    print(len(set.intersection(*a)))
except:
    print(0)
    print(0)
