import signal
import sys
import asyncio
import aiohttp
import lxml.html

loop = asyncio.get_event_loop()
loop.slow_callback_duration = 0.5
client = aiohttp.ClientSession(loop=loop)


async def get_json(client, url):
    async with client.get(url) as response:
        return await response.read(), response.status


async def get_reddit_top(topic_id, client):
    url = 'http://www.newrank.cn/public/info/detail.html?account=%s' % topic_id
    data1, code = await get_json(client, url)
    if code != 200:
        pass
    else:
        try:
            doc = lxml.html.fromstring(data1)
            lines = doc.xpath('//*[@class="detail-fans-counts"]/text()')
            print([topic_id] + list(map(lambda x: x.strip(), lines)))
        except:
            pass


def signal_handler(signal, frame):
    loop.stop()
    client.close()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

id_list = []
with open('/Users/jilu/Downloads/weixin-accounts-50000.txt', 'r', encoding='utf8') as fr:
    for line in fr.readlines():
        weixin_id = line.strip()
        id_list.append(weixin_id)

for topic_id in id_list:
    asyncio.ensure_future(get_reddit_top(topic_id, client))

loop.run_forever()
