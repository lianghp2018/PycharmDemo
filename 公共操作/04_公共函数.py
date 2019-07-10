# len() --计算容器中元素个数

# del or del() --删除

# max() --返回元素中最大值
str1 = 'sdgfiu'
list1 = [1, 2, 3, 4, 5]
dict1 = {'age': 30, 'name': 'ert'}
s = {1.5,  'sdgsdfg'}
print(max(str1))
print(max(list1))
print(max(dict1.items()))
# 如果max()比较set中的整数数据类型和str类型会报错:TypeError: '>' not supported between instances of 'str' and 'int'
print(max(s))
# min() --返回元素中最小值

# range(start, end, step) --生成start到end(不包括end)的数字,步长为step(默认为1),供for循环使用
# 生成1~9,start为1,step为1,
# 生成1,3,5,7,9 start为1,step为2,
# 生成0-9,range(10),start默认为0,step默认为1
# for i in range(1, 10, 2):
#     print(i)


# enumerate(可遍历对象,start=0) start参数用来设置遍历数据下标起始值,默认为0
# 返回元组,元组第一个数据是原迭代对象数据的对应下标,第二个数据是原迭代对象的数据
# --用于将一个可遍历是数据对象(如列表,元组,字符串)组合成为一个索引序列,
#   同时列出数据和数据下标,一般用在for循环中
# str1 = "sdgdsfhgdfshf"
# for i in enumerate(str1, start=1):
#     print(i)