from random import randint


DESCRITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def get_round():
    question = randint(MIN_NUMBER, MAX_NUMBER)
    return str(question), 'yes' if is_prime(question) else 'no'
