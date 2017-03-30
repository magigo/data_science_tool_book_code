# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com")
# print(driver.find_element_by_xpath('your xpath'))
print(driver.title)
print(driver.page_source)

if __name__ == '__main__':
    pass