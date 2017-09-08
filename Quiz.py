from Question import Question
from QuizEncoder import QuizEncoder
import json
import os
import Resources
import random


class Quiz(object):
    def __init__(self, questions=set(), score=0, quiz_title="New Quiz"):
        super().__init__()
        self.questions = questions
        self.score = score
        self.quiz_title = quiz_title

    def _populate_quiz(self):
        while input('Would you like to add another question? [Y/n] ').lower() != 'n':
            question_text = input('What is the question?\n')
            answer = input('What is the correct answer?\n')
            self.questions.add(Question(question_text, answer))

    def quiz(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.score = 0
        for num, question in enumerate(self.questions):
            print('Question {}'.format(num))
            wrong_answers = self.get_wrong_answers(question)
            if question.ask(wrong_answers, how_to_ask='MC'):
                self.score += 1
        print('You scored {}/{}'.format(self.score, len(self.questions)))

    def load_quiz(self):
        quiz_again = True
        while quiz_again:
            new_or_old = input('Would you like to create a new quiz or load a pre-existing one? (new/old)').lower()
            if new_or_old != 'new' and new_or_old != 'old':
                print('You must enter either \'new\' or \'old\'')
            else:
                if new_or_old == 'new':
                    # get the quiz title
                    self.quiz_title = input("Enter the title of the quiz: ")
                    # populate the quiz
                    self._populate_quiz()
                    # save the quiz to the quizzes directory as a new file
                    quiz_file = open('{}.txt'.format(self.quiz_title), 'w')
                    quiz_file.write(json.dumps(self, encoder=QuizEncoder()))
                    # ask if the user would like to take the quiz now
                    if input('Would you like to take the quiz now? [Y/n]').lower() != 'n':
                        self.quiz()
                    if input('Would you like to load another quiz? [Y/n]').lower() == 'n':
                        quiz_again = False
                elif new_or_old == 'old':
                    valid_index = False
                    quiz_dict = {}
                    # print the list of files in the quizzes directory
                    print('Quiz List')
                    for num, file in enumerate(os.listdir(os.path.dirname(__file__) + '/quizzes'), start=1):
                        print('{}: {}'.format(num, file))
                        quiz_dict[num] = file
                    # ask the user which of the quizzes they would like to take.
                    while not valid_index:
                        try:
                            quiz_index = int(input('Enter the number of the quiz that you would to take'))
                        except ValueError:
                            print('Sorry, that wasn\'t a valid index')
                        else:
                            # load that quiz from the json in the file
                            json_quiz = json.load(Resources.quizzes_file_path + ' \\' + quiz_dict[quiz_index])
                            selected_quiz = self.dict_to_quiz(
                                json_quiz['questions'],
                                json_quiz['score'],
                                json_quiz['quiz_title']
                            )
                            # give the user the quiz
                            selected_quiz.quiz()

    def get_wrong_answers(self, current_question):
        while True:
            rand_questions = random.sample(self.questions, 3)
            if current_question not in rand_questions:
                answers = set()
                for question in rand_questions:
                    answers.add(question.answer)
                    return answers

    @classmethod
    def dict_to_quiz(cls, questions, score, quiz_title):
        return cls(questions, score, quiz_title)
