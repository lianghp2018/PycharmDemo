"""
1.需要通过 @staticmethod 来进行修饰.
2.不需要传递类对象或实例对象(形参没有self/cls)
3.可通过 实例对象 或 类对象访问

当方法中不需要使用 实例对象(如实例对象,实例属性) 和
                类对象(如类方法,类属性或创建实例等) 时,定义静态方法
取消不需要的参数传递,有利于 减少不必要的内存占用和性能消耗

"""


# 定义类属性
class Dog(object):
    @staticmethod
    def info_print():
        print('这是一个狗类........')


wangcai = Dog()
wangcai.info_print()
Dog.info_print()
