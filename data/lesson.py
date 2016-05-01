class Lesson:

    group_no = None
    lesson_no = None
    periods = None
    week = None
    time = None
    place = None

    def __init__(self, group_no, lesson_no, week, time, place):
        self.group_no = group_no
        self.lesson_no = lesson_no
        self.periods = []
        self.week = int(week)
        self.time = int(time)
        self.place = place

    def add(self, period):
        self.periods.append(int(period))

    def __repr__(self):
        return self.group_no + ',' + self.lesson_no + ',' + str(self.week) + ',' + str(self.time)

    def __str__(self):
        return '<' + self.__repr__() + '>'
