n = int(input())
data = {}
for i in range(n):
    key, value = input().split()
    data[key] = int(value)

n = int(input())
sales = {}
icecream_sales = {}
total_sales = 0
for i in range(n):
    key, value = input().split()
    if key in data:
        if key in icecream_sales:
            icecream_sales[key] += float(int(value) * data[key])
        else:
            icecream_sales[key] = float(int(value) * data[key])

if len(icecream_sales) == 0:
    print('No ice cream sales')
else:
    top_sales = max(icecream_sales.values())
    top = []
    for key in icecream_sales:
        if icecream_sales[key] == top_sales:
            top.append(key)
    top.sort()
    print('Total ice cream sales:', sum(icecream_sales.values()))
    print('Top sales:', ', '.join(top))
