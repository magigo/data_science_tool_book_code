# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import json
import requests

# key_set = set()
#
# result = {}
# url = 'http://api.weibo.cn/2/users/show?gsid={}&s={}&c={}&has_profile=1&has_badges=1&has_extend=1&has_member=1&sflag=1'
# with open('/Users/jilu/Downloads/weibo_user_friends_0412', 'r') as fr1, \
#         open('/Users/jilu/Downloads/weibo_user_info_0412', 'r') as fr2:
#     user_info_dict = {}
#     for r2 in fr2:
#         j2 = json.loads(r2)
#         user_info_dict[tuple(j2.get('gsid_s_c'))] = j2.get('idstr')
#     for row1 in fr1:
#         d1 = json.loads(row1)
#         u = user_info_dict.get(tuple(d1.get('gsid_s_c')))
#
#         friends = map(lambda x: x.get('idstr'), d1.get("users", []))
#         if u and not friends:
#
#             resp = requests.get(url.format(*d1.get('gsid_s_c')))
#             dd = json.loads(resp.content)
#             u = dd.get("idstr")
#         result[u] = friends
#
# result_ids = result.keys()

# with open('/Users/jilu/Downloads/weibo_user_friends_0412.json', 'a') as fw:
#     fw.write(json.dumps(result))
#


#
# import torndb
#
# mysql = {
#     "host": "rtb-v2.c0lj6shdz7lj.rds.cn-north-1.amazonaws.com.cn",
#     "port": "3306",
#     "database": "atweiquan",
#     "password": "Detective#891534",
#     "user": "dev_jilu",
#     "charset": "utf8"
# }
#
# db = torndb.Connection(
#     host=mysql["host"] + ":" + mysql["port"],
#     database=mysql["database"],
#     user=mysql["user"],
#     password=mysql["password"],
#     max_idle_time=3600,
#     charset="utf8"
# )
#
#
# id_list = []
# for row in db.query(
#         'select id, gsid, s, c from weixin_imei_user_info'):
#     if not row:
#         continue
#     id_list.append(','.join(map(str, [row.get(x) for x in ['id', 'gsid', 's', 'c']])) + '\n')
#
# with open('/Users/jilu/Downloads/weibo_ids_0412', 'a') as fw:
#     fw.writelines(id_list)
#
import re
from collections import defaultdict
from itertools import chain
#
pt = re.compile('>(.+)<')

stop_app_list = [u'三星', u'酷派', u'YunOS', u'联想', u'小米', u'索尼',
                 u'iPhone', u'金立', u'HUAWEI', u'乐蛙', u'乐Max' u'魅蓝',
                 u'纤薄王者', u'Dopool', u'坚果', u'中国移动定制', u'中兴',
                 u'ZTE', u'HTC', u'Pioneer', u'MOTO', u'摩托罗拉', u'荣耀',
                 u'OPPO', u'奥克斯', u'Flyme', u'美图手机', u'nubia', u'红米',
                 u'vivo',u'小辣椒', u'一加', u'乐1s', u'华为', u'Lumia', u'Sony',
                 u'魅族', u'大神手机', u'诺基亚', u'samsung']

app_set = set()
calc = 0
_result = defaultdict(list)
with open('/Users/jilu/Downloads/log', 'r') as fr:
    for row in fr:
        d = json.loads(row)
        result = d.get('result', {})
        total = result.get('total_number')
        statuses = result.get('statuses', [])
        if statuses:
            user = str(statuses[0].get('user', {}).get('id'))
            useful_status_info = list(set(reduce(lambda x, y: x + y, [
                pt.findall(status.get('source')) for status in
                statuses])))
            _useful_status_info = []
            for isi in useful_status_info:
                flag = 0
                for iiis in stop_app_list:
                    if iiis in isi:
                        flag = 1

                if not flag:
                    _useful_status_info.append(isi)
                    app_set.add(isi)
            _result[user] = _useful_status_info
            # for it in _useful_status_info:
            #     app_set.add(it)
            # print(user, useful_status_info)


