from constant.constant import input_lesson,input_people, input_places
from data.lesson import Lesson
from data.place import Place
from data.group import Group


def read_from_file():

    lessons = dict()
    groups = dict()
    places = dict()
    people = dict()

    with open(input_people, 'r+') as f:
        for line in f:
            v = list(map(lambda x:x.strip(), line.split(',')))
            people[v[0]] = int(v[1])

    with open(input_lesson, 'r+') as f:
        for line in f:
            v = list(map(lambda x:x.strip(), line.split(',')))
            key = v[0] + ',' + v[5] + ',' + v[1] + ',' + v[2]
            if key not in lessons:
                lesson = Lesson(v[0], v[5], v[1], v[2], v[6])
                for i in range(8, 33):
                    if v[i] == '1':
                        lesson.add(i - 8)
                lessons[key] = lesson
            else:
                for i in range(8, 33):
                    if v[i] == '1':
                        lessons[key].add(i - 8)

    with open(input_places, 'r+', encoding='UTF-8') as f:
        for line in f:
            v = list(map(lambda x:x.strip(), line.split(',')))
            place = Place(v[0], v[1], int(v[2]))
            places[v[0]] = place

    for key, value in lessons.items():
        groups_no_last_six = value.group_no[-6:] if len(value.group_no) == 24 else value.group_no[-7:-1]
        if groups_no_last_six in people:
            group = Group(people[groups_no_last_six], value.group_no)
            for element in value.periods:
                group.add(element, value.week, value.time, value)
            if value.group_no not in groups:
                groups[value.group_no] = group
            else:
                for element in value.periods:
                    groups[value.group_no].add(element, value.week, value.time, value)

    return places, groups, lessons
