# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import requests
import json
from urllib import quote

headers = {
    'Cookie': 'ASP.NET_SessionId=ve0ewzgqdnq5be5vfkckctud; .ASPXUSER=2B81208FCA64899870AAB68FFBCF8C800BF395AB43B2B419F2FB399A82E574CD4054D7D9C046172380DA40914B8C34C654C771D024C9A53001E5F8DF17E552622C0182FF7C68CAFCCA45909061FD98AD741728327A90DE8A2F62CDD545AA21E0CEBC1911BAE3C2407E7824FA305DDBBA13D5B9FDA9BC77682AAB0B37E523E0D3CDA2C1A048C3F887D4BC6CEEBCD50F4E'}

headers2 = {
    'Cookie': 'ASP.NET_SessionId=ve0ewzgqdnq5be5vfkckctud; .ASPXUSER=2B81208FCA64899870AAB68FFBCF8C800BF395AB43B2B419F2FB399A82E574CD4054D7D9C046172380DA40914B8C34C654C771D024C9A53001E5F8DF17E552622C0182FF7C68CAFCCA45909061FD98AD741728327A90DE8A2F62CDD545AA21E0CEBC1911BAE3C2407E7824FA305DDBBA13D5B9FDA9BC77682AAB0B37E523E0D3CDA2C1A048C3F887D4BC6CEEBCD50F4E'}


def get_msg_stat(msg_id):
    url = 'http://web.51welink.com/CommitMsg/GetReportState?msgId={msgid}&reportState=7&total=0&page=0&iDisplayLength=10&iDisplayStart=0'.format(
        msgid=msg_id)
    resp = requests.post(url, headers=headers2)
    d = json.loads(resp.content)
    ss = d.get('data', {}).get('aaData', [{}])[0]
    s = ss.get('ReportState')
    m = ss.get('MobilePhone')
    if not s:
        print(m)


tasks = [{'s': quote('2016-03-26 00:00:01'), 'e': quote('2016-03-26 23:59:59')},
         {'s': quote('2016-03-28 00:00:01'), 'e': quote('2016-03-28 23:59:59')},
         {'s': quote('2016-03-31 00:00:01'), 'e': quote('2016-03-31 23:59:59')},
         {'s': quote('2016-04-20 00:00:01'), 'e': quote('2016-04-20 23:59:59')},
         {'s': quote('2016-04-21 00:00:01'), 'e': quote('2016-04-21 23:59:59')}]
page = 0
size = 100
for t in tasks:
    while True:
        t['size'] = size
        t['page'] = page
        t['start'] = page * size
        url = 'http://web.51welink.com/CommitMsg/PageIndexEx?startTime={s}&endTime={e}&dllProduct=1012812&msgID=&dllState=0&ckbChildAccount=false&childAccountId=&page={page}&iDisplayLength={size}&iDisplayStart={start}'.format(
            **t)
        resp = requests.post(url, headers=headers)
        d = json.loads(resp.content)
        total = d.get('aaData').get('iTotalDisplayRecords')
        msg_list = d.get('aaData', {}).get('aaData', [])
        page += 1
        msg_id_list = map(lambda x: x.get('MsgID'), msg_list)
        for msgid in msg_id_list:
            get_msg_stat(msgid)
        if (page + 1) * size >= total:
            break

if __name__ == '__main__':
    pass
