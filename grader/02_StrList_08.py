import math


a, b, c = input().strip().split(",")
if b == "":
    dividend = int(c)
else:
    dividend = int(b + c) - int(b)
nine = zero = ""
for i in range(len(c)):
    nine = nine + "9"
for i in range(len(b)):
    zero = zero + "0"
divisor = int(nine + zero)
dividend = divisor * int(a) + dividend
gcd = int(math.gcd(dividend, divisor))
dividend = int(dividend // gcd)
divisor = int(divisor // gcd)
print(dividend, "/", divisor)
