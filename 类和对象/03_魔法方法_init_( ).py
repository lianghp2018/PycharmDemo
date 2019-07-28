"""
在Python中, _XX_()的函数叫做魔法方法
    _init_()方法:初始化对象,给对象赋予与生俱来的属性
        --创建一个对象时默认被调用,不需要手动调用
        --self参数不需要开发者传递,Python解释器或自动把当前的对象引用传递过去
        --带参数的_init_方法,可使创建多个对象的属性值不同
"""


class Washer:

    def __init__(self):
        self.height = 500
        self.width = 300

    def print_info(self):
        print(f'洗衣机的初始化高度是:{self.height}')
        print(f'洗衣机的初始化宽度是:{self.width}')


# 带参数的魔法方法_init_()
class Washer1:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def print_info(self):
        print(f'洗衣机的初始化高度是:{self.height}')
        print(f'洗衣机的初始化宽度是:{self.width}')


haier = Washer()
haier.print_info()

haier1 = Washer1(10, 20)
haier1.print_info()
