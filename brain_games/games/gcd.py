from random import randint
from math import gcd


DESCRITION = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER1 = 50
MAX_NUMBER2 = 20


def get_round():
    number_1 = randint(MIN_NUMBER, MAX_NUMBER1)
    number_2 = randint(MIN_NUMBER, MAX_NUMBER2)
    right_answer = gcd(number_1, number_2)
    return f'{number_1} {number_2}', str(right_answer)
