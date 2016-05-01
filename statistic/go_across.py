from constant.constant import weeks_time

def calculate_go_accross(places, groups, lessons):

    statistics_list = []

    mydict = dict()
    for _, p in places.items():
        mydict[p.place_no] = 'N' if u'北' in p.exact_place else 'S'

    for i in range(weeks_time):

        statistics = [[0 for _ in range(2)] for _ in range(7)]

        for _, group in groups.items():
            for t in range(7):
                lesson_list = [group.lessons[i][t][1],group.lessons[i][t][2],
                               group.lessons[i][t][5],group.lessons[i][t][6]]
                for j in range(2):
                    if lesson_list[2 * j] is not None and lesson_list[2 * j + 1] is not None and \
                        lesson_list[2 * j].place in mydict and lesson_list[2 * j + 1].place in mydict and \
                            mydict[lesson_list[2 * j].place] != mydict[lesson_list[2 * j + 1].place]:
                        statistics[t][j] += group.people

        statistics_list.append(statistics)

    return statistics_list