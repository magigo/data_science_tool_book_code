# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import random
import csv as csv

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

data_df = pd.read_csv('train.csv', header=0)

# 将性别转换成数字表示, 1表示男性, 0表示女性
data_df.Sex = data_df.Sex.map({'female': 0, 'male': 1}).astype(int)

# 将登船地点转换为数字表达
embarded_dict = dict(map(lambda x: x[::-1], enumerate(np.unique(data_df.Embarked))))
data_df.Embarked = data_df.Embarked.map(embarded_dict).astype(int)
print(embarded_dict)

# 计算数据集中登船地点中的众数(mode), 并且将缺失登船地点的全部赋值为最常见的地点
embarked_mode = pd.Series(data_df.Embarked).dropna().mode().values
data_df.Embarked[data_df.Embarked.isnull()] = embarked_mode

# 使用年龄的中位数补全缺失的年龄信息
median_age = data_df.Age.dropna().median()
data_df.Age[data_df.Age.isnull()] = median_age

# 按照每个阶级的中位数票价补全缺失的票价信息
class_median_fare = dict(data_df.loc[:, ["Pclass", "Fare"]].dropna(how='any').groupby('Pclass').Fare.median())
data_df.Fare[data_df.Fare.isnull()] = data_df.Pclass[data_df.Fare.isnull()].map(class_median_fare)

# 在删除乘客ID栏之前保存乘客的id
ids = data_df['PassengerId'].values
# 移除非数字类型的栏
data_df = data_df.drop(['Name', 'Ticket', 'Cabin', 'PassengerId'], axis=1)

# 将原始数据分为训练集和测试集
index = np.array(range(len(ids)))
random.shuffle(index)
train_df, test_df = data_df.loc[index[:800]], data_df.loc[index[800:]]
train_ids, test_ids = ids[index[:800]], ids[index[800:]]

# 训练算法
print('Training...')
forest = RandomForestClassifier(n_estimators=100)
forest = forest.fit(train_df.values[0::, 1::], train_df.Survived.values)

# 进行预测
print('Predicting...')
output = forest.predict(test_df.values[0::, 1::]).astype(int)
print(output)

# 最简单的方式评估预测效果, 分值越大越好
score = forest.score(test_df.values[0::, 1::], test_df.Survived.values)
print('score:', score)

# 混淆矩阵
from sklearn.metrics import confusion_matrix

print(confusion_matrix(test_df.Survived.values, output))

# 正确路和召回率
from sklearn.metrics import precision_score, recall_score
print('precision:', precision_score(test_df.Survived.values, output))
print('recall', recall_score(test_df.Survived.values, output))

# ROC曲线以及AUC
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
fpr, tpr, _ = roc_curve(test_df.Survived.values, output)
roc_auc = auc(fpr, tpr)
print('auc:', roc_auc)

plt.figure()
plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc="lower right")
plt.show()



# 交叉验证



# print(data_df)


if __name__ == '__main__':
    pass