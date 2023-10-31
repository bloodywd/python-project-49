from .cli import welcome_user


ROUNDS = 3


def play_game(game=None):
    name = welcome_user()
    if game:
        print(game.DESCRITION)
        for i in range(ROUNDS):
            question, answer = (game.get_round())
            print(f'Question: {question}')
            user_answer = input("Your answer: ")
            if answer != user_answer:
                str = f"'{user_answer}' is wrong answer ;(. "
                str += f"Correct answer was '{answer}'.\n"
                str += f'Let\'s try again, {name}!'
                print(str)
                return
            else:
                print('Correct!')
        print(f'Congratulations, {name}!')
