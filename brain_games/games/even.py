from random import randint


DESCRITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_round():
    question = randint(1, 100)
    right_answer = question % 2 == 0 and 'yes' or 'no'
    return (str(question), str(right_answer))
