# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import json

with open('/Users/jilu/Downloads/aws-kinesis-agent.json', 'r') as fr:
    raw_j = fr.read()

j = json.loads(raw_j)

print(j)
print(json.dumps(j))

print(json.dumps(j, ensure_ascii=False, indent=4))

if __name__ == '__main__':
    pass