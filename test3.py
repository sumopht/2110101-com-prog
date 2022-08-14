import math


a, b, c = input().strip().split(",")
if c == "0":
    if b == "":
        number = float(a)
    else:
        number = float(a + "." + b)
    dividend = int(number * (10 ** len(b)))
    divisor = 10 ** len(b)
    print(
        str(int(dividend / math.gcd(dividend, divisor)))
        + " / "
        + str(int(divisor / math.gcd(dividend, divisor)))
    )
else:
    if b == "":
        # number = float(a + "." + c)
        # number3 = float(a)
        number = int(a + c)
        number3 = int(int(a) * (10 ** len(c)))
    else:
        # number = float(a + "." + b + c)
        # number3 = float(a + "." + b)
        number = int(a + b + c)
        number3 = int(int(a + b) * (10 ** len(c)))
    # print("number", number)
    number2 = int(number * (10 ** len(c)))
    # print("number2", number2)
    # print("number3", number3)
    dividend = int(number2 - number3)
    print("dividend:", dividend)
    divisor = int((10 ** len(c)) - 1)
    print("divisor", divisor)
    dividend = int(dividend * (10 ** len(b)) * 2)
    # dividend = int((dividend * (10 ** len(b))) / (10 ** len(b + c)))
    divisor = int(divisor * (10 ** len(b)))
    print("dividend:", dividend)
    print("divisor", divisor)
    # print(
    #     str(int(dividend / math.gcd(dividend, divisor)))
    #     + " / "
    #     + str(int(divisor / math.gcd(dividend, divisor)))
    # )
