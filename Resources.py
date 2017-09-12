import os


def proper_slash():
    return '\\' if os.name == 'nt' else '/'

quizzes_file_path = '{}{}quizzes'.format(
    os.path.dirname(__file__),
    proper_slash()
)

# testing_file_path = '{}{}testing'.format(
#     os.path.dirname(__file__),
#     '\\' if os.name == 'nt' else '/'
# )


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')