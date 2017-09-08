from json import JSONEncoder
from QuestionEncoder import QuestionEncoder


class QuizEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
