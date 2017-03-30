# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import csv

# 7.1.1
with open('test.csv', 'r') as fr:
    rows = csv.reader(fr)

    for row in rows:
        print(row)

# 7.1.2
with open('csv_tutorial.csv', 'a') as fw:
    writer = csv.writer(fw)
    writer.writerow(["c1", 'c2', 'c3'])
    for x in range(10):
        writer.writerow([x, chr(ord('a') + x), 'abc'])

# 7.1.3
csv.register_dialect('pipes', delimiter='|')
with open('csv_tutorial.pipe.csv', 'r') as fr:
    rows = csv.reader(fr, dialect='pipes')

    for row in rows:
        print(row)

# 7.1.4
with open('test.csv', 'r') as fr:
    rows = csv.DictReader(fr)

    for row in rows:
        print(row)
