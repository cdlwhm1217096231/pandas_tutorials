#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2

import numpy as np
import pandas as pd
from pandas import Series,DataFrame


"""汇总和计算描述统计"""

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
print(df)
print('----------------snip-----------------')
# 调用DataFrame的sum方法将会返回一个含有列小计的Series
print(df.sum())
print('----------------snip-----------------')
# 传入axis=1将会按列进行求和
print(df.sum(axis=1))
print('----------------snip-----------------')
# NA值会被自动排除，除非整个切片都是NA，通过skipna选项可以禁用该功能
print(df.mean(axis=1, skipna=False))
print('----------------snip-----------------')
# idxmin、idxmax返回的是间接统计,属于约简型
print(df.idxmax())
print('----------------snip-----------------')
# 另一些方法是累积型的
print(df.cumsum())
print('----------------snip-----------------')
# 还有一种方法不属于上面两种类型，describe用于一次性产生多个汇总统计
print(df.describe())
print('----------------snip-----------------')
# 对应非数值型数据，describe也会产生另一种汇总统计
obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
print(obj.describe())
print('----------------snip-----------------')
# 唯一值、值计数以及成员资格
# 从一维Series的值中抽取信息,第一个函数是unique，可以得到Series中的唯一值数组
obj = Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
uniques = obj.unique()
print(uniques)
print('----------------snip-----------------')
# 计算一个Series中各个值出现的频率
print(obj.value_counts())
print('----------------snip-----------------')
# value_counts还是一个顶级pandas方法，可以用于任何数组或序列
print(pd.value_counts(obj.values, sort=False))
print('----------------snip-----------------')
# isin用于判断矢量化集合的成员资格，用于选取Series或DataFrame列中数据的子集
mask = obj.isin(['b', 'c'])
print(mask)
print('----------------snip-----------------')
print(obj[mask])
print('----------------snip-----------------')


