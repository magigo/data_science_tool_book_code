# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pandas as pd
from collections import OrderedDict

import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def read_excel():
    """读取人口普查分民族/年龄/性别统计
    """
    excel_content = pd.read_excel('/Users/jilu/Downloads/A0201.xls',
                                  skiprows=2)
    race_list = excel_content.irow(0)[1:][::3].tolist()
    age_list = map(lambda x: str(x).replace(' ', ''),
                   excel_content.icol(0)[2:].tolist())
    excel_content = pd.read_excel('/Users/jilu/Downloads/A0201.xls',
                                  skiprows=4)

    def get_num(lines):
        ret_dict = OrderedDict()
        for k, v in lines.to_dict().items():
            new_v_dict = OrderedDict()
            for vk, vv in v.items():
                new_v_dict[age_list[int(vk)]] = vv
            ret_dict[k.split('.', 1)[0]] = new_v_dict  # 将每一列表头中"."号后面的字符去掉
        return ret_dict

    result_dict = OrderedDict()
    for i, x in enumerate(range(1, 178, 3)):
        ids = [x, x + 1, x + 2]
        race_list[i] = race_list[i].replace(' ', '')
        result_dict[race_list[i]] = get_num(excel_content.icol(ids))

    return result_dict


def calc_mean(d):
    total = 0
    total_age = 0
    for age, count in d.items():
        if age.isdigit():
            total += count
            total_age += int(age) * count
    return total_age / float(total)


def calc_median(d):
    total = d.get("总计")
    half_total = total / 2.0
    count_total = 0
    for age, count in d.items():
        if age.isdigit():
            count_total += count
        if count_total > half_total:
            break
    return age


def get_race_num():
    from collections import defaultdict
    d = read_excel()
    cc = defaultdict(list)
    for t in [u"小计", u"男", u"女"]:
        for k, v in d.items():
            if k == u"合计" or k == u"汉族":
                continue
            cc[t].append((k, v.get(t).get("总计")))

    race_num_dict = OrderedDict()
    for k, v in cc.items():
        race_num_dict[k] = dict(v)

    return race_num_dict


def calc_variance(d):
    mean = sum(d.values()) / float(len(d.values()))
    total = 0
    for k, v in d.items():
        total += (v - mean) ** 2
    return total / float(len(d.values()))


def calc_pmf(data_list):
    ret_list = []
    total = sum(data_list)
    for item in data_list:
        ret_list.append(float(item) / total)
    return ret_list


# 计算年龄的中位数,
# 计算人口的平均年龄对于各个种族可能还算公平, 但是计算每个种族的平均人数就很不公平了,需要计算方差
# 计算分布, 年龄分布(正态分布)
# 各民族男女比例直方图
#
#
if __name__ == '__main__':
    import json
    import math
    import matplotlib.pyplot as plt

    # print(json.dumps(read_excel(), ensure_ascii=False, indent=4))
    d = read_excel()
    # for t in [u"合计", u"男", u"女"]:
    #     mean_count = calc_mean(d.get(u"合计").get(t))
    #     print("{}人口平均年龄".format(t), mean_count)
    # print('=' * 10)
    # for t in [u"合计", u"男", u"女"]:
    #     median_count = calc_median(d.get(u"合计").get(t))
    #     print("{}人口中位数年龄".format(t), median_count)
    #
    # print("全国各民族人口平均数".format(1332810869 / 58.0))
    # d = get_race_num()
    # for k, v in d.items():
    #     var = calc_variance(v)
    #     std = math.sqrt(var)
    #     print(k, var, std)
    # print(json.dumps(d, ensure_ascii=False, indent=4))

    # men_num = d.get(u"合计").get(u"男")
    # women_num = d.get(u"合计").get(u"女")
    # bottom = [0] * 100
    # color_list = ['b', 'y']
    # p_list = []
    # for i, item in enumerate([men_num, women_num]):
    #     dr = OrderedDict([(int(k), int(v)) for k, v in item.items() if k.isdigit()])
    #     age_list, num_list = dr.keys(), dr.values()
    #     num_list = calc_pmf(num_list)
    #     p = plt.bar(age_list, num_list, bottom=bottom, color=color_list[i])
    #     bottom = num_list
    #     p_list.append(p)
    # plt.ylabel('Population')
    # plt.xlabel('Age')
    # plt.title('The Distribution of Population')
    #
    # plt.legend((p_list[0][0], p_list[1][0]), ('Men', 'Women'))
    # plt.show()

    total_num = d.get(u"合计").get(u"合计")
    fracs = []
    labels = []
    for k, v in total_num.items():
        if k.endswith("岁"):
            fracs.append(v)
            labels.append(k)

    plt.pie(fracs, labels=labels, autopct='%1.1f%%', startangle=90)

    plt.title(u'全国人口分布')
    plt.show()


