# h = int(input("How deep is the well? "))
# u = int(input("How high the frog can jump up? "))
# d = int(input("How far the frog slips down? "))
# frog = 0
# day = 0
# if u <= d and u < h:
#     print("The frog cannot get out of the well.")
# else:
#     while 1:
#         day += 1
#         frog = frog + u
#         if frog >= h:
#             print("The frog gets out of the well on day", day)
#             break
#         frog = frog - d
def shift(a):
    for i in range(len(a) - 1):
        a[i] = a[i + 1]
    del a[-1]
a = [1, 2, 3, 4]
print(a)
shift(a)
print(a)
