# ! /usr/bin/python
# -*- coding: utf-8 -*-


def gen_counter(name):
    count = [0]

    def counter():
        count[0] += 1
        print('Hello,', name, ',', str(count[0]) + ' access!')

    return counter


c = gen_counter('master')
c()
c()
c()
