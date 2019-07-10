name_list = ['tom', 'Lily', 'Rose']

# append() 列表结尾追加数据
# 将数据整体追加
name_list.append('lhp')
new_list = ['sdef', 'sdghjgj']
name_list.append(new_list)
print(name_list)

# extend(): ；列表结尾追加数据，如果数据是一个列表，则逐一添加到列表
# 将数据拆开追加
#new_list = ['sdef', 'sdghjgj']
# name_list.extend(new_list)
# s = name_list.extend(0, 'xiaoming')
# # ['tom', 'Lily', 'Rose', 'lhp', 'sdef', 'sdghjgj', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g']
# print(name_list)

# insert(): 指定位置新增数据
# 语法： 列表序列.insert(位置下标, 数据)
# name_list.insert(1, 'dshf')
# print(name_list)
