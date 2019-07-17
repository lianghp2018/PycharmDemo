"""
高阶函数: 将函数作为参数传递到另一个函数中

"""
# abs(): 绝对值
# print(abs(-9))

# # round: 四舍五入
# print(round(0.6))
# print(0.3)


def add_num(a, b):
    return abs(a) + abs(b)


result = add_num(1, -5)
print(result)


# 高阶函数(higher-order function) : 灵活性高,代码量少
def sum_num(a, b, func):    # func形参传入函数名
    return func(a) + func(b)


func_sum = sum_num(3, -9.6, abs)
print(func_sum)
