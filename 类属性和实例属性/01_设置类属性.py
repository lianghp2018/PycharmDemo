"""
类属性:
    类对象所拥有的属性,被该类 所有的实例对象 所共有
    类属性可以使用 类对象(类名) 或 实例对象 访问
优点:
    1. 记录的某项数据 始终保持一致时,则定义类属性
    2. 实例属性 要求 每个对象 为其 单独开辟一份内存空间 来记录数据
        而 类属性 为全类所共有, 仅占用一份内存, 更加节省内存空间
"""


# 定义类属性
class Dog(object):
    tooth = 10

# 创建对象
wangcai = Dog()
xiaohei = Dog()

# 访问类型属性
print(Dog.tooth)  # 10
print(wangcai.tooth)  # 10
print(xiaohei.tooth)  # 10