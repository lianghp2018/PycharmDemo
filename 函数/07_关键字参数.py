"""
关键字参数:
    函数参数通过"键 = 值"的形式指定,参数的顺序不再要求
    Ps:函数调用时,有位置参数则位置参数在前,关键字参数在后,
        关键字参数无先后顺序.
"""


def user_info(name, age, gender):
    print(f'name: {name}, age: {age}, gender: {gender} ')


user_info('Lily', age=20, gender='man')
user_info(gender='man', name='tom', age=20)
# user_info(gender='man', 'Lily', age=20)
