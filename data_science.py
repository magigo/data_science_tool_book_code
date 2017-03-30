# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import numpy as np

# Numpy
# ********


# ndarray类型的基本操作
a = np.arange(15).reshape(3, 5)
print('a             ', '=', a)
print('a.ndim        ', '=', a.ndim)
print('a.shape       ', '=', a.shape)
print('a.dtype.name  ', '=', a.dtype.name)
print('a.itemsize    ', '=', a.itemsize)
print('a.size        ', '=', a.size)
print('type(a)       ', '=', type(a))

# 创建array类型的数据
a = np.array([1, 2, 3, 4])

b = np.array([1.2, 3.4, 5.6])
print(a.dtype, b.dtype)

# 二维数组和三维数组
a = np.array([(1, 2), (3.4, 5)])
print(a)
print(a.ndim)
b = np.array([(1, 2), (3.4, 5), (6, 7.8)])
print(b)

# 占位符
a = np.zeros((3, 4))
b = np.ones((2, 3, 4), dtype=np.int64)
c = np.empty((4, 5))
print('zeros\n', a)
print('ones \n', b)
print('empty\n', c)

# range, Python的range是不能创建小数步长的列表的
a = np.arange(1, 30, 5)
b = np.arange(0, 1, 0.2)
print(a, b)

# 在某个区间均匀的生成一定数量个数
c = np.linspace(0, np.e * 10, 5)
print(c)

# See also
# array, zeros, zeros_like, ones, ones_like, empty, empty_like, arange, linspace, numpy.random.rand, numpy.random.randn, fromfunction, fromfile
# =====


# 关于打印
print(np.arange(10000).reshape(100, 100))

# 基本操作
a = np.array([10, 20, 30, 40])
b = np.arange(4)
print('a\n', a, '\nb\n', b)
print('a - 4\n', a - 4)
c = a - b
print('c\n', c)
print('b * 2\n', b * 2)
print('b ** 2\n', b ** 2)
print('a < 21\n', a < 21)

# 矩阵乘法使用dot()方法, *是按位置计算
a = np.array(([1, 2], [2, 3]))
b = np.array(([1, 0], [0, 2]))
print('a\n', a)
print('b\n', b)
print('a * b\n', a * b)
print('a.dot(b)\n', a.dot(b))

c = np.array([1, 2, 3, 4, 5])
d = np.array([2, 3, 4, 5, 6])
print('c * d.T\n', c.dot(d.T))


# +=, *=是原地修改值
a = np.ones((3, 2))
b = np.random.random((3, 2))
a *= 3
print(a)

b += a
print(b)

# 很多一元操作被实现成ndarray的方法
a = np.random.random((3, 2))
print('a\n', a)
print('a.sum()\n', a.sum())
print('a.min()\n', a.min())
print('a.max()\n', a.max())

# 可以通过指定轴把计算应用到特定的轴上
print('a.sum(axis=0)\n', a.sum(axis=0))
print('a.sum(axis=1)\n', a.sum(axis=1))
print('a.cumsum(axis=1)\n', a.cumsum(axis=1))  # 累积和

# 一般的数学函数都是作用在每一个元素上的
a = np.arange(3)
print(a)
print(np.exp(a))
print(np.sqrt(a))

#
# See also
# all, any, apply_along_axis, argmax, argmin, argsort, average, bincount, ceil, clip, conj, corrcoef, cov, cross, cumprod, cumsum, diff, dot, floor, inner, inv, lexsort, max, maximum, mean, median, min, minimum, nonzero, outer, prod, re, round, sort, std, sum, trace, transpose, var, vdot, vectorize, where
#

# 一维列表,下标\切片\迭代与list一样
# 多维列表

a = np.fromfunction(lambda x, y: 5 * x + y, (4, 4))  # x, y是每个位置的索引
print('a\n', a)
print('a[2, -1]\n', a[2, -1])
print('a[:, 1:3]\n', a[:, 1:3])
b = np.fromfunction(lambda x, y, z: x + y + z, (4, 5, 6))
print('b\n', b)
print('b[1, ...]\n', b[1, ...])  # 在数组维度比较高时, ...代表剩下其余的全部维度

# 高维数组迭代
# 按行迭代
print('=*')
for row in a:
    print(row)

# 按元素迭代
for e in a.flat:
    print(e)
#
# See also
# Indexing, Indexing (reference), newaxis, ndenumerate, indices

# 改变数组形状
a = np.random.random((3, 4))
print('a\n', a)
print('a.shape\n', a.shape)
# print(a.ravel())  # 摊平多维数组
print('a.T\n', a.T)  # 转秩

