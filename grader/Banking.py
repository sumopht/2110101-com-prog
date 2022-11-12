accounts = {}
for i in range(int(input())):
    datas = input().split()
    accounts[datas[1]] = [datas[0], float(datas[2])]
# print(accounts)
while 1:
    datas = input().split()
    if datas[0] == 'exit':
        break
    # [name, id, mode, amount]
    # [name, id, mode, receiver_id, amount]
    name = datas[0]
    id = datas[1]
    mode = datas[2]
    amount = float(datas[-1])
    if mode == 'deposit':
        if id in accounts:
            if accounts[id][0] == name:
                accounts[id][1] += amount
            else:
                print('Transaction Failed')
                continue
        else:
            accounts[id] = [name, amount]
    elif mode == 'withdraw':
        if id in accounts:
            if accounts[id][0] == name:
                if accounts[id][1] >= amount:
                    accounts[id][1] -= amount
                else:
                    print('Transaction Failed')
                    continue
            else:
                print('Transaction Failed')
                continue
        else:
            print('Transaction Failed')
            continue
    if mode == 'transfer':
        id_receiver = datas[3]
        if id in accounts:
            if accounts[id][0] == name:
                if accounts[id][1] >= amount:
                    if id_receiver in accounts:
                        accounts[id_receiver][1] += amount
                    else:
                        print('Transaction Failed')
                        continue
                    accounts[id][1] -= amount
                else:
                    print('Transaction Failed')
                    continue
            else:
                print('Transaction Failed')
                continue
        else:
            print('Transaction Failed')
            continue
        print(accounts[id][0], '(' + id + ')', str(accounts[id][1]))
        print(accounts[id_receiver][0], '(' + id_receiver + ')', str(accounts[id_receiver][1]))
        continue
    print(accounts[id][0], '(' + id + ')', str(accounts[id][1]))

# 2
# computer.pro 0123456789 40000.32
# apple.str 0089553714 0
# computer.pro 0123456789 transfer 0089553714 40
# computer.rop 0123456789 deposit 10
# computer.pro 5555555555 deposit 10
# exit
