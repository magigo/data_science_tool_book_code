# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from lxml import etree
import json
from collections import OrderedDict
import abc
import warnings
import six
import requests

import requests
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
try:
    from selenium import webdriver
except ImportError:
    warnings.warn('导入selenium模块失败, 不可以使用PhantomJS抓取器')


def get_tmall_mean_cat():
    with open('/Users/jilu/Downloads/tmall.html', 'r') as fr:
        content = fr.read()
    doc = etree.HTML(content)

    cat_list = []
    for i, main_cat in enumerate(doc.xpath('//*[@id="content"]/div/div/div/div/ul/li')):
        first_cat = zip(main_cat.xpath('a/text()'), main_cat.xpath('a/@href'))
        if not first_cat:
            continue
        cat_list.append({"cat": first_cat})

    sub_cat_list = []
    for i, item in enumerate(doc.xpath('//*[@id="content"]/div/div/div/div')):
        second_items = item.xpath('div/div/div/div')
        second_cat_list = []
        for second_item in second_items:
            if not second_item.xpath('h3/a/text()'):
                continue
            second_cat = OrderedDict(zip(second_item.xpath('h3/a/text()'), second_item.xpath('h3/a/@href')))
            second_cat.pop(u"更多", '')
            second_cat = list(second_cat)
            _third_item = second_item.xpath('div')
            third_item_list = []
            for thi_item in _third_item:
                third_item_list.append(zip(thi_item.xpath('div/a/text()'), thi_item.xpath('div/a/@href')))
            second_cat_list.append(dict(zip(second_cat, third_item_list)))

        if not second_cat_list:
            continue
        sub_cat_list.append(second_cat_list)

    for i, item in enumerate(sub_cat_list):
        cat_list[i]["sub_cat"] = item

    with open('/Users/jilu/Downloads/tamll_cat.json', 'a') as fw:
        fw.write(json.dumps(cat_list, ensure_ascii=False, indent=4))


with open('/Users/jilu/Downloads/tamll_cat.json', 'r') as fr:
    doc = json.loads(fr.read())

ph_js_driver = webdriver.PhantomJS(service_log_path='/tmp/ph.js.log')


def get_tmall_brand(url):
    ph_js_driver.get(url)
    el = ph_js_driver.page_source
    doc = etree.HTML(el)
    item_dict = OrderedDict()
    for item in doc.xpath('//*[@id="J_NavAttrsForm"]/div/div/div'):

        _class = item.xpath('@class')[0]
        if not _class.startswith("j_"):
            continue

        if _class in ['j_MoreAttrsCont', 'j_Cate attr']:
            if _class == 'j_Cate attr':
                try:
                    sub_title = map(lambda x: x.strip(), filter(lambda x: x.strip(), item.xpath('div[1]/a/text()')))[0]
                except IndexError:
                    sub_title = map(lambda x: x.strip(), filter(lambda x: x.strip(), item.xpath('div[1]/text()')))[0]
                sub_cat = map(lambda x: x.strip(), item.xpath('div[2]/ul/li[1]/a/b/text()'))
                sub_href = map(lambda x: x.strip(), item.xpath('div[2]/ul/li[1]/a/b/@href'))
                item_dict[sub_title] = OrderedDict(zip(sub_cat, sub_href))
                continue

            sub_items = item.xpath('div')
            for sub_item in sub_items:
                sub_title = map(lambda x: x.strip(), filter(lambda x: x.strip(), sub_item.xpath('div/text()')))[0]
                sub_cat = map(lambda x: x.strip(), sub_item.xpath('div/ul/li/a/text()'))
                sub_href = map(lambda x: x.strip(), sub_item.xpath('div/ul/li/a/@href'))
                item_dict[sub_title] = OrderedDict(zip(sub_cat, sub_href))
            continue
        else:
            title = map(lambda x: x.strip(), filter(lambda x: x.strip(), item.xpath('div/text()')))[0]
            cat = map(lambda x: x.strip(), item.xpath('div/ul/li/a/text()'))
            href = map(lambda x: x.strip(), item.xpath('div/ul/li/a/@href'))
        item_dict[title] = OrderedDict(zip(cat, href))
    return item_dict


# r = get_tmall_brand('https://list.tmall.com/search_product.htm?spm=875.7789098.2015106.13.uA3Ef7&acm=lb-zebra-17931-289102.1003.2.495755&q=%D1%A9%B7%C4%C9%C0&vmarket=100015571&aldid=2zG9PW5U&from=.list.pc_1_searchbutton&type=p&scm=1003.2.lb-zebra-17931-289102.ITEM_1458162318822_495755&pos=11')
# print(json.dumps(r, ensure_ascii=False, indent=4))

#
# result_dict = OrderedDict()
# for i, item in enumerate(doc):
#     c = item.get('cat')
#     r_list = []
#     for sub_item in item.get("sub_cat", []):
#         sub_item.pop(u"特色品牌", "")
#         if not sub_item:
#             continue
#
#         sub_cat_dict = OrderedDict()
#         for sub_item_key, sub_item_value in sub_item.items():
#             print(sub_item_key)
#             brand_list = []
#             for sub_cat in sub_item_value:
#                 cat_name = sub_cat[0]
#                 cat_url = sub_cat[1]
#                 if cat_url.startswith("//list"):
#                     cat_url = 'https:' + cat_url
#                 if not cat_url.startswith('https://list'):
#                     continue
#                 print(cat_url)
#                 brand_dict = get_tmall_brand(cat_url)
#                 brand_list.append(brand_dict)
#             sub_cat_dict[sub_item_key] = brand_list
#         r_list.append(sub_cat_dict)
#     result_dict[i] = {"sub_cat": r_list, 'cat': c}
#
# with open('/Users/jilu/Downloads/tamll_cat_all.json', 'a') as fw:
#     fw.write(json.dumps(result_dict, ensure_ascii=False, indent=4))
#

ph_js_driver.get("http://www.jd.com")
el = ph_js_driver.page_source
print(el)
ph_js_driver.quit()

if __name__ == '__main__':
    pass
