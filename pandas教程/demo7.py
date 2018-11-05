#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

"""数据加载、存储与文件格式"""

# 一、读取文本格式的数据
# pandas提供了一些用于将表格型数据读取为DataFrame对象的函数，其中read_csv和read_table用的最多
# 在windows系统终端中使用type ex1.csv可以查看文件中的内容

df = pd.read_csv('ex1.csv')  # 默认以逗号为分隔符
print(df)
print('-------------snip----------')
# 也可以使用read_table，必须指定分隔符,默认是以\t作为分隔符
print(pd.read_table('ex1.csv', sep=','))
print('-------------snip----------')
# 并不是所有文件都有标题行，如ex2.csv,此时有两个办法
# 1.使用pandas默认的列名
print(pd.read_csv('ex2.csv', header=None))
print('-------------snip----------')
# 2.自己定义列名
print(pd.read_csv('ex2.csv', names=['a', 'b', 'c', 'd', 'message']))
print('-------------snip----------')
# 如果希望将message列作为DataFrame的索引，可以通过index_col参数指定message
print(pd.read_csv('ex2.csv', names=['a', 'b', 'c', 'd', 'message'], index_col='message'))
print('-------------snip----------')
# 有些表格不是由固定的分隔符去分隔字段的，此时需要使用正则表达式作为分隔符
print(pd.read_table('ex3.csv', sep='\s+'))
print('-------------snip----------')
# 文件中含有缺失值的处理
result = pd.read_csv('ex4.csv')
print(result)
print('-------------snip----------')
print(pd.isnull(result))
print('-------------snip----------')
# na_values可以接受一组用于表示缺失值的字符串
result = pd.read_csv('ex4.csv', na_values='NULL')
print(result)
print('-------------snip----------')
# 可以使用一个字典为各列指定不同的NA标记值
ss = {'message': ['foo', 'NA'], 'something': ['three', 'NA']}
print(pd.read_csv('ex4.csv', na_values=ss))
print('-------------snip----------')

# 二、将数据写出到文本格式
data = pd.read_csv('ex4.csv')
print(data)
print('-------------snip----------')
# 利用DataFrame的to_csv方法，将数据写到一个以逗号分隔的文件中,还可以使用其他分隔符,如|
data.to_csv('out.csv', sep=',')
# 缺失值在输出结果中可以被表示为空字符串
data.to_csv('out1.csv', na_rep='NULL')
# 也可以禁止写入行和列的标签
data.to_csv('out2.csv', index=False, header=False)
# 也可以写入部分的列，并以你指定的顺序排列
data.to_csv('out3.csv', index=False, columns=['a', 'b', 'c'])



