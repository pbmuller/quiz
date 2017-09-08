from json import JSONEncoder


class QuestionEncoder(JSONEncoder):
    def encode(self, o):
        print(o.__dict__)
        return o.__dict__
