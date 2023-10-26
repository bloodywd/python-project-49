#!/usr/bin/env python3
from ..cli import welcome_user
from brain_games.games.data import get_data
from ..logic import play_game


def start(game):
    name = welcome_user()
    [question, q_and_a_list] = get_data(game)
    play_game(name, question, q_and_a_list)


def main():
    welcome_user()


if __name__ == '__main__':
    main()
