
# play game function
def play_game(name, question_to_be_asked, questions, right_answers):
    # get list with questions and answers
    print(question_to_be_asked)
    n = 3
    for i in range(0, n):
        print(f'Question: {questions[i]}')
        ans_u = input("Your answer: ")
        if right_answers[i] != ans_u:
            str = f"'{ans_u}' is wrong answer ;(. "
            str += f"Correct answer was '{right_answers[i]}'."
            print(str)
            print(f'Let\'s try again, {name}')
            return
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')
