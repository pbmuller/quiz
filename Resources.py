import os

quizzes_file_path = '{}{}quizzes'.format(
    os.path.dirname(__file__),
    '\\' if os.name == 'nt' else '/'
)

# testing_file_path = '{}{}testing'.format(
#     os.path.dirname(__file__),
#     '\\' if os.name == 'nt' else '/'
# )


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')