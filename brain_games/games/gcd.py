from random import randint
from math import gcd


DESCRITION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number1 = randint(1, 50)
    number2 = randint(1, 20)
    right_answer = gcd(number1, number2)
    return f'{number1} {number2}', str(right_answer)
