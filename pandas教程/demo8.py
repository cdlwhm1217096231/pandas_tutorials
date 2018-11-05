#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2
import numpy as np
import pandas as pd
from pandas import DataFrame,Series
import re


"""数据规整化：清理、转换、合并、重塑"""

# 1.合并数据集
# pandas.merge可以根据一个或多个键将不同的DataFrame中的行连接起来
# pandas.concat可以沿一条轴将多个对象堆叠到一起
# 实例方法combine_first可以将重复数据连接在一起，用一个对象中的值填充另一个对象中的缺失值

# 数据库风格的DataFrame合并
"""数据集的合并merge或连接join运算是通过一个或多个键将行连接起来"""
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df2 = pd.DataFrame({'key':['a', 'b', 'd'], 'data2': range(3)})
print(df1)
print('--------------snip------------')
print(df2)
print('--------------snip------------')
print(pd.merge(df1, df2))
print('--------------snip------------')
# 如果没有指明要用哪个列进行连接，merge就会将重叠列的列名当做键，最好显示指定一下
print(pd.merge(df1, df2, on='key'))
print('--------------snip------------')
# 如果两个对象的列名不同，也可以分别进行指定
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})
print(pd.merge(df3, df4, left_on='lkey', right_on='rkey'))
print('--------------snip------------')
# 注意:默认情况下,merge做的是内连接，结果中的交集；外连接求取的是并集,还有其他合并方式：left right outer
print(pd.merge(df1, df2, how='outer'))
print('--------------snip------------')
# 2.索引上的合并
"""有时候Dataframe的连接键位于其索引中，此时可以传入left_index=True或者right_index=True来说明索引应该被用作连接键"""
left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'], 'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
print(left1)
print('--------------snip------------')
print(right1)
print('--------------snip------------')
print(pd.merge(left1, right1, left_on='key', right_index=True))
print('--------------snip------------')
print(pd.merge(left1, right1, left_on='key', right_index=True, how='outer'))
print('--------------snip------------')
# 3.轴向连接
arr = np.arange(12).reshape(3, 4)
print(arr)
print('--------------snip------------')
print(np.concatenate([arr, arr], axis=1))
print('--------------snip------------')
# 没有重叠索引轴的Series
s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
print(pd.concat([s1, s2, s3]))  # 默认是在axis=0上连接的
print('--------------snip------------')
print(pd.concat([s1, s2, s3], axis=1))
print('--------------snip------------')
# Dataframe对象也是如此
df1 = pd.DataFrame(np.arange(6).reshape((3, 2)), index=['a', 'b', 'c'], columns=['one', 'two'])
df2 = pd.DataFrame(5+np.arange(4).reshape((2, 2)), index=['a', 'c'], columns=['three', 'four'])
print(pd.concat([df1, df2], axis=1, keys=['level1', 'level2']))
print('--------------snip------------')
# 2.重塑和轴转向
data = pd.DataFrame(np.arange(6).reshape((2, 3)), index=pd.Index(['curry', 'harden'], name='name'), columns=pd.Index(['one', 'two', 'three'], name='number'))
print(data)
print('--------------snip------------')
# 使用stack方法将列转化为行
result = data.stack()
print(result)
print('--------------snip------------')
# 使用unstack将其重排为一个DataFrame
print(result.unstack())
print('--------------snip------------')
# 3.字符串对象方法
val = 'a,b, curry'
print(val.split(','))
pieices = [x.strip() for x in val.split(',')]
print(pieices)
# 向字符串'::'的join方法传入一个列表或元组
print('::'.join(pieices))
# replace()用于将指定模式替换成另一个模式，一般用于删除操作，传入空字符串
print(val.replace(',', ':'))
print(val.replace(',', ''))
# 正则表达式regex
text = 'foo bar\t baz  \tqux\nhaha'
# 描述一个或多个空白符(制表符、空格、换行符)的正则表达式\s+
print(re.split(r'\s+', text))
print('--------------snip------------')
# 也可以使用re.compile()自己编译一个regex来得到一个regex对象
regex = re.compile(r'\s+')
print(regex.split(text))
