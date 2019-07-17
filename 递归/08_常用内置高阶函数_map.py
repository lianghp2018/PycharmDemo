"""
map(func, lst):
    将传入的函数变量func作用到lst变量的每个元素中,
    并将结果自称的新列表(Python2)/迭代器(Python3)返回
"""
# 需求: 计算list 序列中的每个数字的2次方
list1 = [1, 2, 3, 4, 5]


def func(x):
    return x ** 2


result = map(func, list1)
print(result)  # <map object at 0x7f950afe9748>
print(list(result))  # [1, 4, 9, 16, 25]
