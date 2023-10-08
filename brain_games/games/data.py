from .calc import calc_game
from .even import even_game
from .gcd import gcd_game
from .progression import progression_game
from .prime import prime_game


def get_what_to_ask(game):
    answer = ''
    if game == 'even':
        answer = 'Answer "yes" if the number is even, otherwise answer "no".'
    elif game == 'calc':
        answer = "What is the result of the expression?"
    elif game == 'gcd':
        answer = "Find the greatest common divisor of given numbers."
    elif game == 'progression':
        answer = "What number is missing in the progression?"
    elif game == 'prime':
        answer = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    return answer


def get_questions(game):
    question = ''
    right_answer = ''
    if game == 'even':
        (question, right_answer) = even_game()
    if game == 'calc':
        (question, right_answer) = calc_game()
    if game == 'gcd':
        (question, right_answer) = gcd_game()
    if game == 'progression':
        (question, right_answer) = progression_game()
    if game == 'prime':
        (question, right_answer) = prime_game()
    return (question, right_answer)


def get_data(game):
    question_to_be_asked = get_what_to_ask(game)
    questions = []
    right_answers = []
    n = 3
    for i in range(0, n):
        (question, right_answer) = get_questions(game)
        questions.append(question)
        right_answers.append(right_answer)
    return ([question_to_be_asked, questions, right_answers])
