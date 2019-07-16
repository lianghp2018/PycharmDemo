"""
递归: 1.函数内部调用自己
     2.需要出口
"""


# 需求: 数字累加
def sum_number(num):
    # 函数出口
    if num == 1:
        return 1
    # 递归
    return num + sum_number(num - 1)


sum_result = sum_number(100)
print(sum_result)
print(type(sum_result))
