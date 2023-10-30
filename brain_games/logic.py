from .games import calc
from .games import even
from .games import gcd
from .games import prime
from .games import progression
from .cli import welcome_user


ROUNDS = 3
GAMES = {
    'calc': calc,
    'even': even,
    'gcd': gcd,
    'prime': prime,
    'progression': progression,
}


def play_game(game_name=None):
    name = welcome_user()
    if game_name:
        game = GAMES[game_name]
        print(game.DESCRITION)
        for i in range(0, ROUNDS):
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