# print(*app_set)
            for iii in statuses:
                t = iii.get('created_at')
                geo = iii.get('geo')
                # if geo:
                #     _g = geo.get('coordinates', [])
                #     if not _g:
                #         continue
                #     _result[user].append(_g + [t])
                #     continue
                for ii in iii.get('annotations', []):
                    try:
                        place = ii.get('place', {})
                        __g = place
                        __g['time'] = t
                        _result[user].append(__g)
                    except AttributeError:
                        continue
# for k, v in _result.items():
#     _result[k] = filter(lambda x: x, v)

with open('/Users/jilu/Downloads/weibo_user_geo_0412.json', 'w') as fw:
    fw.write(json.dumps(_result))

    # useful_status_info = [(pt.findall(status.get('source')), status.get('created_at'), status.get('source_type')) for status in statuses]
    # for s in useful_status_info:
    #     if s[0]:
    #         _result[user].append((s[0][0], s[1], s[2]))
    #
    #     else:
    #         _result[user].append((s, s[1], s[2]))

# with open('/Users/jilu/Downloads/weibo_user_mod_0412.json', 'w') as fw:
#     fw.write(json.dumps(_result))
#
# import time
# import numpy as np
# import arrow
# from collections import Counter, defaultdict
#
# stop_word = [u'搜索', u'浏览器', u'客户端', u'中文', u'分享', u'豆瓣', u'微博', u'乐视', u'投票', u'网易', u'红包', u'短信', u'卡券', u'支付宝', u'相册',
#              u'美图', u'播放器', u'今日头条', u'应用', u'日报', u'平台', u'话题', u'秒拍', u'k歌', u'测试', u'APP', u'购物', u'小咖秀', u'FM', u'蘑菇街',
#              u'管家', u'微盘']
# cc = Counter()
# result = defaultdict(list)
# with open('/Users/jilu/Downloads/weibo_user_mod_0412.json', 'r') as fr:
#     d = json.loads(fr.read())
# for uid, mods in d.items():
#     _mods = sorted([(mod[0], arrow.get(mod[1].split(' ', 1)[-1], 'MMM DD HH:mm:ss Z YYYY')) for mod in mods],
#                    key=lambda x: x[1])
#     # print(d, _mods)
#     np_mod = np.array(_mods)
#     mod, ts = np_mod[:, 0], np_mod[:, 1]
#     l_mod = list(mod)
#
#     try:
#         for item in set(mod):
#             flag = 0
#             for w in stop_word:
#                 if w in item:
#                     flag = 1
#             if flag:
#                 continue
#             first, last = l_mod.index(item), -l_mod[::-1].index(item) - 1
#             # print(uid, item, ts[first], ts[last])
#             result[uid].append((item, str(ts[first]), str(ts[last])))
#     except TypeError:
#         continue
#
# with open('/Users/jilu/Downloads/weibo_user_mod_0412_.json', 'w') as fw:
#     fw.write(json.dumps(result))
#
# #
# for k, v in cc.most_common():
#     print(k, v)
#
# print(sum(cc.values()))


from glob import glob
import fileinput
result = {}


for line in fileinput.input(glob('/Users/jilu/Downloads/weibo_user_info_04*')):
    d = json.loads(line)
    try:
        uid = d.get('idstr')
        description = {'d': d.get('description', ''), 'v': d.get('verified_reason', '')}
        edu = d.get('education_info', [])
        for e in edu:
            if e:
                e.pop('visible')
                e.pop('type')
                e.pop('id')
        result[uid] = {'uid': uid, 'desc': description, 'edu': edu}
    except AttributeError:
        print(d)

with open('/Users/jilu/Downloads/weibo_user_other_info_0412.json', 'w') as fw:
    fw.write(json.dumps(result))



if __name__ == '__main__':
    pass
