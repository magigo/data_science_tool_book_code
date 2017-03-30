# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
# 7.3.1
import csv

with open('ipdata.csv', 'r') as fr:
    sql = 'insert into ipdata_1000 ({}) values ({})'
    rows = csv.reader(fr)
    header = rows.next()
    for row in rows:
        print(sql.format(', '.join(header), ', '.join(row)))
