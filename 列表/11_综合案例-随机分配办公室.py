# 需求： 8位老师 3个办公室 随机分配办公室
"""
步骤：
1 准备数据
    1.1 8位老师 --列表
    1.2 3个办公室 --列表（嵌套）

2 分配老师到办公室
    *** 随机分配
    将老师的名字写入到办公室列表 --列表追加

3 验证是否分配成功
    打印办公室列表信息

"""
# 1.准备数据

import random


teachers = ['A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H']
offices = [[], [], []]

# 2.分配老师到办公室
# 遍历数据
for t in teachers:
    # 随机选择一个办公室
    index = random.randint(0, 2)
    # 将老师追加到办公室
    offices[index].append(t)
# 打印办公室信息
print(offices)

# 验证是否分配成功
i = 1
for office in offices:
    print(f'办公室{i}的人数是{len(office)},分别是：')
    for t in office:
        print(t, end="\t")
    print()
    i += 1
