from constant.constant import weeks_time


def calculate_place_occupation(places, groups, lessons):
    statistics_list = []
    for i in range(weeks_time):
        statistics = dict()

        for key, value in places.items():
            statistics[key] = [[0] * 12 for _ in range(7)]
            for _, lesson in lessons.items():
                if lesson.place == key and i in lesson.periods:
                    statistics[key][lesson.week - 1][lesson.time - 1] += groups[lesson.group_no].people
            for t in range(12):
                for j in range(7):
                    statistics[key][j][t] /= int(value.people)

        statistics_list.append(statistics)

    return statistics_list
