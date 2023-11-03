from random import randint, choice
import operator


DESCRITION = 'What is the result of the expression?'
operators = [
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul)
]


def get_question_and_answer():
    number1, number2 = randint(1, 25), randint(1, 25)
    operator, method = choice(operators)
    right_answer = method(number1, number2)
    return f'{number1} {operator} {number2}', str(right_answer)
