"""
super(当前类名, self).函数名()
    方法1,带参数,多层继承中继承关系为
        --徒弟 继承 学校
        --学校 继承 师父
        当徒弟想调用所有父类(师父类,学校类)的同名方法时,
        需要在同样继承了师父类的 学校类中 的同名方法中也添加带参数的super()代码语句
       *该方法依旧没有解决函数名改变时程序员需要修改代码的工作量

    方法2,无参数  super().函数名()
        同上
        学校类同名方法也需要带无参数super()代码语句
       *该方法成功解决了上述问题  
"""

# 师父类, 属性,方法
class Master(object):
    def __init__(self):
        self.kongfu = "独门技术"

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 学校类 继承师父类
class School(Master):
    def __init__(self):
        self.kongfu = "学校教授的技术"

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

        # 方法2.1 带参数 super()
        # super(School, self).__init__()
        # super(School, self).make_cake()

        # 方法2.2 无参数的super()
        super().__init__()
        super().make_cake()
        return


# 徒弟类,继承师父类
class Prentice(School):
    def __init__(self):
        self.kongfu = "自己研究出的技术"

    def make_cake(self):
        # 如果先调用了父类的方法,kongfu属性会被父类覆盖
        # 所以此处先调用自己的初始化方法
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_master_cake(self):
        # 让父类的kongfu属性覆盖上一次调用的kongfu属性

        # 方法1. 该方法代码冗余,父类名改变需要修改多处代码
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        # 让父类的kongfu属性覆盖上一次调用的kongfu属性
        School.__init__(self)
        School.make_cake(self)

    def make_old_cake(self):
        # 方法2.1 使用super(当前类名, self).函数名()
        # 带参数
        # super(Prentice, self).__init__()
        # super(Prentice, self).make_cake()

        # 方法2.2 无参数的super()
        super().__init__()
        super().make_cake()


daqiu = Prentice()

daqiu.make_old_cake()
