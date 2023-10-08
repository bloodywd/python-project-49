from random import randint


def prime_game():
    question = randint(1, 100)
    if question == 1:
        return (str(question), 'no')
    for i in range(2, (question // 2) + 1):
        if question % i == 0:
            return (str(question), 'no')
    return (str(question), 'yes')
