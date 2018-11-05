#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

'''基本功能'''
# 1.重新索引reindex：作用是创建一个适应新索引的新对象
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['c', 'b', 'a', 'd'])
print(obj)
print('-----------------snip-------------')
# 调用Series的reindex将会根据新索引进行重排，如果某个索引值当前不存在，就引入缺失值
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)
print('-----------------snip-------------')
obj21 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
print(obj21)
print('-----------------snip-------------')
# 使用ffill/pad可以实现前向值填充;使用bfill/backfill可以实现后向值填充
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj31 = obj3.reindex(range(6), method='ffill')
print(obj31)
print('-----------------snip-------------')
# 对于DataFrame，reindex可以修改行、列索引，如果仅传入一个序列，则会重新索引行
frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['Curry', 'Harden', 'James'])
print(frame)
print('-----------------snip-------------')
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)
print('-----------------snip-------------')
# 使用columns关键字即可重新索引列
names = ['Curry', 'Durant', 'James']
print(frame.reindex(columns=names))
print('-----------------snip-------------')
# 同时对行和列进行重新索引，插值则只能按行应用（axis=0）
print(frame.reindex(['a', 'b', 'c', 'd'], method='ffill', columns=names))
print('-----------------snip-------------')
# 利用ix的标签索引功能，重新索引任务会变的简洁
print(frame.ix[['a', 'b', 'c', 'd'], names])
print('-----------------snip-------------')

