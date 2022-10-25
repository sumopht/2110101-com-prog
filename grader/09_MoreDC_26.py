data = dict()
for i in range(int(input())):
    id, city = input().split(': ')
    data[id] = set(city.split(', '))
keyID = input()
valid_id = []
for id in data:
    if len(data[id] & data[keyID]) != 0:
        valid_id.append(id)
valid_id.remove(keyID)
if len(valid_id) == 0:
    print('Not Found')
else:
    [print(a) for a in valid_id]
