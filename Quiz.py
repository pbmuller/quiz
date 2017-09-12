from Question import Question
import pickle
import os
import Resources


class Quiz:
    def __init__(self, questions=list(), score=0, quiz_title="New Quiz"):
        self.questions = questions
        self.score = score
        self.quiz_title = quiz_title

    def _populate_quiz(self):
        while input('Would you like to add another question? [Y/n]\n>').lower() != 'n':
            question_text = input('What is the question?\n>')
            answer = input('What is the correct answer?\n>')
            while True:
                wrong_answers = []
                how_to_ask = input('How should this question be asked? (\'mc\', \'fitb\', \'tf\')\n>').lower()
                if how_to_ask.upper() == Question.MC:
                    i = 2
                    print('Multiple Choice Questions require at 2 wrong answers be given')
                    while i > 0:
                        wrong_answer = input('Enter a wrong answer\n>')
                        wrong_answers.append(wrong_answer)
                        i -= 1
                    break
                elif how_to_ask.upper() == Question.TF:
                    while True:
                        if answer.lower() != 'true' and answer.lower() != 'false':
                            print('True/False questions must have their answer be either true or false.'
                                  'Here is the Question. Please enter either true or false')
                            answer = input(question_text).lower()
                        else:
                            break
                    break
                elif how_to_ask.upper() != 'FITB':
                    print('Sorry, that\'s not a valid way to ask a question. Try Again')
                else:
                    break
            self.questions.append(Question(question_text, answer, how_to_ask, wrong_answers=wrong_answers))

    def quiz(self):
        Resources.clear_screen()
        self.score = 0
        for num, question in enumerate(self.questions, start=1):
            print('Question {} of {}'.format(num, len(self.questions)))
            if question.ask():
                self.score += 1
            input('Press ENTER to continue')
            Resources.clear_screen()
        print('You scored {}/{}'.format(self.score, len(self.questions)))
        input('Press ENTER to continue')
        Resources.clear_screen()

    def load_quiz(self):
        quiz_again = True
        while quiz_again:
            new_or_old = input('Would you like to create a new quiz or load a pre-existing one? (new/old)\n>').lower()
            if new_or_old != 'new' and new_or_old != 'old':
                print('You must enter either \'new\' or \'old\'\n')
            else:
                if new_or_old == 'new':
                    # get the quiz title
                    self.quiz_title = input("Enter the title of the quiz\n>").replace(' ', '_')
                    # populate the quiz
                    self._populate_quiz()
                    # save the quiz to the quizzes directory as a new file
                    quiz_file = open('{}{}{}.pickle'.format(
                        Resources.quizzes_file_path,
                        '\\' if os.name == 'nt' else '/',
                        self.quiz_title), 'wb')
                    pickle.dump(self, quiz_file)
                    quiz_file.close()
                    # ask if the user would like to take the quiz now
                    if input('Would you like to take the quiz now? [Y/n]\n>').lower() != 'n':
                        self.quiz()
                elif new_or_old == 'old':
                    valid_index = False
                    quiz_dict = {}
                    # print the list of files in the quizzes directory
                    print('Quiz List')
                    for num, file in enumerate(
                            os.listdir(Resources.quizzes_file_path),
                            start=1):
                        print('\t{}: {}'.format(num, file))
                        quiz_dict[num] = file
                    # ask the user which of the quizzes they would like to take.
                    while not valid_index:
                        try:
                            quiz_index = int(input('Enter the number of the quiz that you would to take\n>'))
                            valid_index = True
                        except ValueError:
                            print('Sorry, that wasn\'t a valid index')
                        else:
                            quiz_file = open('{}{}{}'.format(
                                Resources.quizzes_file_path,
                                '\\' if os.name == 'nt' else '/',
                                quiz_dict[quiz_index]), 'rb')
                            # load that quiz from the pickle in the file
                            pickle_quiz = pickle.load(quiz_file)
                            quiz_file.close()
                            # give the user the quiz
                            pickle_quiz.quiz()
                if input('Would you like to load another quiz? [Y/n]\n>').lower() == 'n':
                    quiz_again = False

    @classmethod
    def dict_to_quiz(cls, questions, score, quiz_title):
        return cls(questions, score, quiz_title)
