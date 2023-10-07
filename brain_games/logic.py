from random import randint


def get_random():
    number = randint(1, 100)
    odd_or_not = number % 2 == 0 and 'yes' or 'no'
    return (number, odd_or_not)
