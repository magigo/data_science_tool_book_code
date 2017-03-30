# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from glob import glob
import fileinput
import json
from collections import defaultdict


idlist = set()
cc = defaultdict(list)
with open('/Users/jilu/Downloads/0422/all', 'r') as fr2:
    filter_set = set(map(lambda x: x.strip(), fr2.readlines()))
    for line in fileinput.input(glob('/Users/jilu/Downloads/0422/*/*')):
        user, friends = line.strip().split('|')
        if user not in filter_set:
            continue
        if not friends:
            continue
        friend_list = friends.split(',')
        cc[user].extend(friend_list)
        idlist.add(user)
        for f in friend_list:
            idlist.add(f)

with open('/Users/jilu/Downloads/idlist', 'w') as fw1, open('/Users/jilu/Downloads/idmap', 'w') as fw2:
    fw1.writelines(map(lambda x: str(x) + '\n', list(idlist)))
    json.dump(cc, fw2, ensure_ascii=False, indent=4)



if __name__ == '__main__':
    pass
