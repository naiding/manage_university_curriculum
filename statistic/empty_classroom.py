from constant.constant import weeks_time
from scripts.json_handler import writeJson, readJson
import os

def calculate_empty_classroom(places, groups, lessons, week, period, time):

    north_statistics_list = []
    south_statistics_list = []

    path = os.getcwd()
    parent_path = os.path.dirname(path)
    occupation_list = readJson(parent_path + '/jsons/occupation_list.json')

    mydict = dict()
    for _, p in places.items():
        mydict[p.place_no] = 'N' if u'北' in p.exact_place else 'S'

    for key, values in occupation_list[week].items():
        if values[period][time] == 0:
            place = places[key]
            if mydict[place.place_no] == 'N':
                north_statistics_list.append(place)
            if mydict[place.place_no] == 'S':
                south_statistics_list.append(place)

    return north_statistics_list, south_statistics_list