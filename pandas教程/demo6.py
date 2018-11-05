#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2

import numpy as np
import pandas as pd
from pandas import Series,DataFrame

"""层次化索引"""
data = Series(np.random.randn(10), index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'], [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print(data)
print('----------------snip-----------------')
print(data.index)
print('----------------snip-----------------')
# 选取子集
print(data['b'])
print('----------------snip-----------------')
print(data['b':'c'])
print('----------------snip-----------------')
print(data.ix[['b', 'd']])
print('----------------snip-----------------')
# 通过unstack方法重新安排到一个DataFrame中
print(data.unstack())
print('----------------snip-----------------')
# 整数索引
ser = pd.Series(np.arange(3))
print(ser)
print('----------------snip-----------------')
# 使用.ix方法
print(ser.ix[:1])
