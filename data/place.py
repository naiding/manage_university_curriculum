class Place:

    place_no = None
    exact_place = None
    people = None

    def __init__(self, place_no, exact_place, people):
        self.place_no = place_no
        self.exact_place = exact_place
        self.people = people

    def __lt__(self, other):
        return self.people < other.people

def place_to_dict(place):
    mydict = dict()
    mydict["place_no"] = place.place_no
    mydict["exact_place"] = place.exact_place
    mydict["people"] = place.people
    return mydict
