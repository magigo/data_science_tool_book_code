# ! /usr/bin/python
# -*- coding: utf-8 -*-
"""本部分的代码会随着时间的推移而不能使用，请读者及时反馈，或者按照书中的方法自行寻找合适的xpath"""

from __future__ import print_function
import requests
from lxml import etree

# 9.3.1 代码
resp = requests.get('http://www.jd.com')
doc_main = etree.HTML(resp.content)
for x in doc_main.xpath("//body/div/div/div/div/ul/li/a"):
    print(*x.xpath("text()") + x.xpath("@href"))

print('*'*100)
