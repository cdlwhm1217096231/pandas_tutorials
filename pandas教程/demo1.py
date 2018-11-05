#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

'''pandas的数据结构介绍'''
# pandas有两个主要的数据结构：Series和DataFrame

# Series是一种类似与一维数组的对象,它由一组数据以及一组与之相关的数据标签(即索引)组成。
obj = pd.Series([4, 7, -5, 3])
print(obj)
print('------------------snip-------------')
# Series的字符串表现形式为：索引在左，值在右，当没有为数据指定索引时，会自动创建一个0到N-1的整数型索引
# 通过values和index属性获取其数组表示形式和索引对象
print(obj.values)
print('------------------snip-------------')
print(obj.index)
print('------------------snip-------------')
# 通常，希望创建的Series带有一个可以对各个数据点进行标记的索引
obj2 = pd.Series([4, 5, 7, -3], index=['d', 'b', 'a', 'c'])
print(obj2)
print('------------------snip-------------')
print(obj2.index)
print('------------------snip-------------')
# 通过索引的方式选取Series中的单个或一组值
print(obj2['a'])
print('------------------snip-------------')
print(obj2[['c', 'a', 'd']])
print('------------------snip-------------')
# 根据布尔型数组进行过滤、标量乘法、应用数学函数都会保留索引与值之间的链接
print(obj2[obj2 > 2])
print('------------------snip-------------')
print(obj2 * 2)
print('------------------snip-------------')
print(np.exp(obj2))
print('------------------snip-------------')
# 还可以将Series看成是一个定长的有序字典，因为它是索引值到数据值的一个映射
print('b' in obj2)
print('e' in obj2)
print('------------------snip-------------')
# 如果数据被存放在一个python字典中，可以直接通过这个字典来创建Series,如果只传入一个字典，则结果Series中的索引就是字典的键
sdata = {'Curry': 30, 'Harden': 28, 'Durant': 29, 'James': 33}
obj3 = pd.Series(sdata)
print(obj3)
print('------------------snip-------------')
# 由于sdata中跟states索引相匹配的那3个值会被找出来并放到相应的位置上，由于'USA'所对应的sdata值找不到，所以结果就是NaN(非数字）表示缺失值NA
# 用NA表示缺失值
states = ['Curry', 'Harden', 'USA', 'James']
obj4 = pd.Series(sdata, index=states)
print(obj4)
print('------------------snip-------------')
# 使用isnull和notnull来检测缺失数据
print(pd.isnull(obj4))
print('------------------snip-------------')
print(pd.notnull(obj4))
# Series也有类似的实例方法
print('------------------snip-------------')
print(obj4.isnull())
print('------------------snip-------------')
print(obj4.notnull())
print('------------------snip-------------')
# 关于处理缺失数据，后面教程中介绍....

# Series最重要的一个功能是：它在算术运算中会自动对齐不同索引的数据
print(obj3)
print('------------------snip-------------')
print(obj4)
print('------------------snip-------------')
print(obj3 + obj4)
print('------------------snip-------------')
# Series对象本身及其索引都有一个name属性，该属性跟pandas其他的关键功能关系非常密切
obj4.name = 'age'
obj4.index.name = 'name'
print(obj4)
print('------------------snip-------------')

