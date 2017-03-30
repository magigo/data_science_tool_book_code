# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from sklearn import datasets
from sklearn import svm
from sklearn.externals import joblib
import matplotlib.pyplot as plt

iris_data = datasets.load_iris()
digits_data = datasets.load_digits()

clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits_data.data[:-1], digits_data.target[:-1])
print('predicted', clf.predict(digits_data.data[-1:]))
print('true', digits_data.target[-1:])
#
# plt.figure(1, figsize=(3, 3))
# plt.imshow(digits_data.images[-1], cmap=plt.cm.gray_r, interpolation='nearest')
# plt.show()
# 方法1
import pickle

with open('clf', 'a') as fw:
    pickle.dump(clf, fw)
with open('clf', 'r') as fr:
    clf = pickle.load(fr.read())

# 方法2
from sklearn.externals import joblib

joblib.dump(clf, 'clf')
clf = joblib.load('clf')

if __name__ == '__main__':
    pass
