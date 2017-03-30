# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import csv


def reader_csv():
    with open('/Users/jilu/Downloads/test.csv', 'r') as fr:
        rows = csv.reader(fr)

        for row in rows:
            print(row)


def write_csv():
    with open('/Users/jilu/Downloads/csv_tutorial.csv', 'w') as fw:
        writer = csv.writer(fw, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(["c1", 'c2', 'c3'])
        for x in range(10):
            writer.writerow([x, chr(ord('a') + x), 'abc'])


def reader_dialect():
    csv.register_dialect('pipes', delimiter='|')
    with open('/Users/jilu/Downloads/csv_tutorial.pipe.csv', 'r') as fr:
        rows = csv.reader(fr, dialect='pipes')

        for row in rows:
            print(row)

with open('/Users/jilu/Downloads/test.csv', 'r') as fr:
    rows = csv.DictReader(fr)

    for row in rows:
        print(row)

if __name__ == '__main__':
    pass
