import os
import copy
import json
from constant.constant import weeks_time
from json_handler import writeJson, readJson
from input.read_from_data import read_from_file
from statistic.go_across import calculate_go_accross
from statistic.place_occupation import calculate_place_occupation
from statistic.room_people import calculate_room_people
from statistic.floor_people import calculate_floor_people
from statistic.empty_classroom import calculate_empty_classroom
from statistic.cross_group import calculate_cross_group
from statistic.half_day_group import calculate_half_day_group

from optimization.optimize_place import optimize_by_place

# places 教室相关
# groups 班级相关
# lessons 课程相关

places, groups, lessons = read_from_file()

week = 4
period = 0
time_option = 0
time = 2

# print(lessons.keys())
#
# key = '201419312015-20161193141,21209222,1,8' # '201308602015-20161086131,20822700,5,5'
# print(lessons[key].group_no)
# print(lessons[key].lesson_no)
# print(lessons[key].periods)
# print(lessons[key].week)
# print(lessons[key].time)
# print(lessons[key].place)


# print('Total classroom: ', len(places))

#
# 把教室的方位写入文件
#
# mydict = dict()
# for _, p in places.items():
#     mydict[p.place_no] = 'N' if u'北' in p.exact_place else 'S'
#
# with open('places.json', 'w') as f:
#     f.write(json.dumps(mydict))



#
# 找出某个时间段的空教室
#
# north_empty_classroom, south_empty_classroom = calculate_empty_classroom(places, groups, lessons, 0, 0, 0)

#
# 找出某个时间段的交叉班级
#
# n_to_s_group_list, s_to_n_group_list = calculate_cross_group(places, groups, lessons, 0, 0, 0)




#
# 写入json
#
# room_people_list = calculate_room_people(places, groups, lessons)
# writeJson(room_people_list, 'room_people_list.json')

# occpuation_list = calculate_place_occupation(places, groups, lessons)
# writeJson(occpuation_list, 'occupation_list.json')
#
# across_list = calculate_go_accross(places, groups, lessons)
# writeJson(across_list, 'across_list.json')

#
# 从json读取
#
path = os.getcwd()
parent_path = os.path.dirname(path)

occpuation_list = readJson(parent_path + '/jsons/occupation_list.json')
across_list = readJson(parent_path + '/jsons/across_list.json')
room_people_list = readJson(parent_path + '/jsons/room_people_list.json')
building_info = readJson(parent_path + '/jsons/building_info.json')
classroom_info = readJson(parent_path + '/jsons/classroom_info.json')
building_classroom_info = readJson(parent_path + '/jsons/building_classroom_info.json')
floor_people = readJson(parent_path + '/jsons/floor_people.json')
area_info = readJson(parent_path + '/jsons/places.json')
building_people_info = readJson(parent_path + '/jsons/building_people_info.json')



building = '北区综合楼'
total_in = 0
total_out = 0

i = 8
j = 2
t = 0
for _, group in groups.items():

    lesson1 = group.lessons[i][j][t*4+1]
    lesson2 = group.lessons[i][j][t*4+2]

    if lesson1 is not None and lesson2 is None and \
        lesson1.place in classroom_info and \
        classroom_info[lesson1.place] == building:
        total_out += group.people

    if lesson2 is not None and lesson1 is None and \
        lesson2.place in classroom_info and \
        classroom_info[lesson2.place] == building:
        total_in += group.people

    if lesson1 is not None and lesson2 is not None and \
        lesson1.place in classroom_info and \
        lesson2.place in classroom_info:
        if classroom_info[lesson1.place] == building and classroom_info[lesson2.place] != building:
            total_out += group.people
        if classroom_info[lesson1.place] != building and classroom_info[lesson2.place] == building:
            total_in += group.people

print("in", total_in, 'out', total_out)

