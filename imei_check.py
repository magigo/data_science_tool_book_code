# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import json
import requests


def get_imei_info(imei):
    url = 'http://www.imei.info/api/checkimei/'
    data = {"login": 'magigo',
            'password': 'detective',
            'imei': imei}
    r = requests.post(url, data=data)
    print(r.status_code, r.content)
    return json.loads(r.content)


if __name__ == '__main__':
    print(get_imei_info("352580061207937"))
