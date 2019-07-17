"""
filter(func, lst): 用于过滤序列,过滤掉不符合条件的元素,返回一个filter对象,
                    如果要转换成列表,使用list()转换
"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 过滤序列中的偶数
def func(x):
    # return x > 5  可根据需求修改过滤条件
    return x % 2 == 0


result = filter(func, list1)
print(result)   # <filter object at 0x7f2a53080780>
print(list(result))  # [2, 4, 6, 8, 10]
