teams = {}
n = int(input())
for i in range(n):
    team, country = input().split()
    teams[team] = country
# print(teams)
while 1:
    status = 'OK'
    s_input = input()
    if s_input == 'q':
        quit()
    group = s_input.split()
    countries_in_group = []
    for team in group:
        if team not in teams:
            print('Not OK')
            status = 'Not OK'
            break
        else:
            # if teams[team] not in countries_in_group:
            #     countries_in_group.append(teams[team])
            # else:
            #     print('Not OK')
            #     status = 'Not OK'
            #     break
            if teams[team] in countries_in_group:
                print('Not OK')
                status = 'Not OK'
                break
            else:
                countries_in_group.append(teams[team])

    if status == 'OK':
        print('OK')
