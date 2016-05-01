import os
import json
from constant.constant import weeks_time
from json_handler import writeJson, readJson
from input.read_from_data import read_from_file
from statistic.go_across import calculate_go_accross
from statistic.place_occupation import calculate_place_occupation
from statistic.floor_people import calculate_floor_people
from statistic.empty_classroom import calculate_empty_classroom
from statistic.cross_group import calculate_cross_group
from statistic.half_day_group import calculate_half_day_group

from optimization.optimize_place import optimize_by_place

# places 教室相关
# groups 班级相关
# lessons 课程相关

# places, groups, lessons = read_from_file()


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
# 找出某个上午或者下午的满课的班级
#
# week = 5
# period = 4
# time_option = 0
# target_groups_list = calculate_half_day_group(places, groups, lessons, week, period, time_option)
# north_empty_classroom, south_empty_classroom = calculate_empty_classroom(places, groups, lessons, week, period, time_option)
# print('North empty classroom: ', len(north_empty_classroom))
# print('South empty classroom: ', len(south_empty_classroom))
#
# 优化地点
#
# optimized_groups_list = optimize_by_place(places, groups, lessons, target_groups_list, week, period, time_option, north_empty_classroom, south_empty_classroom)


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
# floor_people_list = calculate_floor_people(places, groups, lessons)
# writeJson(floor_people_list, 'floor_people_list.json')
#
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
floor_people_list = readJson(parent_path + '/jsons/floor_people_list.json')
classroom_info = readJson(parent_path + '/jsons/classroom_info.json')


print(floor_people_list[1])
print(occpuation_list[1])
print(across_list[0])
print(classroom_info['N'])




# import matplotlib.pyplot as plt
# plt(np.arrage(10))
#


