#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-18 11:09:38
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import pandas as pd
import numpy as np

# 1.创建对象
"""
在创建分类数据之前，先来了解下什么是分类（Category）数据呢？分类数据直白来说就是取值为有限的，或者说是固定数量的可能值,例如：性别、血型
"""
# 一种有效的方法就是明确指定 dtype="category"
index = pd.Index(data=['Tom', 'Bob', 'James', 'Curry',
                       'Mary', 'Alice'], name='name')
user_info = pd.Series(data=['A', 'O', 'B', 'AB', 'A', np.nan],
                      index=index, name='blood_type', dtype="category")
print(user_info)
print('-------------------snip---------------')
# 也可以使用 pd.Categorical 来构建分类数据
print(pd.Categorical(['A', 'O', 'B', 'AB', 'A', np.nan]))
print('-------------------snip---------------')
# 也可以自己制定类别数据所有可能的取值，假定我们认为血型只有 A、B 以及 AB 这三类，那么我们可以这样操作
print(pd.Categorical(['A', 'O', 'B', 'AB', 'A', np.nan],
                     categories=['A', 'B', 'AB']))
print('-------------------snip---------------')
# 将已经创建好的一个Series将它转为分类数据
user_info = pd.Series(
    data=['A', 'O', 'B', 'AB', 'A', np.nan], index=index, name='blood_type')
user_info = user_info.astype('category')
print(user_info)
print('-------------------snip---------------')
# 2.常用操作
# 可以对分类数据使用 .describe() 方法，它得到的结果与 string类型的数据相同
print(user_info.describe())
print('-------------------snip---------------')
# 可以使用 .cat.categories 来获取分类数据所有可能的取值
print(user_info.cat.categories)
print('-------------------snip---------------')
# 修改分类数据的名称
print(user_info.cat.rename_categories(['A+', 'AB+', 'B+', 'O+']))
print('-------------------snip---------------')
# 除了重命名，也会遇到添加类别，删除分类的操作，这些都可以通过 .cat.add_categories ，.cat.remove_categories 来实现
# 分类数据也支持使用 value_counts 方法来查看数据分布
print(user_info.value_counts())
print('-------------------snip---------------')
# 分类数据也支持使用 .str 属性来访问的
print(user_info.str.contains('O'))
print('-------------------snip---------------')
# 合并数据,借助 pd.concat 来完成
blood_type1 = pd.Categorical(['A', 'AB'])
blood_type2 = pd.Categorical(['B', 'O'])
print(pd.concat([pd.Series(blood_type1), pd.Series(blood_type2)]))
print('-------------------snip---------------')
# 分类数据经过 pd.concat 合并后类型转为了 object 类型。如果想要保持分类类型的话，可以借助 union_categoricals 来完成
from pandas.api.types import union_categoricals
print(union_categoricals([blood_type1, blood_type2]))
print('-------------------snip---------------')
# 3. 内存使用量的陷阱
# Categorical 的内存使用量是与分类数乘以数据长度成正比，object 类型的数据是一个常数乘以数据的长度
blood_type = pd.Series(['AB', 'O', 'A', 'B', np.nan, 'A'] * 1000)
print('object 类型的数据的长度:\n', blood_type.nbytes)
print('-------------------snip---------------')
print('转换成分类数据的长度:\n', blood_type.astype('category').nbytes)
print('-------------------snip---------------')
# 当类别的数量接近数据的长度，那么 Categorical 将使用与等效的 object 表示几乎相同或更多的内存
blood_type = pd.Series(['AB%04d' % i for i in range(2000)])
print('object 类型的数据的长度:\n', blood_type.nbytes)
print('-------------------snip---------------')
print('转换成分类数据的长度:\n', blood_type.astype('category').nbytes)
