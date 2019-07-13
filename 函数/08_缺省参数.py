"""
缺省参数:
    为参数提供默认值,在参数列表的最后定义
    Ps:函数调用时为其传值则覆盖默认值
"""


def user_info(name, age, gender='man'):
    print(f'name: {name}, age: {age}, gender: {gender} ')


user_info('tom', 20)
user_info('Lily', 20, 'woman')
