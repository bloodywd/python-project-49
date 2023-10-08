#!/usr/bin/env python3
from ..cli import welcome_user
from brain_games.games.data import get_data
from ..logic import play_game


def start(game):
    name = welcome_user()
    [question_to_be_asked, questions, right_answers] = get_data(game)
    play_game(name, question_to_be_asked, questions, right_answers)


def main():
    welcome_user()


if __name__ == '__main__':
    main()
