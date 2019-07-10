dict1 = {'name': 'TOM', 'age': 20, 'gender': '男'}

# 键值对查找
print(dict1['name'])

# get()
print(dict1.get('name'))
print(dict1.get('names', 'Lily'))
print(dict1.get('names'))

# keys()
print(dict1.keys())

# values()
print(dict1.values())

# items()
print(dict1.items())

# 遍历键值对
for key, value in dict1.items():
    print(f'{key} = {value}')