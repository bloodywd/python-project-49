from random import randint


DESCRITION = 'What number is missing in the progression?'


def get_round():
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
