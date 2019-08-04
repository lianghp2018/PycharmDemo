"""
异常: 错误,bug, 异常处理可以防止程序报错
    语法:
        try:
            可能发生错误的代码
        except 异常类型:
            如果出现异常执行的代码
PS: 1. 如果尝试执行的代码的异常类型与要捕获的异常类型不一致,则无法捕获异常
    2. 一般try下方只放一行尝试执行的代码


自定义异常:
    捕获程序某些可能出现的情况并进行处理(不一定是bug)
"""
try:
    f = open('1.txt', 'r')
except FileNotFoundError:
    print('such file is no exist.')
