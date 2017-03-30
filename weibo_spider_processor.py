# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from glob import glob
import fileinput
import json
from multiprocessing import Pool, cpu_count


class AutoMult(object):
    def __init__(self, processnum=cpu_count()):
        self.pool = Pool(processnum)

    def auto_multiprocessing_map(self, func, input_list):
        '''
        自动多进程函数，仅限纯map函数，默认用尽所有CPU,
        :param func: map函数
        :param input_list: 输入数据
        :return: map函数处理完输入列表中的的每个值之后的返回值，迭代器类型
        '''
        result = self.pool.map(func, input_list)
        for r in result:
            yield r


def extract_useful_info(pin):
    row, auth_type = pin
    d = json.loads(row)
    uid = d.get('idstr')
    name = d.get('screen_name')
    gender = d.get('gender')
    birthday = d.get('birthday')
    desc = d.get('description')
    verified_reason = d.get('verified_reason')
    education_info = d.get('education_info')
    career_info = d.get('career_info')
    gsid_s_c = d.get('gsid_s_c')
    location = d.get('location')
    return json.dumps({'uid': uid, 'name': name, 'gender': gender, 'birthday': birthday, 'desc': desc,
                       'verified_reason': verified_reason, 'education_info': education_info, 'career_info': career_info,
                       'gsid_s_c': gsid_s_c, 'location': location, 'auth_type': auth_type}) + '\n'


def gen_input(path):
    if 'gsid' in path:
        auth_type = 1
    else:
        auth_type = 0
    for row in fileinput.input(glob(path), bufsize=8 * 1024):
        yield row, auth_type


def write_lines(path, lines_iter, num=2000):
    with open(path, 'a') as fw:
        w_lines = []
        for i, line in enumerate(lines_iter):
            if i % num == 0:
                fw.writelines(w_lines)
                w_lines = []
            w_lines.append(line)
            print(i)
        fw.writelines(w_lines)
    return True


if __name__ == '__main__':
    from sys import argv


    path, output = argv[1], argv[2]
    auto = AutoMult()
    input_list = gen_input(path)
    output_iter = auto.auto_multiprocessing_map(extract_useful_info, input_list)
    write_lines(output, output_iter)

    # from random import choice
    # import fileinput
    # from glob import glob
    # import json
    # gsid_list = []
    # for line in fileinput.input(glob('/mnt/logs/gsid/*')):
    #     gsid_list.append(line.strip().split(','))
    #
    # with open('/mnt/uid_user_info', 'r') as fr, open('/mnt/uid_user_info_g', 'w') as fw:
    #     for row in fr:
    #         d = json.loads(row)
    #         d['gsid_s_c'] = choice(gsid_list)
    #         fw.write(json.dumps(d) + '\n')

