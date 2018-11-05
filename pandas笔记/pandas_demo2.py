#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-14 23:24:15
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import pandas as pd
import numpy as np


index = pd.Index(data=['Tom', 'Bob', 'Mary', 'James'], name='name')
data = {
    'age': [18, 30, 25, 40],
    'city': ['beijing', 'shanghai', 'nanjing', 'hangzhou'],
    'sex': ['male', 'male', 'female', 'male']
}
user_info = pd.DataFrame(data=data, index=index)
print(user_info)
print('--------------------分隔线1------------------')
# 了解下数据的整体情况，可以使用info方法来查看
print(user_info.info())
# 如果我们的数据量非常大，我想看看数据长啥样，不希望查看所有的数据了，这时候可以采用只看头部的n条或者尾部的n条
print('-------------------分隔线2-------------------')
print(user_info.head(2))
print(user_info.tail(2))
# Pandas 中的数据结构都有 ndarray 中的常用方法和属性,例如.shape()和.T方法
print('-------------------分隔线3-------------------')
print(user_info.shape)
# print(user_info.T)
# 通过DataFrame来获取它包含的原有数据，可以通过 .values来获取，获取后的数据类型其实是一个ndarray
print('-------------------分隔线4-------------------')
print(user_info.values)
print('-------------------分隔线5-------------------')
# 查看某一列的最大值,类似的，通过调用 min、mean、quantile、sum 方法可以实现最小值、平均值、中位数以及求和
print(user_info.age.max())
print(user_info.sum())
print('-------------------分隔线6-------------------')
# cumsum 也是用来求和的，不过它是用来累加求和的，也就是说它得到的结果与原始的 Series 或 DataFrame 大小相同
print(user_info.age.cumsum())
print('-------------------分隔线7-------------------')
# cumsum 也可以用来操作字符串类型的对象
print(user_info.sex.cumsum())
print('-------------------分隔线8-------------------')
# 想要一次性获取多个统计指标，只需调用 describe 方法即可
print(user_info.describe())
print('-------------------分隔线9-------------------')
# 如果想要查看非数字类型的列的统计指标，可以设置 include=["object"] 来获得
print(user_info.describe(include=['object']))
print('-------------------分隔线10-------------------')
# 统计某列中每个值出现的次数
print(user_info.sex.value_counts())
print('-------------------分隔线11-------------------')
# 获取某列最大值或最小值对应的索引，可以使用idxmax或idxmin方法
print(user_info.age.idxmax())
print('-------------------分隔线12-------------------')
# 将年龄进行离散化（分桶），直白来说就是将年龄分成几个区间,这里我们想要将年龄分成3个区间段,就可以使用cut方法
print(pd.cut(user_info.age, 3))
print('-------------------分隔线13-------------------')
# 自己定义区间段的大小
print(pd.cut(user_info.age, [1, 18, 30, 50]))
print('-------------------分隔线14-------------------')
# 离散化之后，想要给每个区间起个名字，可以指定 labels 参数
print(pd.cut(user_info.age, [1, 18, 30, 50], labels=['children', 'youth', 'middle']))
print('-------------------分隔线15-------------------')
# cut 是根据每个值的大小来进行离散化的，qcut 是根据每个值出现的次数来进行离散化的
print(pd.qcut(user_info.age, 3))
# 排序
################Pandas支持两种排序方式：按轴（索引或列）排序和按实际值排序################
# 按索引排序：sort_index 方法默认是按照索引进行正序排列的
print('-------------------分隔线16-------------------')
print(user_info.sort_index())
# 按照列进行倒序排列，可以设置参数 axis=1 和 ascending=False
print('-------------------分隔线17-------------------')
print(user_info.sort_index(axis=1, ascending=False))
# 按照实际值来排序
print('-------------------分隔线18-------------------')
print(user_info.sort_values(by='age'))
# 按照多个值来排序
print('-------------------分隔线19-------------------')
print(user_info.sort_values(by=['age', 'city']))
# 排序后，需要获取最大的n个值或最小值的n个值，我们可以使用 nlargest 和 nsmallest 方法来完成
print('-------------------分隔线20-------------------')
print(user_info.age.nlargest(2))
#####################函数应用##########################
# 1.常用到的函数有：map、apply、applymap, map 是 Series 中特有的方法，通过它可以对 Series 中的每个元素实现转换
print(user_info.age.map(lambda x: "yes" if x >= 30 else "no"))
print('-------------------分隔线21-------------------')
city_map ={
    'beijing': 'north',
    'shanghai': 'south',
    'nanjing': 'south',
    'hangzhou': 'south',
}
print(user_info.city.map(city_map))
print('-------------------分隔线22-------------------')
# apply 方法既支持 Series，也支持 DataFrame，在对Series操作时会作用到每个值上，在对DataFrame操作时会作用到所有行或所有列（通过 axis 参数控制）
# 对 Series 来说，apply 方法 与 map 方法区别不大
print(user_info.age.apply(lambda x: "yes" if x >= 30 else "no"))
print('-------------------分隔线23-------------------')
# 对 DataFrame 来说，apply 方法的作用对象是一行或一列数据（一个Series）
print(user_info.apply(lambda x: x.max(), axis=0))
# applymap 方法针对于 DataFrame，它作用于 DataFrame 中的每个元素，它对 DataFrame 的效果类似于 apply 对 Series 的效果
print('-------------------分隔线24-------------------')
print(user_info.applymap(lambda x: str(x).upper()))
print('-------------------分隔线25-------------------')
##############################修改列/索引名称#########################
# 1.修改列名只需要设置参数 columns 即可
print(user_info.rename(columns={'age': 'Age', 'city': 'City', 'sex': 'Sex'}))
# 2.修改索引名只需要设置参数 index 即可
print('-------------------分隔线25-------------------')
print(user_info.rename(index={'Tom': 'tom', 'Bob': 'bob'}))
##########################类型操作##################################
# 获取每种类型的列数,可以使用 get_dtype_counts 方法
print('-------------------分隔线26-------------------')
print(user_info.get_dtype_counts())
# 转换数据类型，可以通过 astype 来完成
print('-------------------分隔线27-------------------')
print(user_info['age'].astype(float))
print('-------------------分隔线28-------------------')
# 将 object 类型转为其他类型，常见的有转为数字、日期、时间差，Pandas 中分别对应 to_numeric、to_datetime、to_timedelta 方法
# 添加一些关于身高的信息
user_info["height"] = ["178", "168", "178", "180cm"]
print(user_info)
# 将身高这一列转为数字,180cm 并非数字，为了强制转换，我们可以传入 errors 参数，这个参数的作用是当强转失败时的处理方式
'''
默认情况下，errors='raise'，这意味着强转失败后直接抛出异常，
设置 errors='coerce' 可以在强转失败时将有问题的元素赋值为 pd.NaT（对于datetime和timedelta）或 np.nan（数字）。
设置 errors='ignore' 可以在强转失败时返回原有的数据
'''
print('-------------------分隔线29-------------------')
print(pd.to_numeric(user_info.height, errors='coerce'))
print('-------------------分隔线30-------------------')
print(pd.to_numeric(user_info.height, errors='ignore'))