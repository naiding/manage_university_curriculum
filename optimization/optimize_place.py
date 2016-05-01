import os
import json
from scripts.json_handler import writeJson, readJson
from statistic.empty_classroom import calculate_empty_classroom
def calculate_cross_people(groups_list, week, period, time_option):

    cross_people = 0

    path = os.getcwd()
    parent_path = os.path.dirname(path)
    mydict = readJson(parent_path + '/jsons/places.json')

    for index, group in enumerate(groups_list):

            lesson1 = group.lessons[week][period][time_option*4+1]
            lesson2 = group.lessons[week][period][time_option*4+2]

            if lesson1 is None or lesson2 is None:
                continue

            place1 = lesson1.place
            place2 = lesson2.place

            if place1 in mydict and place2 in mydict and mydict[place1] != mydict[place2]:
                cross_people += group.people

    return cross_people

def get_separate_group_list(lesson_group_list, week, period, time_option):

    path = os.getcwd()
    parent_path = os.path.dirname(path)
    mydict = readJson(parent_path + '/jsons/places.json')

    north_groups = []
    south_groups = []
    total_north_people = 0
    total_south_people = 0
    lesson_location = ''

    for index, group in enumerate(lesson_group_list):
        if mydict[group.lessons[week][period][time_option*4+2].place] == 'N':
            north_groups.append(group)
            total_north_people = total_north_people + group.people
            lesson_location = mydict[group.lessons[week][period][time_option*4+2].place]

        elif mydict[group.lessons[week][period][time_option*4+2].place] == 'S':
            south_groups.append(group)
            total_south_people = total_south_people + group.people
            lesson_location = mydict[group.lessons[week][period][time_option*4+2].place]


    return lesson_location, north_groups, south_groups, total_north_people, total_south_people


def optimize_by_place(places, groups, lessons, target_groups_list, week, period, time_option, north_empty_classroom, south_empty_classroom):

    path = os.getcwd()
    parent_path = os.path.dirname(path)
    mydict = readJson(parent_path + '/jsons/places.json')

    cross_people = calculate_cross_people(target_groups_list, week, period, time_option)
    print('Total cross people: ', cross_people)

    cross_groups_list = []
    for index, target_group in enumerate(target_groups_list):

        lesson1 = target_group.lessons[week][period][time_option*4+1]
        lesson2 = target_group.lessons[week][period][time_option*4+2]

        place1 = lesson1.place
        place2 = lesson2.place

        if place1 in mydict and place2 in mydict:
            if place1 == place2:
                # print('----------------------------')
                continue
            else:
                conflict_groups_list = []

                for _, group in groups.items():
                    if group.lessons[week][period][time_option*4+2] is not None and \
                        group.lessons[week][period][time_option*4+3] is not None and \
                        group.lessons[week][period][time_option*4+2].place in mydict and \
                        group.lessons[week][period][time_option*4+2].place == place2:

                        conflict_groups_list.append(group)

                # print('Length = ', len(conflict_groups_list))
                for index, conflict_group in enumerate(conflict_groups_list):
                    if conflict_group.lessons[week][period][time_option*4+1] is not None and \
                        conflict_group.lessons[week][period][time_option*4+2] is not None and \
                        conflict_group.lessons[week][period][time_option*4+1].place in mydict and \
                        conflict_group.lessons[week][period][time_option*4+2].place in mydict and \
                        mydict[conflict_group.lessons[week][period][time_option*4+1].place] != \
                        mydict[conflict_group.lessons[week][period][time_option*4+2].place]:
                        cross_groups_list.append(conflict_groups_list)
                        break

    print('Length of cross_groups_list: ', len(cross_groups_list))

    new_cross_groups_list = []
    for index, value in enumerate(cross_groups_list):
        if value not in new_cross_groups_list:
            new_cross_groups_list.append(value)
    print('Length of new_cross_groups_list: ', len(new_cross_groups_list))

    # total = 0
    # for _, value in enumerate(new_cross_groups_list):
    #     total += calculate_cross_people(value, week, period, time_option)
    #
    # print(total)

    optimized_groups_list = []

    for index, value in enumerate(new_cross_groups_list):
        lesson_location, north_groups, south_groups, total_north_people, total_south_people = \
            get_separate_group_list(value, week, period, time_option)
        # print(lesson_location)

        if total_north_people >= total_south_people and total_north_people + total_south_people != 0:
            for _, empty_classroom in enumerate(north_empty_classroom):
                if empty_classroom.people >= total_north_people:
                    print(index, "Found")
                    for _, every_group in enumerate(value):
                        every_group.lessons[week][period][time_option*4+2].place = empty_classroom.place_no
                        every_group.lessons[week][period][time_option*4+3].place = empty_classroom.place_no
                        optimized_groups_list.append(every_group)

                    break
                # else:
                #     print(index, "Not found")
        if total_north_people < total_south_people and total_north_people + total_south_people != 0:
            for _, empty_classroom in enumerate(south_empty_classroom):
                if empty_classroom.people >= total_south_people:
                    print(index, "Found")
                    for _, every_group in enumerate(value):
                        every_group.lessons[week][period][time_option*4+2].place = empty_classroom.place_no
                        every_group.lessons[week][period][time_option*4+3].place = empty_classroom.place_no
                        optimized_groups_list.append(every_group)

                    break
                # else:
                #     print(index, "Not found")

    print('Total of optimized cross people:', len(optimized_groups_list))

    return optimized_groups_list







# def optimize_by_place(north_empty_classroom, south_empty_classroom, n_to_s_group_list, s_to_n_group_list):
#
#     go_cross_group_people = 0
#     n_to_s_group_list.sort()
#     s_to_n_group_list.sort()
#
#     for index, group in enumerate(n_to_s_group_list):
#         go_cross_group_people += group.people
#
#     for index, group in enumerate(s_to_n_group_list):
#         go_cross_group_people += group.people
#
#     print(go_cross_group_people)
#
#
#     empty_classroom_people = 0
#     north_empty_classroom.sort()
#     south_empty_classroom.sort()
#
#     for index, place in enumerate(north_empty_classroom):
#         empty_classroom_people += place.people
#         print(place.place_no)
#
#     for index, place in enumerate(south_empty_classroom):
#         empty_classroom_people += place.people
#         print(place.place_no)
