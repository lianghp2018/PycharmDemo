
def sum(a, b):
    print(a + b)


# 防止运行测试代码
if __name__ == '__main__':
        # 测试代码, 测试功能是否有bug
        sum(1, 2)
"""
__name__ 是一个系统变量,是模块的标识符,值是:
          1. 在当前文件打印是: __main__
          2. 当被其他文件导入,打印的是 模块文件名
print(__name__)
"""