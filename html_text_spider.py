# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from lxml import etree
from glob import glob
from collections import Counter

import jieba

p_set = set()
for html in glob('/Users/jilu/Downloads/shuzilm/www.shuzilm.cn/*.html'):
    with open(html, 'r') as fr:
        doc = etree.HTML(fr.read())
    for p in filter(lambda x: x, [p.strip() for p in doc.xpath("//text()")]):
        if p.startswith("//"):
            continue
        p_set.add(p)

doc = '.'.join(p_set)
for k, v in Counter(list(jieba.cut(doc))).most_common():
    print(k, v)

if __name__ == '__main__':
    pass