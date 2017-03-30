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
    excel_content = pd.read_excel("A0201.xls",
                                  skiprows=2)
    race_list = excel_content.irow(0)[1:][::3].tolist()
    # 去掉字符中间的空格
    age_list = map(lambda x: str(x).replace(" ", ""),
                   excel_content.icol(0)[2:].tolist())
    excel_content = pd.read_excel("A0201.xls",
                                  skiprows=4)

    def get_num(lines):
        ret_dict = OrderedDict()
        for k, v in lines.to_dict().items():
            new_v_dict = OrderedDict()
            for vk, vv in v.items():
                new_v_dict[age_list[int(vk)]] = vv
            ret_dict[k.split(".", 1)[0]] = new_v_dict  # 将每一列表头中"."号后面的字符去掉
        return ret_dict

    result_dict = OrderedDict()
    for i, x in enumerate(range(1, 178, 3)):
        ids = [x, x + 1, x + 2]
        race_list[i] = race_list[i].replace(" ", "")
        result_dict[race_list[i]] = get_num(excel_content.icol(ids))

    return result_dict


# 8.1.2 增加的代码
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


# 8.1.3 增加的代码
def get_race_num():
    from collections import defaultdict
    d = read_excel()
    cc = defaultdict(list)
    for t in [u"小计", u"男", u"女"]:
        for k, v in d.items():
            if k == u"合计":
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


# 8.1.4 中增加的代码
def calc_pmf(data_list):
    ret_list = []
    total = sum(data_list)
    for item in data_list:
        ret_list.append(float(item) / total)
    return ret_list


if __name__ == "__main__":
    import json

    print(json.dumps(read_excel(), ensure_ascii=False, indent=4))

    # 8.1.2 增加的代码
    d = read_excel()
    for t in [u"合计", u"男", u"女"]:
        mean_count = calc_mean(d.get(u"合计").get(t))
        print("{}人口平均年龄".format(t), mean_count)
    print('*' * 100)
    for t in [u"合计", u"男", u"女"]:
        median_count = calc_median(d.get(u"合计").get(t))
        print("{}人口中位数年龄".format(t), median_count)
    print('*' * 100)

    # 8.1.3 增加的代码
    import math

    d = get_race_num()
    print(json.dumps(d, ensure_ascii=False, indent=4))
    for k, v in d.items():
        var = calc_variance(v)
        std = math.sqrt(var)
        print(k, var, std)

    # 8.1.4 增加的代码, 8.2.2 柱状图代码
    import matplotlib.pyplot as plt

    d = read_excel()
    men_num = d.get(u"合计").get(u"男")
    women_num = d.get(u"合计").get(u"女")
    bottom = [0] * 100
    color_list = ['b', 'y']
    p_list = []
    for i, item in enumerate([men_num, women_num]):
        dr = OrderedDict([(int(k), int(v)) for k, v in item.items() if k.isdigit()])
        age_list, num_list = dr.keys(), dr.values()
        # num_list = calc_pmf(num_list)  # 新增, 需要打开注释以测试效果
        p = plt.bar(age_list, num_list, bottom=bottom, color=color_list[i])
        bottom = num_list
        p_list.append(p)
    plt.ylabel('Population')
    plt.xlabel('Age')
    plt.title('各年龄段人口分布')

    plt.legend((p_list[0][0], p_list[1][0]), ('Men', 'Women'))
    plt.show()
    print('*'*100)

    # 8.2.2 饼图代码
    d = read_excel()
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


