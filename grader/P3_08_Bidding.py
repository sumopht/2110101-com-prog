products = {}
out = {}
for i in range(int(input())):
    info = input().split()
    try:
        info[3] = int(info[3])
    except:
        pass
    out[info[1]] = [0, []]
    if info[0] == 'B':
        if info[2] not in products:  # info[2] is product name
            products[info[2]] = [(info[1], info[3])]
        else:
            for bid in products[info[2]]:
                if bid[0] == info[1]:
                    products[info[2]].remove((bid[0], bid[1]))
            products[info[2]].append((info[1], info[3]))
    elif info[0] == 'W':
        for bid in products[info[2]]:
            if bid[0] == info[1]:
                products[info[2]].remove((bid[0], bid[1]))
    else:
        continue

for product in products:
    prices = []
    for bid in products[product]:
        prices.append(bid[1])
    for bid in products[product]:
        if bid[1] == max(prices):  # bid[0] is name, bid[1] is price
            out[bid[0]][0] += bid[1]
            out[bid[0]][1].append(product)
            break
for person in sorted(out):
    if out[person][0] != 0:
        print(person + ': $' + str(out[person][0]) + ' -> ' + ' '.join(sorted(out[person][1])))
    else:
        print(person + ': $0')
