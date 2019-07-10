"""
需求:创建一个0-10的列表
    1.循环实现
    2.列表推导式实现
"""
# 1.1 while循环
list1 = []
i = 0
while i <= 10:
    list1.append(i)
    i += 1
print(list1)

# 1.2 for循环
list2 = []
for i in range(11):
    list2.append(i)
print(list2)

# 2.列表推导式
# 格式 [表达式 for 变量 in 列表] 
#     [表达式 for 变量 in 列表 if 条件]
list3 = [i for i in range(11)]
print(list3)

# 需求:0-10的偶数列表
list4 = [i for i in range(0, 11, 2)]
print(list4)
# if 实现
list5 = [i for i in range(11) if i % 2 == 0]
print(list5)
# 多个for循环实现列表推导式(嵌套循环)
list6 = [(i, j) for i in range(1, 10) if i % 3 == 0 for j in range(3)]
print(list6)
