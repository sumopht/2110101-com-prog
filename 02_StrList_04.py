m = input()
n = int(input())
d = n - len(m)
if d > 0:
    print("0" * d, end="")
print(m)
