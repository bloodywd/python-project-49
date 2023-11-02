from random import randint


DESCRITION = 'What number is missing in the progression?'
MIN_FIRST_ELEMENT = 1
MAX_FIRST_ELEMENT = 10
MIN_STEP = 2
MAX_STEP = 8
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10


def get_round():
    start = randint(
        MIN_FIRST_ELEMENT, MAX_FIRST_ELEMENT
    )  # первый элемент прогрессии
    step = randint(MIN_STEP, MAX_STEP)  # шаг между элементами прогрессии
    progression_range = randint(
        MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH
    )  # количество элементов в прогрессии
    end = start + progression_range * step
    progression = list(range(start, end, step))  # генерируем прогрессию
    answer_index = randint(0, progression_range - 1)  # скрытый элемент
    answer, progression[answer_index] = progression[answer_index], '..'
    return ' '.join(map(str, progression)), str(answer)
