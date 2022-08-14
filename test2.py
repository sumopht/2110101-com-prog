a, b, c = input().strip().split(",")
# print("a:", a)
# print("b:", b)
# print("c:", int(c))
# a = input()
# print(float(a))
# 82379831204982398023982937498723270
if b == "":
    number = float(a + "." + c)
    number3 = float(a)
    # number = int(a + c) * (10 ** len(b + c))
    # number3 = int(a) * (10 ** len(b + c))
    number = int(a + b + c) * (10 ** len(b + c))
else:
    number = float(a + "." + b + c)
    number3 = float(a + "." + b)
    # number = int(a + b + c) * (10 ** len(b + c))
    # number3 = int(a) * (10 ** len(b + c))
print(number)
