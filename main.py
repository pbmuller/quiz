from Quiz import Quiz
import os

def main():
    # quiz = Quiz()
    # quiz.load_quiz()
    for num, name in enumerate(os.listdir(os.path.dirname(__file__) + '/quizzes'), start=1):
        print("{}: {}".format(num, name))

if __name__ == '__main__':
    main()
