from constant.constant import weeks_time


class Group:

    lessons = None
    lessons_map = None
    group_no = None
    people = None

    def __init__(self, people, group_no):
        self.people = int(people)
        self.group_no = group_no
        self.lessons = [[[None for _ in range(12)] for _ in range(7)] for _ in range(weeks_time)]
        self.lessons_map = dict()

    def add(self, period, week, time, lesson):
        self.lessons[period - 1][week - 1][time - 1] = lesson
        self.lessons_map[(period, week, time)] = lesson

    def __repr__(self):
        return self.group_no + ',' + str(self.people)

    def __str__(self):
        return '<' + self.__repr__() + '>'

    def __lt__(self, other):
         return self.people < other.people

def group_to_dict(group):
    mydict = dict()
    mydict["people"] = group.people
    mydict["group_no"]