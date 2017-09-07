class Question(object):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask(self):
        answer = input(self.question + '\n').lower()
        if answer == self.answer:
            print('CORRECT!')
            return True
        else:
            print('Sorry, that was not correct')