# total_in_out_rate = []
#
# for building, people in building_people_info.items():
#
#     total_in_out = 0
#
#     for _, group in groups.items():
#         for i in range(25):
#             for j in range(5):
#                 for t in range(2):
#                     lesson1 = group.lessons[i][j][t*4+1]
#                     lesson2 = group.lessons[i][j][t*4+2]
#
#                     if lesson1 is not None and lesson2 is None and \
#                         lesson1.place in classroom_info and \
#                         classroom_info[lesson1.place] == building:
#                         total_in_out += group.people
#
#                     if lesson2 is not None and lesson1 is None and \
#                         lesson2.place in classroom_info and \
#                         classroom_info[lesson2.place] == building:
#                         total_in_out += group.people
#
#                     if lesson1 is not None and lesson2 is not None and \
#                         lesson1.place in classroom_info and \
#                         lesson2.place in classroom_info and \
#                         ((classroom_info[lesson1.place] == building and classroom_info[lesson2.place] != building) or \
#                          (classroom_info[lesson1.place] != building and classroom_info[lesson2.place] == building) ):
#
#                         total_in_out += group.people
#
#     total_in_out_rate.append([building, total_in_out/250/people])
#
# total_rate = 0
# count = 0
# for index, value in enumerate(total_in_out_rate):
#      total_rate += value[1]
#      count += 1
# print(total_rate/count)
#
# print("in out rate: ", total_in_out_rate)

# max_people = 0
# total_cross_people = 0
# for i in range(25):
#     for j in range(5):
#         for t in range(2):
#
#             once_cross_people = 0
#             for _, group in groups.items():
#                 lesson1 = group.lessons[i][j][t*4+1]
#                 lesson2 = group.lessons[i][j][t*4+2]
#
#                 if lesson1 is not None and lesson2 is not None and \
#                     lesson1.place in area_info and lesson2.place in area_info and \
#                     area_info[lesson1.place] != area_info[lesson2.place]:
#                     once_cross_people += group.people
#
#             if once_cross_people > max_people:
#                 max_people = once_cross_people
#
#             total_cross_people += once_cross_people
#             # print(once_cross_people)
#
# print(max_people, total_cross_people, total_cross_people/max_people/250)
#

# total_cross_people = 0
# times = 0
# for _, value in enumerate(across_list):
#     for aDay in range(5):
#         total_cross_people += value[aDay][0]
#         total_cross_people += value[aDay][1]
#         times += 1
#
# print(total_cross_people, " ", times)
#
# total_people = 0
# total_group = 0
# for _, group in groups.items():
#     total_people += group.people
#     total_group+=1
# print(total_people, ' ', total_group)

# print(floor_people[week][period][time])
#
# print(room_people_list[1])
# print(occpuation_list[1])
# print(across_list[0])
# print(building_info['N']['北区综合楼'])
# print(classroom_info['JS0210'])
# print(building_classroom_info['北区综合楼'])

#
# 计算楼层人数

# floor_people = calculate_floor_people(places, groups, lessons, room_people_list, building_info)
# writeJson(floor_people, 'floor_people.json')


#
# 计算优化之前每栋楼的人数
#

# floor_dict = floor_people[week][period][time]
# building_dict = floor_dict
#
# for area, buildings_list in floor_dict.items():
#     for building, floors_list in buildings_list.items():
#         total = 0
#         for floor, people in floors_list.items():
#             total += people
#
#         building_dict[area][building] = total
#
# print(building_dict)
#
# old_building_dict = building_dict

# for area, buildings_list in old_building_dict.items():
#     for building, floors_list in buildings_list.items():
#         old_building_dict[area][building] = 0
#
# for _, group in groups.items():
#     lesson = group.lessons[week][period][time]
#     if lesson is not None and \
#         lesson.place in classroom_info and \
#         lesson.place in area_info:
#         classroom = lesson.place
#         old_building_dict[area_info[classroom]][classroom_info[classroom]] += group.people
#
# print('Old building: ',  old_building_dict)

#
# 找出某个上午或者下午的满课的班级
#

# for i in range(25):
#     for j in range(5):
#         for t in range(2):
#
#             week = i
#             period = j
#             time_option = t
#
#             target_groups_list = calculate_half_day_group(places, groups, lessons, week, period, time_option)
#             north_empty_classroom, south_empty_classroom = calculate_empty_classroom(places, groups, lessons, week, period, time_option)
#             # print('North empty classroom: ', len(north_empty_classroom))
#             # print('South empty classroom: ', len(south_empty_classroom))
#
#             # 优化地点
#             #
#             optimized_groups_list = optimize_by_place(places, groups, lessons, target_groups_list,
#                                                       week, period, time_option, north_empty_classroom, south_empty_classroom)

