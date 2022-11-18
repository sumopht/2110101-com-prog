n = int(input())
A = []
B = []

for i in range(n):
    if i % 2 == 0:
        a, b = [int(e) for e in input().split()]
    else:
        b, a = [int(e) for e in input().split()]

    A.append(a)
    B.append(b)

mode = input()
if mode == 'Zig-Zag':
    print(min(A), max(B))
else:
    print(min(B), max(A))
