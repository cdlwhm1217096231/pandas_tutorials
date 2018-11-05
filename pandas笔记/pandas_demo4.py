#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-17 11:37:43
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import pandas as pd
import numpy as np

"""处理Pandas中的文本(字符串)"""

# 1.为什么使用str属性
'''文本数据也就是我们常说的字符串，Pandas为 Series提供了 str 属性，通过它可以方便的对每个元素进行操作'''
index = pd.Index(data=['Tom', 'Bob', 'Mary', 'James',
                       'Andy', 'Alice'], name='name')
data = {
    'age': [18, 30, np.nan, 40, np.nan, 30],
    'city': ['Bei Jing', 'Shang Hai', 'Nan Jing', 'Shen Zhen', np.nan, ' '],
    'sex': [None, 'male', 'female', 'male', np.nan, 'unknown'],
    'birth': ['2002-02-10', '1988-12-23', None, '1978-09-10', np.nan, '1988-10-19'],
}
user_info = pd.DataFrame(data=data, index=index)
# 将出生日期转为时间戳
user_info['birth'] = pd.to_datetime(user_info.birth)
print(user_info)
print('-----------------snip-------------------')
# print(user_info.city.map(lambda x: x.lower()))
'''报错,因为 float 类型的对象没有 lower 属性,这是因为缺失值（np.nan）属于float 类型'''
print('-----------------snip-------------------')
# 将文本转为小写
print(user_info.city.str.lower())
print('-----------------snip-------------------')
# 统计每个字符串的长度
print(user_info.city.str.len())
# 2.替换和分割
# 使用 .srt 属性也支持替换与分割操作
print('-----------------snip-------------------')
print(user_info.city.str.replace(' ', '_'))
# replace 方法还支持正则表达式，例如将所有开头为 S 的城市替换为空字符串
print('-----------------snip-------------------')
print(user_info.city.str.replace(r'^S.*', ' '))
print('-----------------snip-------------------')
# 分割操作
print(user_info.city.str.split(" "))
print('-----------------snip-------------------')
# 分割列表中的元素可以使用 get 或 [] 符号进行访问
print(user_info.city.str.split(" ").str.get(1))
print('-----------------snip-------------------')
print(user_info.city.str.split(" ").str[1])
print('-----------------snip-------------------')
# 设置参数 expand=True 可以轻松扩展此项以返回 DataFrame
print(user_info.city.str.split(' ', expand=True))
print('-----------------snip-------------------')
# 3.提取子串-------------从一个长的字符串中提取出子串
# 3.1提取第一个匹配的子串
"""extract 方法接受一个正则表达式并至少包含一个捕获组，指定参数 expand=True 可以保证每次都返回 DataFrame"""
print(user_info.city.str.extract("(\w+)\s+", expand=True))
print('-----------------snip-------------------')
# 如果使用多个组提取正则表达式会返回一个 DataFrame，每个组只有一列
print(user_info.city.str.extract("(\w+)\s+(\w+)", expand=True))
print('-----------------snip-------------------')
# 3.2匹配所有子串
'''extract 只能够匹配出第一个子串，使用 extractall 可以匹配出所有的子串'''
print(user_info.city.str.extractall('(\w+)\s+'))
# 3.3测试是否包含子串
'''除了可以匹配出子串外，我们还可以使用 contains 来测试是否包含子串,测试城市是否包含子串 “Zh”'''
print('-----------------snip-------------------')
print(user_info.city.str.contains('Zh'))
print('-----------------snip-------------------')
# 正则表达式也是支持的。例如，想要测试是否是以字母 “S” 开头
print(user_info.city.str.contains('^S'))
# 4.生成哑变量
'''通过 get_dummies 方法可以将字符串转为哑变量，sep 参数是指定哑变量之间的分隔符'''
print('-----------------snip-------------------')
print(user_info.city.str.get_dummies(sep=' '))
# 5.方法摘要
'''
cat()			连接字符串
split()			在分隔符上分割字符串
rsplit()		从字符串末尾开始分隔字符串
get()			索引到每个元素（检索第i个元素）
join()			使用分隔符在系列的每个元素中加入字符串
get_dummies()	在分隔符上分割字符串，返回虚拟变量的DataFrame
contains()		如果每个字符串都包含pattern / regex，则返回布尔数组
replace()		用其他字符串替换pattern / regex的出现
repeat()		重复值（s.str.repeat(3)等同于x * 3 t2 >）
pad()			将空格添加到字符串的左侧，右侧或两侧
center()		相当于str.center
ljust()			相当于str.ljust
rjust()			相当于str.rjust
zfill()			等同于str.zfill
wrap()			将长长的字符串拆分为长度小于给定宽度的行
slice()			切分Series中的每个字符串
slice_replace()	用传递的值替换每个字符串中的切片
count()			计数模式的发生
startswith()	相当于每个元素的str.startswith(pat)
endswith()		相当于每个元素的str.endswith(pat)
findall()		计算每个字符串的所有模式/正则表达式的列表
match()			在每个元素上调用re.match，返回匹配的组作为列表
extract()	在每个元素上调用re.search，为每个元素返回一行DataFrame，为每个正则表达式捕获组返回一列
extractall()	在每个元素上调用re.findall，为每个匹配返回一行DataFrame，为每个正则表达式捕获组返回一列
len()			计算字符串长度
strip()			相当于str.strip
rstrip()		相当于str.rstrip
lstrip()		相当于str.lstrip
partition()		等同于str.partition
rpartition()	等同于str.rpartition
lower()			相当于str.lower
upper()			相当于str.upper
find()			相当于str.find
rfind()			相当于str.rfind
index()			相当于str.index
rindex()		相当于str.rindex
capitalize()	相当于str.capitalize
swapcase()		相当于str.swapcase
normalize()		返回Unicode标准格式。相当于unicodedata.normalize
translate()		等同于str.translate
isalnum()		等同于str.isalnum
isalpha()		等同于str.isalpha
isdigit()		相当于str.isdigit
isspace()		等同于str.isspace
islower()		相当于str.islower
isupper()		相当于str.isupper
istitle()		相当于str.istitle
isnumeric()		相当于str.isnumeric
isdecimal()		相当于str.isdecimal
'''
