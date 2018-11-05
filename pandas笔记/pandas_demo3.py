#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Version: python 3.5.2
# Tools: Pycharm 2017.2.2

import pandas as pd
import numpy as np

"""Pandas缺失值处理"""

# 缺失值表示的是“缺失的数据”,实际生活中可能由于有的数据不全所以导致数据缺失，也有可能由于误操作导致数据缺失，又或者人为造成数据缺失

index = pd.Index(data=['Tom', 'Bob', 'Curry', 'Durant', 'Harden', 'James'], name='name')
data = {
    'age': [20, np.nan, 40, 29, 28, np.nan],
    'city': ['Beijing', 'Shanghai', 'Guangzhou', 'Nanjing', ' ', np.nan],
    'sex': [None, 'male', 'female', 'male', np.nan, 'unknown'],
    'birth': ['2000-02-10', '1988-10-17', None, '1989-08-12', np.nan, '1987-12-23'],
}
user_info = pd.DataFrame(data=data, index=index)
# 将生日日期转为时间戳
user_info['birth'] = pd.to_datetime(user_info.birth)
print(user_info)
# 可以使用 isnull() 或 notnull() 方法来操作,识别出哪些是缺失值或非缺失值
print('----------------------snip1---------------------')
print(user_info.isnull())
print('----------------------snip2---------------------')
print(user_info.notnull())
# 过滤掉一些缺失的行
print('---------------------snip3----------------------')
print(user_info[user_info.birth.notnull()])
#  1.丢弃缺失值
# Series丢弃缺失值
print('---------------------snip4----------------------')
print(user_info.age.dropna())
# Seriese 使用 dropna 比较简单，对于 DataFrame 来说，可以设置更多的参数
"""
axis 参数用于控制行或列，跟其他不一样的是，axis=0 （默认）表示操作行，axis=1 表示操作列
how 参数可选的值为 any（默认） 或者 all。any 表示一行/列有任意元素为空时即丢弃，all 一行/列所有值都为空时才丢弃
subset 参数表示删除时只考虑的索引或列名
thresh参数的类型为整数，它的作用是，比如 thresh=3，会在一行/列中至少有 3 个非空值时将其保留
"""
print('------------------snip5---------------------')
# 一行/列所有值都为空时才丢弃
print(user_info.dropna(axis=0, how='all'))
print('-----------------snip6---------------------')
# 一行/列有任意元素为空时即丢弃
print(user_info.dropna(axis=0, how='any'))
# 一行数据中只要 city 或 sex 存在空值即删除
print('-----------------snip7---------------------')
print(user_info.dropna(axis=0, how='any', subset=['city', 'sex']))
# 2.填充缺失值------------使用 fillna 完成填充
# 填充缺失值时，常见的一种方式是使用一个标量来填充
print('-----------------snip8---------------------')
print(user_info.age.fillna(0))
print('-----------------snip9---------------------')
# 用前一个或后一个有效值来填充,设置参数 method='pad' 或 method='ffill' 可以使用前一个有效值来填充
print(user_info.age.fillna(method='ffill'))
# 设置参数 method='bfill' 或 method='backfill' 可以使用后一个有效值来填充
print('----------------snip10---------------------')
print(user_info.birth.fillna(method='backfill'))
# 通过 interpolate 方法来填充,默认情况下使用线性差值，可以是设置 method 参数来改变方式
print('----------------snip11---------------------')
print(user_info.age.interpolate())
# 3.替换缺失值
# 有时候在我们人类的眼中，某些异常值我们也会当做缺失值来处理
# 使用 replace 方法来替换缺失值
print('---------------snip12---------------------')
print(user_info.age.replace(40, np.nan))
# 也可以指定一个映射字典
print('---------------snip13--------------------')
print(user_info.age.replace({40: np.nan}))
# 对于 DataFrame，可以指定每列要替换的值
print('--------------snip14---------------------')
print(user_info.replace({'age': 40, "birth": pd.to_datetime('1987-12-23')}, np.nan))
# 可以将特定字符串进行替换，如：将 "unknown" 进行替换
print('--------------snip15--------------------')
print(user_info.replace({'sex': 'unknown'}, np.nan))
# 除了可以替换特定的值之外，还可以使用正则表达式来替换，如：将空白字符串替换成空值
print('-------------snip16---------------------')
print(user_info.city.replace(r'\s+', np.nan, regex=True))
# 4.使用其他对象填充
"""
例如有两个关于用户年龄的 Series，其中一个有缺失值，另一个没有，我们可以将没有的缺失值的 Series 中的元素传给有缺失值的
"""
print('------------snip17-------------------- ')
age_new = user_info.age.copy()
age_new.fillna(20, inplace=True)
print(age_new)
print('------------snip18--------------------')
print(user_info.age.combine_first(age_new))