#
# 计算优化后每栋楼的人数
#

# 更新groups信息
# optimized_groups = copy.deepcopy(groups)
#
# for _, new_group in enumerate(optimized_groups_list):
#     print("old group: ", new_group.group_no, ": ",  groups[new_group.group_no].lessons[week][period][time_option*4+2].place)
#     optimized_groups[new_group.group_no] = new_group
#     print("new group: ", new_group.group_no, ": ", new_group.lessons[week][period][time_option*4+2].place)
#     # print("new: ", optimized_groups[new_group.group_no].lessons[week][period][time_option*4+2].place)
#     print()

#
# for _, group in groups.items():
#     for _, new_group in enumerate(optimized_groups_list):
#         if new_group.group_no == group.group_no:
#             print("old: ", group.lessons[week][period][time_option*4+2].place)
#             print("new: ", new_group.lessons[week][period][time_option*4+2].place)
#             optimized_groups[new_group.group_no] = new_group

# 初始化新的字典
# new_building_dict = building_dict
# for area, buildings_list in new_building_dict.items():
#     for building, floors_list in buildings_list.items():
#         new_building_dict[area][building] = 0
#
# # 计算人数
# for group_index, group in optimized_groups.items():
#     lesson = group.lessons[week][period][time]
#     if lesson is not None and \
#         lesson.place in classroom_info and \
#         lesson.place in area_info:
#
#         classroom = lesson.place
#         new_building_dict[area_info[classroom]][classroom_info[classroom]] += group.people
#
# print('New building: ', new_building_dict)




#
# final_rate = 0
# for key, value in enumerate(total_in_out_rate):
#     final_rate += value[1]
# print(final_rate/10)


    # if lesson1 is not None and lesson2 is None and lesson1.place:
    #     total_in_out +=
    #
    # if () or \
    #     (lesson2 is not None and lesson1 is None) or \
    #     ((lesson1 is not None and lesson2 is not None) and \
    #      (lesson1.place in classroom_info and lesson2.place in classroom_info) and \
    #      ()):



# print('Building: ', building)
# print('Total out: ',  total_out)
# print('Total in: ',  total_in)


#
# 计算进出教学楼人数
#


#
# total_in_out_rate = []
#
# for building, people in building_people_info.items():
#
#     total_in_out = 0
#
#     for _, group in groups.items():
#         for i in range(25):
#             for j in range(5):
#                 for t in range(2):
#                     lesson1 = group.lessons[i][j][t*4+1]
#                     lesson2 = group.lessons[i][j][t*4+2]
#
#                     if lesson1 is not None and lesson2 is None and \
#                         lesson1.place in classroom_info and \
#                         classroom_info[lesson1.place] == building:
#                         total_in_out += group.people
#
#                     if lesson2 is not None and lesson1 is None and \
#                         lesson2.place in classroom_info and \
#                         classroom_info[lesson2.place] == building:
#                         total_in_out += group.people
#
#                     if lesson1 is not None and lesson2 is not None and \
#                         lesson1.place in classroom_info and \
#                         lesson2.place in classroom_info and \
#                         ((classroom_info[lesson1.place] == building and classroom_info[lesson2.place] != building) or \
#                          (classroom_info[lesson1.place] != building and classroom_info[lesson2.place] == building) ):
#
#                         total_in_out += group.people
#
#     total_in_out_rate.append([building, total_in_out/250/people])
#
# print("in out rate: ", total_in_out_rate)
#
# max_people = 0
# total_cross_people = 0
# for i in range(25):
#     for j in range(5):
#         for t in range(2):
#
#             once_cross_people = 0
#             for _, group in groups.items():
#                 lesson1 = group.lessons[i][j][t*4+1]
#                 lesson2 = group.lessons[i][j][t*4+2]
#
#                 if lesson1 is not None and lesson2 is not None and \
#                     lesson1.place in area_info and lesson2.place in area_info and \
#                     area_info[lesson1.place] != area_info[lesson2.place]:
#                     once_cross_people += group.people
#
#             if once_cross_people > max_people:
#                 max_people = once_cross_people
#
#             total_cross_people += once_cross_people
#             # print(once_cross_people)
#
# print(max_people, total_cross_people, total_cross_people/max_people/250)