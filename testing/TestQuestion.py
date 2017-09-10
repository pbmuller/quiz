import unittest
import pickle
import Resources
from Question import Question


class TestQuiz(unittest.TestCase):
    def setUp(self):
        self.question = Question("What day is today?", "Today")

    def test_pickling(self):
        self.setUp()
        try:
            pickle_in = open('test_pickling.pickle', 'wb')
            pickle.dump(self.question, pickle_in)
            pickle_in.close()
            self.assertEqual(1, 1)
        except TypeError:
            self.assertEqual(1, 2)

    def test_from_JSON(self):
        self.setUp()
        pickle_in = open('test_pickling.pickle', 'wb')
        pickle.dump(self.question, pickle_in)
        pickle_in.close()
        pickle_out = open('test_pickling.pickle', 'rb')
        q = pickle.load(pickle_out)
        self.assertEqual(self.question, q)

if __name__ == '__main__':
    unittest.main()