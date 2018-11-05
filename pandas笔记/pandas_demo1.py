#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-14 22:06:04
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
####pandas常用的数据结构有两种，series和dataframe，这些数据结构建立在numpy数组上，所以它的效率很高######
# 1.series是一个带名称和索引的一维数组，数组中元素的类型可以是整数、浮点、字符串、python对象
user_age = pd.Series(data=[18, 30, 45, 32])
print(user_age)
print('---------------------分隔线1-----------------')
# 通过Series的索引index来解决问题
user_age.index = ['Tom', 'Curry', 'Mary', 'James']
print(user_age)
# 给Series的索引加上名字name,表示索引的含义
user_age.index.name = "name"
print('----------------------分隔线2----------------')
print(user_age)
# 给Series起个名字
user_age.name = "user_age_info"
print('----------------------分隔线3----------------')
print(user_age)
# 总结：通过上面的一系列操作，得出一个Series包含data、index、name
############################快速实现上面的功能########################
# 构建索引
name = pd.Index(['Tom', 'Curry', 'Mary', 'James'], name='name')
# 构建Series
user_age = pd.Series(data=[18, 30, 45, 32], index=name, name='user_age_info')
print('----------------------分隔线4-----------------')
print(user_age)
# 此外，构建Series时，并没有设定每个元素的数据类型，这时候pandas会自动判断一个数据类型，并作为Series的数据类型，也可以手动指定数据类型
user_age = pd.Series(data=[18, 30, 45, 32], index=name,
                     name='user_age_info', dtype=float)
print('---------------手动指定数据类型----------------')
print(user_age)
#######################Series像dict,将index看作是dict中的key##################
print(user_age['Curry'])
# 通过get方法获取某个值,当索引不存在时,不会抛出异常
print(user_age.get('Curry'))
######################Series像ndarry，这意味着可以进行切片操作#################
print('获取第一个元素:{}'.format(user_age[0]))
print('获取前三个元素:\n{}'.format(user_age[:3]))
print('获取年龄大于30的元素\n%s' % (user_age[user_age > 30]))
print('获取第四个和第二个元素\n:{}'.format(user_age[[3, 1]]))
# 向量化操作
print(user_age + 1)
print(np.exp(user_age))
print('------------------分隔线5----------------')
# 2.DataFrame数据结构
# DataFrame 是一个带有索引的二维数据结构，每列可以有自己的名字，并且可以有不同的数据类型。你可以把它想象成一个 excel表格或者数据库中的一张表，DataFrame是最常用的Pandas对象

# 构建一个dict，key是需要存储的信息，value是信息列表，然后将dict传递给data参数
index = pd.Index(data=['Tom', 'Curry', 'Mary', 'James'], name='name')
data = {
    'age': [18, 30, 45, 32],
    'city': ['beijing', 'shanghai', 'nanjing', 'hangzhou']
}
user_info = pd.DataFrame(data=data, index=index)
print(user_info)
# 先构建一个二维数组，然后再生成一个列名称列表
data = [[18, 'beijing'], [30, 'shanghai'], [45, 'nanjing'], [32, 'hangzhou']]
columns = ['age', 'city']
user_info = pd.DataFrame(data=data, index=index, columns=columns)
print('------------------分隔线6-------------------')
print(user_info)
############访问行##################
# 通过索引名来访问某行，借助loc方法
print(user_info.loc['Curry'])
# 通过这行所在的位置来选择这一行
print('------------------分隔线7-------------------')
print(user_info.iloc[0])
# 访问多行
print('------------------分隔线8-------------------')
print(user_info.iloc[1:3])
####################访问列###################
print('------------------分隔线9-------------------')
print(user_info['age'])
# 同时访问多个列
print('------------------分隔线10-------------------')
print(user_info[['age', 'city']])
####################新增或者删除列##################
# 新增列
user_info['sex'] = 'male'
print('------------------分隔线12-------------------')
print(user_info)
# 上述方法，添加的某列的取值都相同,不符合实际数据
user_info['sex'] = ['male', 'male', 'female', 'male']
print('------------------分隔线13-------------------')
print(user_info)
# 删除某列
print('------------------分隔线14-------------------')
user_info.pop('sex')
print(user_info)