a.resize((2, 6))  # 原地修改
print('a.resize(2, 6)\n', a)

print('a.reshape(3, -1)\n', a.reshape(3, -1))  # 使用reshape()函数, 被赋值为-1的维度会自动计算

# See also
# ndarray.shape, reshape, resize, ravel
#

# 堆叠数组,
a = np.random.random((2, 3))
b = np.random.random((2, 3))
print('a\n', a, '\nb\n', b)
print('np.vstack((a, b))\n', np.vstack((a, b)))
print('np.hstack((a, b))\n', np.hstack((a, b)))

a = np.array([4., 2.])
print(a[:, np.newaxis])  # 可以允许二维的列向量
# 另外一种生成数组的方式
print(np.r_[1:4, 0, 4])  # 还有一个对应列版的c_

# 切分
a = np.floor(10 * np.random.random((2, 12)))
print('a\n', a)
print('np.hsplit(a, 3)\n', np.hsplit(a, 3))
print('np.vsplit(a, 1)\n', np.vsplit(a, 1))

# 同样垂直方向还有一个vsplit()

# 拷贝
a.view()  # 浅拷贝, 拷贝了形状
a.copy()  # 完全拷贝

# 除了标准Python可以使用的索引方法,之外还有更高级的索引方法
a = np.arange(20) * 3
print('a\n', a)
i = np.array([1, 3, 7, 2, 4])
print('a[i]\n', a[i])
j = np.array([[3, 4], [9, 7]])
print('a[j]\n', a[j])

# 当原始数组是多维的时候,也能实现上面的功能
a = np.arange(12).reshape(3, 4)
i = np.array([[1, 1],
              [1, 2]])  # 行向索引

j = np.array([[1, 1],
              [3, 3]])  # 列向索引

print('a[i, j]\n', a[i, j])

# arg_函数,按索引...
data = np.sin(np.arange(20)).reshape(5, 4)
print('data\n', data)
ind = data.argmax(axis=0)
print('ind\n', ind)
sort = data.argsort()
print('sort', sort)
# print(data[ind, range(data.shape[1])])

# 多重复值
a = np.arange(5)
print(a)
a[[1, 2, 3]] = 0
print(a)
a[[1, 2, 3]] = [3, 2, 1]

# 布尔索引
a = np.arange(12).reshape(3, 4)
b = a > 3
print('b\n', b)
print('a[b]\n', a[b])

a[b] = 0
print(a)

# 构建可以进行叉积的一维数组
a, b = np.ix_([0, 1], [2, 4])
print(a.shape)
print(b.shape)
print(a * b)

# 线性代数
a = np.array([[1, 2], [3, 4]])
print(a)
print(a.T, a.transpose())  # 转秩
print(np.linalg.inv(a))  # 矩阵的逆
print(np.eye(4))  # 对角阵
print(np.trace(np.eye(3)))  # 矩阵的迹

y = np.array([[5.], [7.]])
print(np.linalg.solve(a, y))  # 解线性方程
z = np.array([[0.0, -1.0], [1.0, 0.0]])
print(np.linalg.eig(z))  # 解特征方程

# Pandas
# ***********

import pandas as pd
import matplotlib.pyplot as plt

# Pandas中的Series与Numpy中的Array的不同之处在于Series是带索引的ndarray
# 创建对象
a = pd.Series([1, 0.3, np.nan])
b = pd.Series(np.array([1, 2, 3]))
print('a\n', a)
print('b\n', b)

print(pd.Series([1, 'a']))

print('a[0]\n', a[0])
print("a[a > 0.5]\n", a[a > 0.5])
print("a[[2,1]]\n", a[[2, 1]])
print('a.sum()\n', a.sum())

c = pd.Series([1,2,3], index=["a", "b", "c"])
print('c\n', c)
print("c['b']\n", c['b'])
print("c.get('d', np.nan)\n", c.get('d', np.nan))

d = pd.Series({'c': 0, 'd': 1, 'e': 2})
print('d\n', d)



date = pd.date_range('20160101', periods=5)
print(date)

# 使用numpy对象创建DataFrame
df = pd.DataFrame(np.random.randn(5, 4), index=date, columns=list("ABCD"))
print(df)

# 使用字典创建DataFrame
df2 = pd.DataFrame({'A': 2.,
                    'B': pd.Timestamp('20160101'),
                    'C': pd.Series(3, index=list(range(4)), dtype='float64'),
                    'D': np.array([3] * 4, dtype='int64'),
                    'E': pd.Categorical(["t1", "t2", "t3", "t4"]),
                    'F': 'abc'})
print(df2)
print(df2.dtypes)
print(df2.C)

