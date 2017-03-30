# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
# from unittest import TestCase
#
#
# class Test(TestCase):
#     @unittest.skip('abc')
#     def test_db_connection(self):
#         from zhihu_spider import MySQLHelper, mysql
#
#         db = MySQLHelper(
#             host=mysql["host"] + ":" + mysql["port"],
#             database=mysql["database"],
#             user=mysql["user"],
#             password=mysql["password"],
#             charset="utf8")
#
#         print(db.question_sql)
#
#     def test_question_ftecher(self):
#         from zhihu_spider import fetch_question_from_topic
#         fetch_question_from_topic(19555634)


if __name__ == '__main__':
    # unittest.main()
    from zhihu_spider import collect_target_user

    collect_target_user()