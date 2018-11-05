#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# DataFrame数据结构介绍

# 构建DataFrame的办法有很多，最常用的一种的直接传入一个由等长列表或者数组组成的字典,DataFrame会自动加上索引，且全部列会被有序排列
data = {'name': ['Curry', 'Harden', 'Durant', 'James', 'Bob'],
        'year': [1988, 1990, 1989, 1985, 2000],
        'age': [30, 28, 29, 33, 18]}
frame = pd.DataFrame(data)
print(frame)
print('------------------snip-------------')
# 指定列的排列顺序
print(pd.DataFrame(data, columns=['name', 'age', 'year']))
print('------------------snip-------------')
# 如果传入的列在数据中找不到,就会产生缺失值NA
frame2 = pd.DataFrame(data, columns=['name', 'age', 'year', 'state'], index=['one', 'two', 'three', 'four', 'five'])
print(frame2)
print('------------------snip-------------')
print(frame2.columns)
print('------------------snip-------------')
# 通过类似字典标记的方式或属性的方式，可以将DataFrame的列获取为一个Series
print(frame2['name'])
print('------------------snip-------------')
print(frame2.age)
print('------------------snip-------------')
# 注意返回的Series拥有原DataFrame相同的索引，行也可以通过位置或名称的方式进行获取，比如利用索引字典ix
print(frame2.ix['three'])
print('------------------snip-------------')
# 可以通过赋值的方式进行修改,将列表或数组赋值给某一列时，其长度必须与DataFrame的长度相匹配
frame2['state'] = ['USA', 'UK', 'CHINA', 'INDIA', 'JPAN']
print(frame2)
print('------------------snip-------------')
# 如果赋值的是一个Serise，就会精确匹配DataFrame的索引，将索引的空位都将被填上缺失值
val = pd.Series(['USA', 'UK', 'CHINA'], index=['one', 'three', 'five'])
frame2['state'] = val
print(frame2)
print('------------------snip-------------')
# 为不存在的列赋值会创建一个新列，关键字del用于删除列
frame2['eastern'] = frame2.state == 'USA'
print(frame2)
print('------------------snip-------------')
del frame2['eastern']
print(frame2.columns)
print('------------------snip-------------')
# 注意：通过索引方式返回的列只是相应数据的视图，并不是副本

# 另一种常见的数据形式是嵌套字典,如果将它传给DataFrame，外层字典的键作为列，内层的键则作为行索引
pop = {'CHINA': {2001: 2.4, 2002: 2.9}, 'USA': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print(frame3)
print('------------------snip-------------')
# 对上述结果进行转置
print(frame3.T)
print('------------------snip-------------')
# 显式指定索引
pop = {'CHINA': {2001: 2.4, 2002: 2.9}, 'USA': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame4 = pd.DataFrame(pop, index=[2001, 2002, 2003])
print(frame4)
print('------------------snip-------------')
# 如果设置DataFrame的index和columns的name属性，则这些信息也会被显式出来
frame3.index.name = 'year'
frame3.columns.name = 'state'
print(frame3)
print('------------------snip-------------')
# values属性会以二维ndarray的形式返回DataFrame中的数据
print(frame3.values)
print('------------------snip-------------')
# 如果DataFrame中各列的数据类型不同，则值数组的数据类型就会选用能兼容所有列的数据类型
print(frame2.values)
print('------------------snip-------------')

# 索引对象
obj = pd.Series(range(3), index=['a', 'b', 'c'])
index = obj.index
print(index)
print('------------------snip-------------')
print(index[1:])
print('------------------snip-------------')
# 索引是不能修改的,下面代码错误
# index[1] = 'd'
index = pd.Index(np.arange(3))
obj2 = pd.Series([-1.3, 3.14, 0], index=index)
print(obj2.index is index)
print('------------------snip-------------')
print(frame3)
print('USA' in frame3.columns)
print('------------------snip-------------')
print(2002 in frame3.index)
print('------------------snip-------------')

