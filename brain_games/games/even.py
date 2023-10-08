from random import randint


def even_game():
    question = randint(1, 100)
    right_answer = question % 2 == 0 and 'yes' or 'no'
    return (str(question), str(right_answer))
