from random import randint


def even(name):
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    for i in range(0, 3):
        question_number = randint(1, 100)
        ans = (question_number % 2 == 0 and 'yes') or 'no'
        print(f'Question: {question_number}')
        ans_u = input("Your answer: ")

        if ans != ans_u:
            print(f"'{ans_u}' is wrong answer ;(. Correct answer was '{ans}'.")
            print(f'Let\'s try again, {name}')
            return
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')
