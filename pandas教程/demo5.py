#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

"""处理缺失数据"""
# pandas使用浮点值NaN表示浮点和非浮点数组中的缺失数据

data = pd.Series(['Curry', 'Harden', 'James', np.nan])
print(data)
print('----------------snip-----------------')
print(data.isnull())
print('----------------snip-----------------')
# python内置的None值也会被当做NA值处理
data[0] = None
print(data.isnull())
print('----------------snip-----------------')
# 1.过滤缺失数据
data = pd.Series([1, np.nan, 3.5, np.nan, 7])
print(data.dropna())
print('----------------snip-----------------')
# 通过布尔型索引也可以达到目的
print(data[data.notnull()])
print('----------------snip-----------------')
# 对应DataFrame对象，dropna默认丢弃任何含有缺失值的行
data = pd.DataFrame([[1., 6.5, 3.], [1, np.nan, np.nan], [np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
print(data)
print('----------------snip-----------------')
cleaned = data.dropna()
print(cleaned)
print('----------------snip-----------------')
# 传入how='all'将只丢弃全为NA的那些行
print(data.dropna(how='all'))
print('----------------snip-----------------')
# 要丢弃列，则传入axis=1即可
data[4] = np.nan
print(data)
print('----------------snip-----------------')
print(data.dropna(axis=1, how='all'))
print('----------------snip-----------------')
# 只留下一部分观测数据，可以用thresh参数实现
df = pd.DataFrame(np.random.randn(7, 3))
print(df)
df.ix[:4, 1] = np.nan
df.ix[:2, 2] = np.nan
print('----------------snip-----------------')
print(df)
print('----------------snip-----------------')
print(df.dropna(thresh=3))
print('----------------snip-----------------')
# 2.填充缺失数据
# 使用fillna方法将缺失的数据替换为那个常数值
print(df.fillna(0))
print('----------------snip-----------------')
# 如果通过一个字典调用fillna，就可以实现对不同的列填充不同的值
print(df.fillna({1: 0.5, 2: -1}))
print('----------------snip-----------------')
# fillna默认会返回新对象，但也可以对现有对象进行修改
df.fillna(0, inplace=True)
print(df)  # 返回被填充对象的引用
print('----------------snip-----------------')
