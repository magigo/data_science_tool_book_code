# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from random import choice


def throw_dice():
    return choice([1, 2, 3, 4, 5, 6])


def one_trial(trial_count=100000):
    success_count = 0
    for x in range(trial_count):
        t1 = throw_dice()
        t2 = throw_dice()
        if t1 == t2 == 1:
            success_count += 1

    return success_count / float(trial_count)


if __name__ == '__main__':
    for x in range(10):
        print(x + 1, one_trial())
