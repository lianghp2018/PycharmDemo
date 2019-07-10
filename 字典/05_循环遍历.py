dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}

# keys()
for key in dict1.keys():
    print(key)

# values()
for v in dict1.values():
    print(v)

# items()
for it in dict1.items():
    print(f'{it}的数据类型是:{type(it)}')

# 遍历键值对(拆包):
for key, value in dict1.items():
    # print(key)
    # print(value)
    print(f'{key} = {value}')


