import random


class Question(object):
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask(self, how_to_ask='FTIB', *args):
        if how_to_ask == 'MC':
            answer_set = set(args)
            answer_set.add(self.answer)
            answer_set = random.sample(answer_set, len(answer_set))
            for num, answer in enumerate(answer_set, start=1):
                print('{}. {}'.format(num, answer))
                if answer == self.answer:
                    correct = num
            while True:
                try:
                    if int(input('Enter the number corresponding to the correct answer')) == correct:
                        return self.correct_answer()
                    else:
                        return self.wrong_answer()
                except ValueError:
                    print('Sorry that wasn\'t a valid number')
        elif how_to_ask == 'FITB':
            answer = input(self.question + '\n').lower()
            if answer == self.answer:
                print('CORRECT!')
                return True
            else:
                print('Sorry, that was not correct')

    @staticmethod
    def correct_answer():
        print('CORRECT')
        return True

    @staticmethod
    def wrong_answer():
        print('Sorry, that was not correct')
        return False