from .logic import get_random


def even(name):
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    for i in range(0, 3):
        (number, ans) = get_random()
        print(f'Question: {number}')
        ans_u = input("Your answer: ")

        if ans != ans_u:
            print(f"'{ans_u}' is wrong answer ;(. Correct answer was '{ans}'.")
            print(f'Let\'s try again, {name}')
            return
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')
