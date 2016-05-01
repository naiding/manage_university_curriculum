import json

def calculate_cross_people(groups_list, week, period, time_option):

    cross_people = 0

    path = os.getcwd()
    parent_path = os.path.dirname(path)
    mydict = readJson(parent_path + '/jsons/places.json')

    for index, group in enumerate(groups_list):

            lesson1 = group.lessons[week][period][time_option*4+1]
            lesson2 = group.lessons[week][period][time_option*4+2]

            place1 = lesson1.place
            place2 = lesson2.place

            if place1 in mydict and place2 in mydict and mydict[place1] != mydict[place2]:
                cross_people += group.people

    return cross_people