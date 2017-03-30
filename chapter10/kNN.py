# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from collections import Counter, defaultdict
import random
import csv

import numpy as np
import matplotlib.pyplot as plt


def get_data(loc='iris/Iris.csv'):
    with open(loc, 'r') as fr:
        lines = csv.reader(fr)
        data_file = np.array(list(lines))
    data = data_file[1:, 1:-1].astype(float)
    labels = data_file[1:, -1]
    return data, labels


def classify(input_data, train_data, labels, k):
    data_size = train_data.shape[0]
    diff = np.tile(input_data, (data_size, 1)) - train_data
    sqrt_diff = diff ** 2
    sqrt_distance = sqrt_diff.sum(axis=1)
    distance = np.sqrt(sqrt_distance)
    sorted_index = distance.argsort()
    class_count = Counter(labels[sorted_index[:k]])
    return class_count.most_common()[0][0]


def draw():
    style_list = ['rs', 'go', 'bv']
    data, labels = get_data()
    print(data)
    print(labels)
    cc = defaultdict(list)
    for i, d in enumerate(data):
        cc[labels[i]].append(d)
    p_list = []
    c_list = []
    for i, (c, ds) in enumerate(cc.items()):
        draw_data = np.array(ds)
        p = plt.plot(draw_data[:, 0], draw_data[:, 1], style_list[i])
        p_list.append(p)
        c_list.append(c)
    plt.legend(map(lambda x: x[0], p_list), c_list)
    plt.title(u'鸢尾花萼片的长度和宽度')
    plt.xlabel(u'萼片的长度(cm)')
    plt.ylabel(u'萼片的宽度 (cm)')
    plt.show()


def try_once():
    data, labels = get_data()
    index = range(len(data))
    data = data[index]
    labels = labels[index]
    random.shuffle(index)
    labels = labels[index]
    data = data[index]
    input_data = data[-1]
    data = data[:-1]
    input_label = labels[-1]
    labels = labels[:-1]
    print('input_index:', index[-1])
    print('true class:', input_label)
    print(classify(input_data, data, labels, 5))


if __name__ == '__main__':
    draw()
    # for x in range(5):
    #     try_once()
    #     print('='*10)
