n, m, k = [int(e) for e in input().split()]
graduates_dict = dict()
for i in range(n):
    graduate, faculty = input().split()
    graduates_dict[graduate] = faculty

guests_dict = dict()
for i in range(m):
    s_input = input().split()
    guest = s_input[0]
    graduates = s_input[1:]
    guests_dict[guest] = set()
    for graduate in graduates:
        guests_dict[guest].add(graduates_dict[graduate])

for i in range(k):
    guests = input().split()
    faculties = []
    for guest in guests:
        faculties.append(guests_dict[guest])
    temp = set.intersection(*faculties)

    out = []
    for faculty in temp:
        out.append(faculty)
    out.sort()
    if len(out) != 0:
        print(' '.join(out))
    else:
        print('None')
