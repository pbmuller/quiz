from Question import Question
import json
import os
import Resources


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
        for question in self.questions:
            if question.ask():
                self.score += 1
        print('You scored {}/{}'.format(self.score, len(self.questions)))

    def load_quiz(self):
        quiz_again = True
        while quiz_again:
            new_or_old = input('Would you like to create a new quiz or load a pre-existing one? (new/old)').lower()
            if new_or_old == 'new':
                # get the quiz title
                self.quiz_title = input("Enter the title of the quiz: ")
                # populate the quiz
                self._populate_quiz()
                # save the quiz to the quizzes directory as a new file
                # ask if the user would like to take the quiz now
                # if yes, do the quiz
                # elif no, go back to the start of the
            elif new_or_old == 'old':
                valid_index = False
                quiz_dict = {}
                # print the list of files in the quizzes directory
                quiz_enum = enumerate(os.listdir(Resources.quizzes_file_path), start=1)
                print('Quiz List')
                for num, file in quiz_enum:
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
                        selected_quiz = json.load(Resources.quizzes_file_path + '\\' + quiz_dict[quiz_index])
                # give the user the quiz
            else:
                print("You must enter either new or old")
            quiz_again = False

    @classmethod
    def dict_to_quiz(cls, questions, score, quiz_title):
        return cls(questions, score, quiz_title)