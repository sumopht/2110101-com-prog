def shift(a):
    for i in range(len(a) - 1):
        a[i] = a[i + 1]
    del a[-1]


def diffTime(a, b):
    return int(b) - int(a)


q = list()
t = list()
output = list()
qtime = list()
n = int(input())
for k in range(n):
    c = input().split()
    if c[0] == 'reset':
        reset = c[1]
        reset_status = False
    elif c[0] == 'new':
        if reset_status == False:
            q.append(int(reset))
            reset_status = True
        elif len(q) == 0:
            q.append(justCalled + 1)
        else:
            q.append(q[len(q) - 1] + 1)
        print("ticket", q[len(q) - 1])
        t.append(c[1])
    elif c[0] == 'next':
        print("call", q[0])
        justCalled = q[0]
        justCalledTime = t[0]
        shift(q)
        shift(t)
    elif c[0] == 'order':
        waitTime = diffTime(justCalledTime, c[1])
        print("qtime", justCalled, waitTime)
        qtime.append(waitTime)
    elif c[0] == 'avg_qtime':
        print("avg_qtime", round(sum(qtime) / len(qtime), 4))
