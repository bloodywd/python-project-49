from random import randint


DESCRITION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_round():
    question = randint(MIN_NUMBER, MAX_NUMBER)
    right_answer = question % 2 == 0 and 'yes' or 'no'
    return (str(question), right_answer)
