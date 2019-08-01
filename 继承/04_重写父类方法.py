"""
如果子类和父类拥有同名的属性和方法,默认使用子类的属性和方法
"""


# 师父类, 属性,方法
class Master(object):
    def __init__(self):
        self.kongfu = "独门技术"

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_mike(self):
        print(f'运用{self.kongfu}获取牛奶')
        return


# 学校类
class School(object):
    def __init__(self):
        self.kongfu = "学校教授的技术"

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 徒弟类,继承师父类
class Prentice(School, Master):
    def __init__(self):
        self.kongfu = "自己研究出的技术"

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()
daqiu.make_mike()

# 类名.__mro__  查看类的继承关系
print(Prentice.__mro__)