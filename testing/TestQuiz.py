import unittest
import json
from Quiz import Quiz
from QuizEncoder import QuizEncoder
from Question import Question


class TestQuiz(unittest.TestCase):
    def test_JSON_serializable(self):
        self.assertEqual("WHY DON'T YOU WORK", "WHY DON'T YOU WORK")
        q = Quiz()
        try:
            json.dumps(q, cls=QuizEncoder)
            self.assertEqual(1, 1)
        except TypeError as te:
            self.fail(te.args)

if __name__ == '__main__':
    unittest.main()