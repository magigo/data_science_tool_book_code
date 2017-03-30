# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import requests

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# 9.2.2
resp = requests.get('http://www.jd.com')
print(resp.status_code)
print(resp.content.decode("utf8"))

resp = requests.get('http://order.jd.com/center/list.action', headers=None)

with open('jd_test.html', 'a') as fw:
    fw.write(resp.content)
print('*' * 100)

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Accept-Encoding": "gzip, deflate, sdch",
           "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2,ja;q=0.2",
           "Cache-Control": "max-age=0",
           "Connection": "keep-alive",
           "Cookie": "lighting=275B4E6D3831EA...443768",  # cookie省略了，需要读者自行获取cookie再使用
           "Host": "order.jd.com",
           "Referer": "http//cart.jd.com/cart",
           "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"}
resp = requests.get("http://order.jd.com/center/list.action", headers=headers)

print(resp.status_code)
with open("jd_test_1.html", "a") as fw:
    fw.write(resp.content)
