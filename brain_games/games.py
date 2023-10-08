from random import randint
from math import gcd


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


def even_game():
    question = randint(1, 100)
    right_answer = question % 2 == 0 and 'yes' or 'no'
    return (str(question), str(right_answer))


def calc_game():
    number_1 = randint(1, 25)
    number_2 = randint(1, 25)
    operation = randint(0, 2)
    if operation == 0:
        right_answer = number_1 + number_2
        return (f'{number_1} + {number_2}', str(right_answer))
    elif operation == 1:
        right_answer = number_1 - number_2
        return (f'{number_1} - {number_2}', str(right_answer))
    elif operation == 2:
        right_answer = number_1 * number_2
        return (f'{number_1} * {number_2}', str(right_answer))


def gcd_game():
    number_1 = randint(1, 25) + randint(1, 25)
    number_2 = randint(1, 25)
    right_answer = gcd(number_1, number_2)
    return (f'{number_1} {number_2}', str(right_answer))


def progression_game():
    next_number = randint(1, 10)
    step = randint(2, 8)
    progression_range = randint(5, 10)
    answer_index = randint(0, progression_range - 1)
    question = ''
    right_answer = 0
    for i in range(0, progression_range):
        if i == answer_index:
            question += ".. "
            right_answer = next_number
            next_number += step
            continue
        question = question + str(next_number) + " "
        next_number += step
    return (question.strip(), str(right_answer))


def prime_game():
    question = randint(1, 100)
    for i in range(2, (question // 2) + 1):
        if question % i == 0:
            return (str(question), 'no')
    return (str(question), 'yes')


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
