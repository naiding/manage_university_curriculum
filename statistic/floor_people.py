from constant.constant import weeks_time
import copy


def calculate_floor_people(places, groups, lessons, room_people_list, classroom_info):

    statistics_list = []

    mydict = dict()
    for _, p in places.items():
        mydict[p.place_no] = 'N' if u'北' in p.exact_place else 'S'

    for i in range(weeks_time):
        statistics = [[0 for _ in range(12)] for _ in range(7)]

        for j in range(7):
            for t in range(12):

                room_dict = copy.deepcopy(classroom_info)
                # print(room_dict)

                for area, buildings_list in classroom_info.items():
                    for building, floors_list in buildings_list.items():
                        for floor, rooms_list in floors_list.items():

                            total = 0
                            if isinstance(rooms_list, list):
                                # print(type(rooms_list), ": ", rooms_list)
                                for index, room in enumerate(rooms_list):
                                    # print(room_people_list[i][room[0]][j][t])
                                    total += room_people_list[i][room[0]][j][t]

                            room_dict[area][building][floor] = total

                statistics[j][t] = room_dict

        statistics_list.append(statistics)

    return statistics_list


