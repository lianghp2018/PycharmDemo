"""
当方法中需 要使用类对象 时, 定义类方法
    --类方法一般和类属性配合使用
"""


# 定义类属性
class Dog(object):
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth


# 创建对象
wangcai = Dog()
xiaohei = Dog()

# 访问类属性
print(Dog.get_tooth())  # 10
print(wangcai.get_tooth())  # 10
print(xiaohei.get_tooth())  # 10