# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import re

p = re.compile('"(https?://.*?)"', re.I)

with open('HackerNews.htm', 'r') as fr:
    doc = fr.read()

for i in p.findall(doc):
    print(i)


if __name__ == '__main__':
    pass