# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import requests
from lxml import etree
import json
from collections import defaultdict

import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def get_jd_mean_page_list():
    result_dict = {}
    resp = requests.get('http://www.jd.com')
    doc_main = etree.HTML(resp.content)
    lines = doc_main.xpath("//body/div/div/div/div/ul/li/a")
    for i, main_cat in enumerate(lines):
        sub_cat_list = main_cat.xpath('a/text()')
        sub_cat_url_list = main_cat.xpath('a/@href')
        result_dict[i + 1] = {"mean_cat": dict(zip(sub_cat_list, sub_cat_url_list)), 'sub_cat_list': []}
    with open('jd_dropdown.html', 'r') as fr:
        content = fr.read()
    doc = etree.HTML(content)
    for x in range(1, 16):
        layer1 = doc.xpath('//*[@id="category-item-{}"]/div[3]/dl'.format(x))
        for layer2 in layer1:
            cat = {"cat_name": (layer2.xpath("dt/a/text()") or
                                layer2.xpath("dt/span/text()"))[0],
                   "url": (layer2.xpath("dt/a/@href") or [''])[0],
                   "sub_cat_name": dict(zip(layer2.xpath("dd/a/text()"),
                                            layer2.xpath("dd/a/@href")))}
            result_dict[x]['sub_cat_list'].append(cat)
    return json.dumps(result_dict, ensure_ascii=False, indent=4)


def get_jd_brand_list(url):
    resp = requests.get(url)
    doc = etree.HTML(resp.content)
    sub_doc = doc.xpath('//*[@id="J_selector"]/div[2]/div/div[2]/div[2]/ul')
    brand_list = []
    for item in sub_doc:
        for x in zip(item.xpath('li/@id'),
                     item.xpath('li/a/text()'),
                     item.xpath('li/a/@href')):
            brand_list.append(x)

    sub_doc = doc.xpath('//*[@id="J_selector"]/div/div')
    other_dict = defaultdict(list)
    for i, item in enumerate(sub_doc):
        title = item.xpath("div/span/text()")
        for x in zip(item.xpath('div/div/ul/li/a/text()'),
                     item.xpath('div/div/ul/li/a/@href')):
            other_dict[title[0]].append(list(x))
    return brand_list, other_dict


def run():
    jd_cat_dict = json.loads(get_jd_mean_page_list())
    for mean_key, mean_value in jd_cat_dict.items():
        for sub_cat_item in mean_value.get("sub_cat_list"):
            sub_cat_item['sub_cat_list'] = []
            for sub_cat_key, sub_cat_value in sub_cat_item.get("sub_cat_name").items():
                brand_list, other_dict = get_jd_brand_list(sub_cat_value)
                sub_cat_item['sub_cat_list'].append(
                    {"sub_cat_name": sub_cat_key, "sub_cat_url": sub_cat_value,
                     "brand_list": brand_list, "other_dict": other_dict})
                print(sub_cat_key, sub_cat_value)
    with open('jd_cat_brand_all.json', 'a') as fw:
        fw.write(json.dumps(jd_cat_dict, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    # print(get_jd_mean_page_list())
    run()