# 2.丢弃指定轴上的项
obj = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')
print(new_obj)
print('-----------------snip-------------')
print(obj.drop(['d', 'c']))
print('-----------------snip-------------')
# 对DataFrame,可以删除任意轴上的索引值
data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Curry', 'Harden', 'Durant', 'James'], columns=['one', 'two', 'three', 'four'])
print(data)
print('-----------------snip-------------')
print(data.drop(['Curry', 'Durant']))
print('-----------------snip-------------')
print(data.drop('two', axis=1))
print('-----------------snip-------------')
print(data.drop(['two', 'four'], axis=1))
print('-----------------snip-------------')
# 3.索引、选取和过滤
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj['b'])
print('-----------------snip-------------')
print(obj[1])
print('-----------------snip-------------')
print(obj[2:4])
print('-----------------snip-------------')
print(obj[['b', 'a', 'd']])
print('-----------------snip-------------')
print(obj[[1, 3]])
print('-----------------snip-------------')
print(obj[obj > 2])
print('-----------------snip-------------')
# 利用标签的切片与普通的python切片运算不同，其末端是包含的
print(obj['b':'c'])
print('-----------------snip-------------')
obj['b':'c'] = 5
print(obj)
print('-----------------snip-------------')
# 对DataFrame进行索引就是获取一个或多个列
data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Curry', 'Harden', 'Durant', 'James'], columns=['one', 'two', 'three', 'four'])
print(data)
print('-----------------snip-------------')
print(data['two'])
print('-----------------snip-------------')
print(data[['two', 'four']])
print('-----------------snip-------------')
# 通过切片或布尔型数组选取行
print(data[:2])
print('-----------------snip-------------')
print(data[data['three'] > 5])
print('-----------------snip-------------')
# 利用布尔型DataFrame进行索引
print(data < 5)
print('-----------------snip-------------')
data[data < 5] = 0
print(data)
print('-----------------snip-------------')
# 为了在DataFrame的行上进行标签索引，专门引入索引字段ix
print(data.ix[['Curry'], ['two', 'three']])
print('-----------------snip-------------')
print(data.ix[['Curry', 'James'], [3, 0, 1]])
print('-----------------snip-------------')
print(data.ix[2])
print('-----------------snip-------------')
print(data.ix[:'Durant', 'two'])
print('-----------------snip-------------')
print(data.ix[data.three > 5, :3])
# 4.算术运算和数据对齐
# 自动的数据对齐操作，在不重叠的索引处引入NA值
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print(s1)
print('-----------------snip-------------')
print(s2)
print('-----------------snip-------------')
print(s1 + s2)
print('-----------------snip-------------')
# 对DataFrame，对齐操作会同时发生在行和列上
df1 = pd.DataFrame(np.arange(9).reshape((3, 3)), columns=list('bcd'), index=['Curry','Harden', 'James'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Bob', 'Curry', 'Harden', 'Tom'])
print(df1)
print('-----------------snip-------------')
print(df2)
print('-----------------snip-------------')
print(df1 + df2)
print('-----------------snip-------------')
# 5.在算术方法中填充
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
print(df1)
print('-----------------snip-------------')
print(df2)
print('-----------------snip-------------')
# 相加时，没有重叠的位置会产生NA值
print(df1 + df2)
print('-----------------snip-------------')
# 使用df1的add方法，传入df2以及一个fill_value参数
print(df1.add(df2, fill_value=0))
print('-----------------snip-------------')
# 在对Series或DataFrame重新索引时，也可指定一个填充值
print(df1.reindex(columns=df2.columns, fill_value=0))
print('-----------------snip-------------')
# DataFrame与Series之间的运算
arr = np.arange(12.).reshape((3, 4))
print(arr)
print('-----------------snip-------------')
print(arr[0])
print('-----------------snip-------------')
# 广播机制
print(arr - arr[0])
print('-----------------snip-------------')
# DataFrame与Series之间的运算差不多
frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Curry', 'Harden', 'James', 'Bob'])
series = frame.ix[0]
print(frame)
print('-----------------snip-------------')
print(series)
print('-----------------snip-------------')
# 默认情况下，DataFrame与Series之间的算术运算会将Series的索引匹配到DataFrame的列，然后沿着行一直广播下去
print(frame - series)
print('-----------------snip-------------')
# 如果某个索引值在DataFrame的列或Series的索引中找不到，则参与运算的两个对象就会被重新索引来形成并集
series2 = pd.Series(range(3), index=['b', 'e', 'f'])
print(frame + series2)
print('-----------------snip-------------')
# 如果希望匹配行且在列上广播，则必须使用算术运算方法
series3 = frame['d']
print(frame)
print('-----------------snip-------------')
print(series3)
print('-----------------snip-------------')
print(frame.sub(series3, axis=0))
print('-----------------snip-------------')
# 6.函数应用和映射
frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Curry', 'Harden', 'James', 'Tom'])
print(frame)
print('-----------------snip-------------')
print(np.abs(frame))
print('-----------------snip-------------')
# 将函数应用到由各行或各列组成的一维数组上，使用DataFrame的apply方法即可实现
f = lambda x: x.max() - x.min()
print(frame.apply(f))
print('-----------------snip-------------')
print(frame.apply(f, axis=1))
print('-----------------snip-------------')
# 7.排序
# 要对行或列索引进行排序，可以使用sort_index方法,返回一个已排序的新对象
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj.sort_index())
print('-----------------snip-------------')
# 对于DataFrame，可以根据任意一个轴上的索引进行排序
frame = pd.DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'], columns=['d', 'a', 'b', 'c'])
print(frame)
print('-----------------snip-------------')
print(frame.sort_index())
print('-----------------snip-------------')
print(frame.sort_index(axis=1))
print('-----------------snip-------------')
# 数据默认是按升序排列的，也可以按降序排列
print(frame.sort_index(axis=1, ascending=False))
print('-----------------snip-------------')
# 若要按值对Series进行排序，可使用sort_values()方法
obj = pd.Series([4, 7, -3, 2])
print(obj.sort_values())
print('-----------------snip-------------')
# 在排序时，任何缺失值默认都被放到Series的末尾
obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
print(obj.sort_values())
print('-----------------snip-------------')
# 在DataFrame上，使用by则根据一个或多个列中的值进行排序
frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
print(frame)
print('-----------------snip-------------')
print(frame.sort_values(by='b'))
print('-----------------snip-------------')
# 要根据多个列进行排序，传入名称的列表即可
print(frame.sort_values(by=['a', 'b']))
print('-----------------snip-------------')
# 8.带有重复值的轴索引
obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
print(obj)
print('-----------------snip-------------')
# 索引的is_unique属性告诉你它的值是否是唯一的
print(obj.index.is_unique)
print('-----------------snip-------------')
# 如果某个索引对应多个值，则返回一个Series；对于单个值的，则返回一个标量值
print(obj['a'])
print('-----------------snip-------------')
print(obj['c'])
print('-----------------snip-------------')
# 对于DataFrame的行进行索引时也是如此
frame = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
print(frame)
print('-----------------snip-------------')
print(frame.ix['b'])



