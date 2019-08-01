"""
多继承旧时一个类同时继承了多个父类
    当一个类有多个父类时,默认使用第一个父类的同名属性和方法
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
    pass


daqiu = Prentice()
daqiu.make_cake()
daqiu.make_mike()