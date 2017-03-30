# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import json
import requests

friend_url = 'https://api.weibo.cn/2/friendships/friends?page={}&gsid={}&s={}&c={}&has_profile=1&&has_badges=1&has_extend=1&has_member=1&sflag=1&count=200'
timeline_url = 'http://api.weibo.cn/2/statuses/user_timeline?page={}&gsid={}&s={}&c={}&count=100&trim_user=1'  # page从1开始
tags_url = 'https://api.weibo.com/2/tags/tags_batch.json?access_token=2.00UpkQJB0SUt7K1c5e875b114mh3EB&uids=%s'  # 每小时每个ip4万次


def get_friends(user_info):
    """
    输入的参数中必须为包含gsid_s_c这个参数的字典
    example:
        >>> r = get_friends({"gsid_s_c": ["_2A2548QfuDeTxGeRL61sQ8CfNyDiIHXVZpxwmrDV6PUJbrdANLU7FkWpsgaZ11pspTMxCpcF4zp2yXCfxtA..", "240c9f0d","android"]})
        >>> print(r)
    """
    r_list = []

    def _get_friends(user_info, page=1):
        gsid_s_c = user_info.get('gsid_s_c')
        resp = requests.get(friend_url.format(page, *gsid_s_c), timeout=10)
        d = json.loads(resp.content)
        friend_ids = [u.get('idstr') for u in d.get('users', [])]
        next_cursor = d.get('next_cursor')
        r_list.extend(friend_ids)
        if next_cursor:
            page += 1
            _get_friends(user_info, page)
        else:
            return friend_ids

    _get_friends(user_info)
    return list(set(r_list))


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i + n]


def get_user_tags(uid_list):
    for ids in chunks(uid_list, 20):
        yield json.loads(requests.get(tags_url % ','.join(map(str, ids)), timeout=10).content)


def get_one_friends_tags(user_info):
    """
    直接获取某个微博用户所有好友的标签, 不包含这名用户本身
    example:
        >>> print(get_one_friends_tags({"gsid_s_c": [
            "_2A2548QfuDeTxGeRL61sQ8CfNyDiIHXVZpxwmrDV6PUJbrdANLU7FkWpsgaZ11pspTMxCpcF4zp2yXCfxtA..", "240c9f0d",
            "android"]}))
    """
    r = get_friends(user_info)
    ret_list = []
    for item in reduce(lambda x, y: x + y, [[]] + [tags for tags in get_user_tags(r)]):
        ret_list.extend(item.get('tags'))
    return ret_list


if __name__ == '__main__':
    # example 1
    # r = get_friends({"gsid_s_c": [
    #     "_2A2548QfuDeTxGeRL61sQ8CfNyDiIHXVZpxwmrDV6PUJbrdANLU7FkWpsgaZ11pspTMxCpcF4zp2yXCfxtA..", "240c9f0d",
    #     "android"]})
    # for tags in get_user_tags(r):
    #     print(tags)


    # example 2
    print(json.dumps(get_one_friends_tags({"gsid_s_c": [
        "_2A2548QfuDeTxGeRL61sQ8CfNyDiIHXVZpxwmrDV6PUJbrdANLU7FkWpsgaZ11pspTMxCpcF4zp2yXCfxtA..", "240c9f0d",
        "android"]}), ensure_ascii=False, indent=4))
    #
    # from sys import argv
    # input, output = argv[1], argv[2]
    # with open(input, 'r') as fr, open(output, 'w') as fw:
    #     for line in fr:
    #         uid, gsid, s, c = line.strip().split('\t')
    #         d = {'uid': uid, 'gsid_s_c': [gsid, s, c]}
    #         tag_list = get_one_friends_tags(d)
    #         fw.write(json.dumps({'uid': d.get('uid'), 'tag_list': tag_list}) + '\n')

