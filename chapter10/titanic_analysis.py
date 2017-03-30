# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 180)
pd.set_option('max_colwidth', 110)

# 探索性别对幸存率的影响
data = pd.read_csv('train.csv')
print(data)
print(data.xs(0))

# 计算男性和女性的幸存率
# 方法1
men = data[data.Sex == 'male']
women = data[data.Sex == 'female']
proportion_women_survived = float(sum(women.Survived)) / len(women)
proportion_men_survived = float(sum(men.Survived)) / len(men)
print('female: ', proportion_women_survived)
print('male: ', proportion_men_survived)

# 方法2
print(data.groupby('Sex').Survived.mean())

# 探索年龄对幸存率的影响
import matplotlib.style

matplotlib.style.use('ggplot')

need_data = data.loc[:, ['Age', 'Survived']].dropna(how='any')
need_data['Age'] = need_data['Age'].apply(round).astype('int16')
grouped = need_data.groupby('Age').Survived
survived = grouped.sum()
died = grouped.size() - survived
df = pd.DataFrame(dict(died=died, survived=survived))
df.plot.bar(figsize=(20, 10), color=('k', '#5EB2BF'))

plt.show()

# 探索阶级对幸存率的影响

if __name__ == '__main__':
    pass
