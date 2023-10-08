from random import randint
from math import gcd


def gcd_game():
    number_1 = randint(1, 25) + randint(1, 25)
    number_2 = randint(1, 25)
    right_answer = gcd(number_1, number_2)
    return (f'{number_1} {number_2}', str(right_answer))
