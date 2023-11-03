from random import randint


DESCRITION = 'What number is missing in the progression?'


def get_question_and_answer():
    start = randint(1, 10)  # первый элемент прогрессии
    step = randint(2, 8)  # шаг между элементами прогрессии
    length = randint(5, 10)  # количество элементов в прогрессии
    end = start + length * step
    progression = list(range(start, end, step))  # генерируем прогрессию
    answer_index = randint(0, length - 1)  # скрытый элемент
    answer, progression[answer_index] = progression[answer_index], '..'
    return ' '.join(map(str, progression)), str(answer)
