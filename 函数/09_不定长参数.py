"""
不定长参数(可变参数):
    用于不确定参数个数的情况,即使是不传参数
    分为包裹位置传递和包裹关键字传递,两者都是一个组包的过程
"""


# 包裹位置传递:参数传入args变量,
# 根据传递的位置将参数合并为一个元组
def user_info(*args):
    print(args)
    return args


#   包裹关键字传递
def user_info1(**kwargs):
    print(kwargs)
    return kwargs


# ('tom',)
user_info('tom')
# ('Lily', 20)
t = user_info('Lily', 20)
print(type(t))

# {'name': 'tom', 'age': 20}
d = user_info1(name='tom', age=20)
print(type(d))
