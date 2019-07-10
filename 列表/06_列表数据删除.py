name_list = ['tom', 'Lily', 'Rose']

# del 删除列表或列表指定下标数据
# 语法： del 列表名 or del(列表名)

# del name_list
# del name_list[1]
# print(name_list)

# pop() -- 删除指定下标的数据，如果不指定下标，默认删除最后一个数据，
# 有返回值，返回被删除的数据
# del_list = name_list.pop(1)
# print(del_list)
# print(name_list)

# remove(数据)
# name_list.remove('Rose')
# print(name_list)

# clear() 清空
name_list.clear()
print(name_list)