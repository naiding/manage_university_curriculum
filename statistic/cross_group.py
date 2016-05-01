from constant.constant import weeks_time

def calculate_cross_group(places, groups, lessons, week, period, time_option):

    n_to_s_group_list = []
    s_to_n_group_list = []

    mydict = dict()
    for _, p in places.items():
        mydict[p.place_no] = 'N' if u'北' in p.exact_place else 'S'

    j = time_option

    for _, group in groups.items():
        lesson_list = [group.lessons[week][period][1],group.lessons[week][period][2],
                       group.lessons[week][period][5],group.lessons[week][period][6]]

        if  lesson_list[2 * j] is not None and lesson_list[2 * j + 1] is not None and \
            lesson_list[2 * j].place in mydict and lesson_list[2 * j + 1].place in mydict and \
            mydict[lesson_list[2 * j].place] != mydict[lesson_list[2 * j + 1].place] and \
            mydict[lesson_list[2 * j].place] == 'N':

                n_to_s_group_list.append(group)

        if  lesson_list[2 * j] is not None and lesson_list[2 * j + 1] is not None and \
            lesson_list[2 * j].place in mydict and lesson_list[2 * j + 1].place in mydict and \
            mydict[lesson_list[2 * j].place] != mydict[lesson_list[2 * j + 1].place] and \
            mydict[lesson_list[2 * j].place] == 'S':

                s_to_n_group_list.append(group)

    return n_to_s_group_list, s_to_n_group_list
