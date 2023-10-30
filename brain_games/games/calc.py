from random import randint


DESCRITION = 'What is the result of the expression?'


def get_round():
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
