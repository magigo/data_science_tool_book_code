# ! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pandas as pd
from pandas import read_excel

pd.set_option('display.max_columns', 5)
pd.set_option('display.max_rows', 6)

df = read_excel('/Users/jilu/Downloads/A0202.xls', 'Sheet1', index_col=0, skiprows=3)
print(df.describe)

with pd.ExcelFile('/Users/jilu/Downloads/A0202.xls') as xls:
    for x in range(1, 2):
        df = read_excel(xls, 'Sheet{}'.format(x), index_col=0, skiprows=3)
        print(df)

df = pd.DataFrame([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                  index=[0, 1, 2], columns=list("ABCD"))
df.to_excel('/Users/jilu/Downloads/test.xls')

if __name__ == '__main__':
    pass
