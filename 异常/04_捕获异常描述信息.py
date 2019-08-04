try:
    print(1/0)
# 在异常类型后使用 as 关键字, 后跟 任意 变量名
except (NameError, ZeroDivisionError) as result:
    print('here have a error')
    print(result)