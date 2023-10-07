#!/usr/bin/env python3
from ..cli import welcome_user
from ..games import even


def main():
    name = welcome_user()
    even(name)


if __name__ == '__main__':
    main()
