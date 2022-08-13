v1 = list(map(float, input().strip("[]").split(",")))
v2 = list(map(float, input().strip("[]").split(",")))
v3 = [0] * 3
v3[0] = v1[0] + v2[0]
v3[1] = v1[1] + v2[1]
v3[2] = v1[2] + v2[2]
print(v1, "+", v2, "=", v3)
