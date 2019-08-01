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
        # 如果先调用了父类的方法,kongfu属性会被父类覆盖
        # 所以此处先调用自己的初始化方法
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        # 让父类的kongfu属性覆盖上一次调用的kongfu属性
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        # 让父类的kongfu属性覆盖上一次调用的kongfu属性
        School.__init__(self)
        School.make_cake(self)


daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()

# 调用父类方法
daqiu.make_master_cake()

daqiu.make_school_cake()