# ! /usr/bin/python
# -*- coding: utf-8 -*-

import lxml.html
import requests
from html.parser import HTMLParser
from selenium import webdriver
from selenium.webdriver.common.by import By

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Accept-Encoding": "gzip, deflate, sdch",
           "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2,ja;q=0.2",
           "Host": "www.newrank.cn",
           "Proxy-Connection": "keep-alive",
           "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36"}

headers2 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2,ja;q=0.2",
    "Cache-Control": "max-age=0",
    "Cookie": "ABTEST=6|1466414483|v1; SNUID=E27C6C76CACFFF79F0AF3F2FCB3F8154; SUID=29B6A6BC2624930A000000005767B593; SUID=29B6A6BC1620940A000000005767B594; JSESSIONID=aaa4Ic-dNWXFS7JPQaovv; SUV=1466414485832757; IPLOC=NL",
    "Host": "weixin.sogou.com",
    "Proxy-Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36"
}


def fetch(weixin_id):
    url = 'http://www.newrank.cn/public/info/detail.html?account=%s' % weixin_id
    try:
        r = requests.get(url, headers=headers, timeout=10)
        doc = lxml.html.fromstring(r.content)
        lines = doc.xpath('//*[@class="detail-fans-counts"]/text()')
        return [weixin_id] + list(map(lambda x: x.strip(), lines))
    except:
        return []


h = HTMLParser()
driver = webdriver.PhantomJS()


def fetch2(weixin_id):
    url = 'http://weixin.sogou.com/weixin?type=1&query=%s' % weixin_id
    r = requests.get(url, headers=headers2, timeout=10)
    doc = lxml.html.fromstring(r.content)
    lines = doc.xpath('//*[@id="main"]/div/div[2]/div/div/@href')
    print(lines)
    if lines:
        u = h.unescape(lines[0])
        print(u)
        if u:
            print(u)
            sr = driver.get(u)
            print(sr.find_element_by_xpath('//*[@id="history"]/div[10]/div[2]/div[8]/div/p[2]'))


id_list = []
with open('/Users/jilu/Downloads/weixin-accounts-50000.txt', 'r') as fr:
    #     with open('/home/ubuntu/weixin-accounts-50000.txt', 'r') as fr, open('/home/ubuntu/weixin-newrank.txt', 'w') as fw:
    for line in fr.readlines()[1:]:
        weixin_id = line.strip()
        id_list.append(weixin_id)
        #       fw.write('\x01'.join(fetch(weixin_id)) + '\n')
        fetch2(weixin_id)
        break
