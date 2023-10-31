from random import randint


DESCRITION = 'What number is missing in the progression?'


def get_round():
    first_element = randint(1, 10)  # первый элемент прогрессии
    step = randint(2, 8)  # шаг между элементами прогрессии
    progression_range = randint(5, 10)  # количество элементов в прогрессии
    progression = [
        str(first_element + i * step) for i in range(progression_range)
    ]  # генерируем прогрессию
    answer_index = randint(0, progression_range - 1)  # скрытый элемент
    answer, progression[answer_index] = progression[answer_index], '..'
    return (' '.join(progression), str(answer))
