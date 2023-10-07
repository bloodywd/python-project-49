#!/usr/bin/env python3
from ..cli import welcome_user
from ..games import get_data
from ..logic import play_game


def main():
    name = welcome_user()
    [question_to_be_asked, questions, right_answers] = get_data('progression')
    play_game(name, question_to_be_asked, questions, right_answers)


if __name__ == '__main__':
    main()
