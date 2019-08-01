"""
继承的概念
    生活中的继承:
        一般指子女继承父母的财产

    python面向对象的继承
        是指多个类之间的从属关系,即子类默认继承父类的所有属性和方法
    
    在Python中,所有类默认继承object类,object类是顶级类后基类,其他子类叫派生类
"""


# 父类
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)
        return


# 子类
class B(A):
    pass


result = B()
result.info_print()
