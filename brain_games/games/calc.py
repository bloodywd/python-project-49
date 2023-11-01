from random import randint, choice


DESCRITION = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 25
OPERATIONS = {
    'sum': {
        'action': lambda x, y: x + y,
        'sign': '+',
    },
    'dif': {
        'action': lambda x, y: x - y,
        'sign': '-',
    },
    'multiply': {
        'action': lambda x, y: x * y,
        'sign': '*',
    },
}


def get_round():
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    number2 = randint(MIN_NUMBER, MAX_NUMBER)
    operation_names = list(OPERATIONS.keys())  # Создаем список операций
    operation_name = choice(operation_names)  # Выбираем случайную операцию
    operation = OPERATIONS[operation_name]
    right_answer = operation['action'](number1, number2)
    return (f'{number1} {operation["sign"]} {number2}', str(right_answer))
