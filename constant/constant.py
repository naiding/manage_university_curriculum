import os

input_file = os.path.split(os.path.abspath(__file__))[0] + '/../resources/'.replace('/', os.sep)

input_lesson = input_file + 'lesson.csv'
input_people = input_file + 'people.csv'
input_places = input_file + 'places.csv'

weeks_time = 25