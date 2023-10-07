from random import randint


def get_what_to_ask(game):
    if game == 'even':
        return "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def get_questions(game):
    if game == 'even':
        question = randint(1, 100)
        right_answer = question % 2 == 0 and 'yes' or 'no'
        return (str(question), right_answer)


def get_data(game):
    question_to_be_asked = get_what_to_ask(game)
    questions = []
    right_answers = []
    n = 5
    for i in range(0, n):
        (question, right_answer) = get_questions(game)
        questions.append(question)
        right_answers.append(right_answer)
    return ([question_to_be_asked, questions, right_answers])

# def ... other games