# 查看
print(df.head())  # 获取前几行数据
print(df.tail())  # 获取后几行数据
print(df.index)  # 获取索引
print(df.columns)  # 获取栏名
print(df.values)  # 获取值
print(df.describe)  # 获取描述信息
print(df.T)  # 转秩
print(df.sort_index(axis=1, ascending=False))  # 对索引进行重新排序
print(df.sort_values(by='D'))  # 针对某一栏中的元素进行排序

# 选择
print(df['A'])  # 获取某一栏的全部数据
print(df[1:3])  # 获取索引1:3的行数据
print(df['20160101':'20160103'])  # 获取索引值为'20160101':'20160103'的行数据

# loc是定位元素的方法
print(df.loc[date[0]])  # 获取date第一个索引的数据
print(df.loc[:, ['A', 'B']])  # 获取栏名为AB的全部行数据
print(df.loc['20160102':'20160104', ['A', 'B']])  # 获取索引在'20160102':'20160104'范围的AB栏的数据
print(df.loc['20160102', ['A', 'B']])  # 获取索引为'20160102'的AB栏的数据
print(df.loc[date[0], 'A'])
print(df.at[date[0], 'A'])

print(df.iloc[3])
print(df.iloc[3:5, 0:2])
print(df.iloc[[1, 2, 4], [0, 2]])
print(df.iloc[1:3, :])
print(df.iloc[:, 1:3])
print(df.iloc[1, 1])
print(df.iloc[1, 1])

# 通过布尔值获取数据
print(df[df.A > 0])  # 获取A栏中大于0的数据
print(df[df > 0])  # 获取所有大于0的数据

df3 = df.copy()
df3['D'] = ['a', 'a', 'c', 'd', 'a']
print(df3[df3['D'].isin(['a', 'd'])])

# 赋值
print('df\n', df)
s1 = pd.Series([1, 2, 3, 4], index=pd.date_range('20160102', periods=4))
print('s1\n', s1)
df['F'] = s1
print('df\n', df)
df.at[date[0], 'A'] = 0
print('df\n', df)
df.loc[:, 'D'] = np.array([5] * len(df))
print('df\n', df)

df4 = df.copy()
df4[df4 > 0] = -df4
print(df4)

# 处理缺失值
# df5 = df.reindex(index=date[1:4], columns=list(df.columns) + ["G"])
# df5.loc[date[0]:date[1], 'G'] = 2
print(df)
print(df.dropna(how='any'))
print(df.fillna(value=3))
print(pd.isnull(df))

# 操作
print(df.mean())
print(df.mean(1))  # 对特定的轴求均值

s = pd.Series([1, 3, 5, np.nan, 6], index=date).shift(2)  # 向下移位, 用NaN补齐
print(s)
print(df)
print(df.sub(s, axis='index'))  # df中的每一列减去s

print(df.apply(np.cumsum))
print(df.apply(lambda x: x.max() - x.min()))

# 数据直方图(word count)
s = pd.Series(np.random.randint(0, 7, size=10))
print(s.value_counts())

# 字符串处理
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s.str.lower())

# 合并
df = pd.DataFrame(np.random.randn(10, 4))
print('df\n', df)
pieces = [df[:3], df[3:7], df[7:]]
print('pd.concat(pieces)\n', pd.concat(pieces))

left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print('pd.merge(left, right, on="key")\n', pd.merge(left, right, on='key'))

df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
s = df.iloc[3]
df.append(s, ignore_index=True)
print('df.append(s, ignore_index=True)\n', df)

# Splitting
# Applying
# Combining

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})

print(df.groupby('A').sum())
print(df.groupby(['A', 'B']).sum())

# Reshaping
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
print(df)
print(df.stack())  # 压缩一级
print(df.unstack())

df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})
print(df)
print(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']))  # 花式变形

# 时间序列
rng = pd.date_range('1/1/2016', periods=100, freq='min')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(ts.resample('5Min').sum())
ts_utc = ts.tz_localize('UTC')
print(ts_utc)
print(ts_utc.tz_convert('Asia/Shanghai'))
print(ts.to_period())
print(ts.to_period().to_timestamp())

# 按季度, 不太懂
prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
ts = pd.Series(np.random.randn(len(prng)), prng)
ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9
print(ts.head())

# 分类
df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
df["grade"] = df["raw_grade"].astype("category")
print(df["grade"])

df["grade"].cat.categories = ["very good", "good", "very bad"]
print(df)
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
print(df["grade"])

print(df.sort_values(by="grade"))
df.groupby("grade").size()

# 绘图
# ...

# 数据输入和输出


if __name__ == '__main__':
    pass
