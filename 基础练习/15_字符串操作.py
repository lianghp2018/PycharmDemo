mystr = "hello world and itcast and itheima and python"

# 字符串查找操作

# find() rfind() 右侧开始查找
# print(mystr.find('and'))
# print(mystr.find('and', 15, 36))
# print(mystr.find('ands')) # find找不到子串返回 -1

# index() rindex() 右侧开始查找
# print(mystr.index('and'))
# print(mystr.index('and', 15, 36))
# print(mystr.index('ands')) index找不到子串报错

# count() 计数
# print(mystr.count('and'))  # 3
# print(mystr.count('and', 15, 36))  # 1
# print(mystr.count('ands'))  # 0

# -------------------------------------------

# 字符串修改操作

# replace() 将字符串中旧子串 替换 新子串
# 语法 字符串序列.replace(旧子串, 新子串, 替换次数)
'''
    **reolace()有返回值,返回替换后的字符串,原字符串不变
    说明 字符串是不可变数据类型
    数据类型根据是否可以改变分为：可变数据类型 和 不可变数据类型
'''
# new_str = mystr.replace('and', 'he', 1)
# print(mystr)
# print(type(new_str))
# print(new_str)
#
# # split() 按照指定字符分割字符串，返回一个列表,并且会丢失分割字符
# # 语法： 字符串序列.split(分割字符. 分割次数)
# new_strList = mystr.split('and', 1)
# print(type(new_strList))
# print(new_strList)

# join() 用一个字符或字符串合并列表里的字符串数据为一个大字符串
# mylist = ['aa', 'bb', 'cc']
# new_list = '...'.join(mylist)
# print(new_list)

# capitalize() 将字符串首字母改成大写
# new_str = mystr.capitalize()
# print(new_str)
#
# # title() 每个单词首字母大写
# new_str1 = mystr.title()
# print(new_str1)

# upper() 小写转大写
# lower() 大写转小写

# lstrip() 删除字符串左侧空白字符
# rstrip() 删除字符串右侧空白字符
# strip()  删除字符串两侧空白字符

# ljust() 返回一个原字符串左对齐,
# rjust() 返回一个原字符串右对齐,
# center() 返回一个原字符串居中对齐,
#         并使用指定字符（默认空格）填充至对应长度的新字符串
# 语法: 字符串序列.ljust(长度, 填充字符)
# str = 'Hello'
# print(str.ljust(10, '.'))
# print(str.rjust(10, '.'))
# print(str.center(10, '.'))

# ----------------------------

# 判断

# startswith() 检查字符串是否是以指定子串开头
# endswith() 检查字符串是否是以指定子串结尾
# 返回值是True 或 False
# 语法: 字符串序列.startswith(子串, 开始下标, 结束下标)
# b = mystr.startswith('hello', 0, 10)
# b1 = mystr.endswith('python')
# print(b)
# print(b1)

# isalpha() 判断是否全是字母
# isdigit() 判断是否全是数字
# isalnum() 数字或字母或数字和字母
# isspace() 空白(空格)
#           必须是非空字符串, 返回值都是 bool类型
