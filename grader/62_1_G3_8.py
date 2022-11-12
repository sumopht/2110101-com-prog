parties = {}
sorted_parties = []
for i in range(int(input())):
    party = input()
    parties[party] = {}
    sorted_parties.append(party)
sorted_parties.sort()
# print(parties)
for i in range(int(input())):
    name, party = input().split()
    parties[party][name] = 'Z'
# print(parties)
for i in range(int(input())):
    name, vote = input().split()
    for party in parties:
        if name in parties[party]:
            parties[party][name] = vote


for party in parties:
    print(party)

    scores = {'Y': 0, 'N': 0, 'X': 0}
    for name in parties[party]:
        if parties[party][name] == 'Y':
            scores['Y'] += 1
        elif parties[party][name] == 'N':
            scores['N'] += 1
        elif parties[party][name] == 'X':
            scores['X'] += 1
    cobra = []
    # if scores['X'] > scores['N'] and scores['X'] > scores['Y']:
    #     result = 'X'
    #     for name in parties[party]:
    #         if parties[party][name] != result:
    #             cobra.append(name)
    if (scores['Y'] > scores['X'] and scores['N'] > scores['X'] and scores['Y'] == scores['N']) or (scores['Y'] > scores['N'] and scores['X'] > scores['N'] and scores['Y'] == scores['X']) or (scores['N'] > scores['Y'] and scores['X'] > scores['Y'] and scores['N'] == scores['X']):
        result = 'Inconclusive'
        print(result)
        continue
    elif scores['X'] > scores['N'] and scores['X'] > scores['Y']:
        result = 'X'
        for name in parties[party]:
            if parties[party][name] != result:
                cobra.append(name)
    elif scores['Y'] > scores['N']:
        result = 'Y'
        for name in parties[party]:
            if parties[party][name] != result and parties[party][name] != 'Z':
                cobra.append(name)
    elif scores['Y'] < scores['N']:
        result = 'N'
        for name in parties[party]:
            if parties[party][name] != result and parties[party][name] != 'Z':
                cobra.append(name)
    cobra.sort()

    if len(cobra) == 0:
        print('No cobra')
    else:
        print(', '.join(cobra))
