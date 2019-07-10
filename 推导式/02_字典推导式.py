"""
需求: 创建一个字典,key为1-5,value为对应数字的2次方
     将两个列表合并成一个字典
     提取字典中目标数据
"""
dict1 = {i: i ** 2 for i in range(1, 6)}
print(dict1)

# 合并
# 若两个列表数据个数不同,应选择数据个数少的列表进行统计,否则报错:IndexError: list index out of range
list1 = ['name', 'age', 'gender', 'test']
list2 = ['tom', '20', 'man']
dict2 = {list1[i]: list2[i] for i in range(len(list2))}
print(dict2)

# 提取目标数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
# 需求:提取上电脑数量大于等于200的字典数据
count1 = {key: value for key, value in counts.items() if value >= 200}
print(count1)
