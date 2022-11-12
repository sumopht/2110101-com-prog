countries_group = []
enemy_of_countries = {}

while 1:
    s_input = input().split()

    if s_input[0] == 'End':
        break

    elif s_input[0] == 'Ally':
        allies = s_input[1:]
        allies_list = []
        for ally in allies:
            allies_list.append(ally)
        countries_group.append(allies_list)

    elif s_input[0] == 'Enemy':
        have_group_1 = False
        have_group_2 = False
        country1, country2 = s_input[1], s_input[2]
        for group in countries_group:
            if country1 in group:
                have_group_1 = True
            if country2 in group:
                have_group_2 = True

        if have_group_1 == False:
            countries_group.append([country1])
        if have_group_2 == False:
            countries_group.append([country2])

        for group in countries_group:
            for country in group:
                if country not in enemy_of_countries:
                    enemy_of_countries[country] = set()

        for group in countries_group:
            if country1 in group:
                index1 = countries_group.index(group)
            if country2 in group:
                index2 = countries_group.index(group)

        for country in countries_group[index1]:
            enemy_of_countries[country].update(countries_group[index2])

        for country in countries_group[index2]:
            enemy_of_countries[country].update(countries_group[index1])

    elif s_input[0] == 'Table':
        table_order = [s_input[-1]] + s_input[1:] + [s_input[1]]
        valid = True
        for i in range(1, len(table_order) - 1):
            left_country = table_order[i - 1]
            me_country = table_order[i]
            right_country = table_order[i + 1]
            left_ally_index = -1
            me_ally_index = -1
            right_ally_index = -1

            for group in countries_group:
                if left_country in group:
                    left_ally_index = countries_group.index(group)
                if me_country in group:
                    me_ally_index = countries_group.index(group)
                if right_country in group:
                    right_ally_index = countries_group.index(group)

            if me_country not in enemy_of_countries:
                pass
            elif left_country in enemy_of_countries[me_country] or right_country in enemy_of_countries[me_country]:
                valid = False
                print('No')
                break

        if valid == True:
            print('Okay')
