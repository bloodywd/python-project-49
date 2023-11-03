from random import randint


DESCRITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def get_question_and_answer():
    question = randint(1, 100)
    return str(question), 'yes' if is_prime(question) else 'no'
