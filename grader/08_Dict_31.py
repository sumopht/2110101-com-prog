def total(pocket):
    sum = 0
    for key in pocket:
        sum += key * pocket[key]
    return sum


def take(pocket, money_in):
    for key in money_in:
        if key in pocket:
            pocket[key] += money_in[key]
        else:
            pocket[key] = money_in[key]
    return pocket


def pay(pocket, amt):
    typeOfBank = []
    for key in pocket:
        typeOfBank.append(key)
    typeOfBank.sort(reverse=True)
    pay_pocket = {}
    temp = dict(pocket)
    for type in typeOfBank:
        while 1:
            if type > amt or pocket[type] == 0:
                break
            if type in pay_pocket:
                pay_pocket[type] += 1
            else:
                pay_pocket[type] = 1
            amt -= type
            pocket[type] -= 1
    if amt == 0:
        return pay_pocket
    else:
        for key in pocket:
            pocket[key] = temp[key]
        return {}


exec(input().strip())
