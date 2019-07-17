"""
reduce(func,lst) : 其中参数func必须有两个参数.每次func计算的结果继续和序列的下一个元素
                    作累积计算
Ps: 需要import functools,
"""
import functools

list1 = [1, 2, 3, 4, 5]


def func(a, b):
    # return a + b
    return a * b


result = functools.reduce(func, list1)
print(result)  # 120
