# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import matplotlib.pyplot as pl

# 8.2.1
pl.plot([1, 2, 3, 4], [2, 1, 5, 6])
pl.show()

pl.figure(1)
pl.plot([1, 2, 3, 4], [2, 1, 5, 6])
pl.figure(2)
pl.plot([1, 2, 3, 4], [3, 1, 4, 6])
pl.savefig("/Users/jilu/Downloads/fig2")
pl.figure(1)
pl.plot([2, 4], [0, 2])
pl.savefig('/Users/jilu/Downloads/fig1')

x = range(30)
l1 = pl.plot(x, x, 'ro')
l2 = pl.plot(x, [y**2 for y in x], 'bs')
l3 = pl.plot(x, [y**3 for y in x], 'g^')
pl.title(u'不同线型测试')
pl.xlabel(u'x坐标轴标签')
pl.ylabel(u'y坐标轴标签')
pl.legend((l1[0], l2[0], l3[0]), ('1', '2', '3'))

pl.show()

if __name__ == '__main__':
    pass