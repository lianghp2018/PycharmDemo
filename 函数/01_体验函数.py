"""
函数先定义后使用,先调用会报错:
    NameError: name 'sel_func' is not defined

定义函数的语法:
函数前后都需要空两行


def 函数名(参数):
    代码1
    代码2
    .....


函数的调用:
函数名(参数)
"""


def sel_func():
    print('I love ')
    print('you')


print('I love you')
# 调用函数
sel_func()
