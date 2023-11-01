import prompt


ROUNDS = 3


def play_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game.DESCRITION)
    for i in range(ROUNDS):
        question, answer = (game.get_round())
        print(f'Question: {question}')
        user_answer = input("Your answer: ")
        if answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.\n"
                  f"Let\'s try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
