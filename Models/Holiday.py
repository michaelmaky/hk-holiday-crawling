from json import JSONEncoder


class Holiday():
    def __init__(self, uid, date, name):
        self.uid = uid
        self.date = date
        self.name = name


class HolidayEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
