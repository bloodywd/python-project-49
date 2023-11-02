from random import randint, choice
import operator


DESCRITION = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 25
operators = [
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul)
]


def get_round():
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    number2 = randint(MIN_NUMBER, MAX_NUMBER)
    operator, method = choice(operators)
    right_answer = method(number1, number2)
    return f'{number1} {operator} {number2}', str(right_answer)
