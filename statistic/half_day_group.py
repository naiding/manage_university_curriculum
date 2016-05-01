

def calculate_half_day_group(places, groups, lessons, week, period, time_option):

    statistics_list = []
    j = time_option
    for index, group in groups.items():

        if group.lessons[week][period][4*j] is not None and \
            group.lessons[week][period][4*j+1] is not None and \
            group.lessons[week][period][4*j+2] is not None and \
            group.lessons[week][period][4*j+3] is not None :

            statistics_list.append(group)

    return statistics_list