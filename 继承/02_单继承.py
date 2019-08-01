"""
事例:
    师父教得意弟子独门技术
"""


# 师父类, 属性,方法
class Master(object):
    def __init__(self):
        self.kongfu = "独门技术"

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 徒弟类,继承师父类
class Prentice(Master):
    pass


# 创建徒弟类对象
tudi = Prentice()
# print(tudi.kongfu)

tudi.make_cake()
