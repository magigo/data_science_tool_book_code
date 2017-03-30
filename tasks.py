# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import json
# from hook2.script import Task1
import requests

#
# t = Task1()
# ts = t.get_tasks()
#
# with open('/Users/jilu/Downloads/weibo_uid_friends_tags_0411', 'a') as fw:
#     for i, x in enumerate(ts):
#         resp = requests.get(x['url'])
#         fw.write(resp.content + '\n')
#         print(i)

#
# result_dict = {}
# ids_set_list = []
# with open('/Users/jilu/Downloads/weibo_user_info_0408_all', 'r') as fr:
#     for row in fr:
#         d = json.loads(row)
#         result_dict[d.get('gsid_s_c')] = list(set([user.get("idstr") for user in d.get('users', [])]))
#         ids_set_list.extend(result_dict[d.get('gsid_s_c')])
#
# id_list_2 = set(ids_set_list)

map_d = {}
with open('/Users/jilu/Downloads/weibo_user_info_0408', 'r') as fr:
    for l in fr.readlines():
        d = json.loads(l)
        map_d[tuple(d.get('gsid_s_c'))] = d.get('idstr')


result_dict = {}
ids_set_list = []
with open('/Users/jilu/Downloads/weibo_user_info_0408_all', 'r') as fr:
    for row in fr:
        d = json.loads(row)
        iid_l = list(set([user.get("idstr") for user in d.get('users', [])]))
        result_dict[map_d.get(tuple(d.get('gsid_s_c')))] = iid_l
        # ids_set_list.extend(result_dict[tuple(d.get('gsid_s_c'))])

id_list_2 = list(set(ids_set_list))

with open('/Users/jilu/Downloads/weibo_user_info_friends_map.json', 'a') as fw:
    fw.write(json.dumps(result_dict))



if __name__ == '__main__':
    pass
