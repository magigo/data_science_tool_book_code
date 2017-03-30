# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import csv
import torndb

# 连接参数
mysql = {
    "host": "localhost",
    "port": "3306",
    "database": "default",
    "password": "123456",
    "user": "test",
    "charset": "utf8"
}

# 数据库连接
db = torndb.Connection(
    host=mysql["host"] + ":" + mysql["port"],
    database=mysql["database"],
    user=mysql["user"],
    password=mysql["password"],
    charset="utf8")


with open('/Users/jilu/Downloads/ipdata.csv', 'r') as fr:
    sql = 'insert into ipdata_1000 ({}) values ({})'
    rows = csv.reader(fr)
    header = rows.next()
    _sql = sql.format(', '.join(header), ', '.join(['%s'] * len(header)))
    db.insertmany(_sql, rows)

rows = db.query('select * from ipdata_1000')
for row in rows:
    print(row)


if __name__ == '__main__':
    pass
