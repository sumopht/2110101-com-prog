subs = int(input())
if subs >= 1000000000:
    subs = subs / 1000000000
    if subs < 10:
        print(str(round(subs, 1)) + "B")
    else:
        print(str(round(subs)) + "B")
elif subs >= 1000000:
    subs = subs / 1000000
    if subs < 10:
        print(str(round(subs, 1)) + "M")
    else:
        print(str(round(subs)) + "M")
elif subs >= 1000:
    subs = subs / 1000
    if subs < 10:
        print(str(round(subs, 1)) + "K")
    else:
        print(str(round(subs)) + "K")
else:
    print(subs)
