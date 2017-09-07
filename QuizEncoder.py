from json import JSONEncoder


class QuizEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
