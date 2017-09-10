import unittest
import json
import os
from Question import Question
from QuestionEncoder import QuestionEncoder


class TestQuiz(unittest.TestCase):
    def setUp(self):
        self.question = Question("What day is today?", "Today")
        self.test_file = open(os.path.dirname(__file__) + '/test.json', 'w+')

    def tearDown(self):
        self.test_file.close()

    def test_JSON_serializable(self):
        self.setUp()
        try:
            json.dumps(self.question, cls=QuestionEncoder)
            self.assertEqual(1, 1)
        except TypeError:
            self.assertEqual(1, 2)

    def test_from_JSON(self):
        self.setUp()
        json.dump(self.question, self.test_file, cls=QuestionEncoder)
        q = json.load(self.test_file)
        q = Question.from_strings(q['question'], q['answer'])
        self.assertEqual(self.question, q)

if __name__ == '__main__':
    unittest.main()