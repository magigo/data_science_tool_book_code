# ! /usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import torndb



mysql = {
    "host": "rtb-v2.c0lj6shdz7lj.rds.cn-north-1.amazonaws.com.cn",
    "port": "3306",
    "database": "wemedia",
    "password": "Detective#891534",
    "user": "dev_jilu",
    "charset": "utf8"
}
db = torndb.Connection(
    host=mysql["host"] + ":" + mysql["port"],
    database=mysql["database"],
    user=mysql["user"],
    password=mysql["password"],
    charset="utf8")

u_list = []
with open('/Users/jilu/Downloads/weixin-accounts-50000.txt', 'r') as fr:
    for line in fr.readlines()[1:]:
        weixin_id = line.strip()
        u_list.append(weixin_id)
sql = "select alias, __biz from wx_user_info_2 where alias in (%s)" % ', '.join(map(lambda x: "'" + x + "'", u_list))
rows = db.query(sql)
with open('/Users/jilu/Downloads/weixin-alias-biz', 'w') as fw:
    for row in rows:
        a = row.get('alias')
        b = row.get('__biz')
        fw.write(a + '\x01' + b + '\n')



if __name__ == '__main__':
    pass
