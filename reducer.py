#!/usr/bin/env python

import sys
from collections import Counter

word_count = Counter()

for line in sys.stdin:
    line = line.strip()

    word, count = line.split('\t', 1)

    word_count[word] += int(count)

for item in word_count.items():
    print('{}\t{}'.format(*item))
