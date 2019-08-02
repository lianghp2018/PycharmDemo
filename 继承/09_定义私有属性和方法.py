"""
私有化属性和方法的意义:
    -- 某些实例属性和方法不想让子类继承

设置私有权限的方法: 在属性名和方法名前加两个下划线 __

"""


# 师父类, 属性,方法
class Master(object):
    def __init__(self):
        self.kongfu = "独门技术"

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

    def make_mike(self):
        print(f'运用{self.kongfu}获取牛奶')


# 学校类
class School(object):
    def __init__(self):
        self.kongfu = "学校教授的技术"

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 徒弟类,继承师父类
class Prentice(School, Master):
    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money

    def __init__(self):
        self.kongfu = "自己研究出的技术"
        # 定义私有属性
        self.__money = 2000000

    # 定义私有方法
    def __info_print(self):
        print(self.kongfu)
        print(self.__money)

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class Tusun(Prentice):
    pass


t = Tusun()
p = Prentice()
p.set_money(100)
print(p.get_money())


#t.__info_print()