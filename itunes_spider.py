# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from collections import OrderedDict
import requests
from lxml import etree
import json

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

def get_itunes_mean_page():
    cc = OrderedDict()
    itunes_mean_page = requests.get('https://itunes.apple.com/cn/genre/ios/id36')
    itunes_mean_page_doc = etree.HTML(itunes_mean_page.content)

    for i in range(1, 4):
        items = itunes_mean_page_doc.xpath('//*[@id="genre-nav"]/div/ul[%s]/li' % i)
        for item in items:
            item_name = item.xpath('a/text()')[0]
            item_url = item.xpath('a/@href')[0]
            sub_items = item.xpath('ul')
            sub_cat_dict = OrderedDict()
            if sub_items:
                for sub_item in sub_items:
                    for c in sub_item.xpath('li/a'):
                        sub_cat_dict[c.xpath('text()')[0]] = {"sub_cat_url": c.xpath('@href')[0]}
            cc[item_name] = {'cat_url': item_url, 'sub_cat': sub_cat_dict}

    return cc


def get_top100(url):
    resp = requests.get(url)
    doc = etree.HTML(resp.content)
    cc = OrderedDict()
    for i in range(1, 4):
        items = doc.xpath('//*[@id="selectedcontent"]/div[%s]' % i)
        for item in items:
            for app in item.xpath('ul/li/a'):
                cc[app.xpath('text()')[0]] = app.xpath('@href')[0]
    return cc


if __name__ == '__main__':
    itunes_dict = get_itunes_mean_page()
    for k, v in itunes_dict.items():
        top100app = get_top100(v['cat_url'])
        itunes_dict[k]['top100'] = top100app
        if v['sub_cat']:
            for sub_cat_k, sub_cat_v in v['sub_cat'].items():
                sub_cat_top100 = get_top100(sub_cat_v['sub_cat_url'])
                v['sub_cat']['sub_cat_top100'] = sub_cat_top100
                print(sub_cat_k)
        print(k)

    with open('/Users/jilu/Downloads/itunes_top100.json', 'a') as fw:
        fw.write(json.dumps(itunes_dict, ensure_ascii=False, indent=4))
