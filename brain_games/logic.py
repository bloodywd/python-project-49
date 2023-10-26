def play_game(name, question, q_and_a_list):
    # get list with questions and answers
    print(question)
    ROUNDS = 3
    for i in range(0, ROUNDS):
        question, answer = q_and_a_list[i]
        print(f'Question: {question}')
        user_answer = input("Your answer: ")
        if answer != user_answer:
            str = f"'{user_answer}' is wrong answer ;(. "
            str += f"Correct answer was '{answer}'."
            print(str)
            print(f'Let\'s try again, {name}!')
            return
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')
