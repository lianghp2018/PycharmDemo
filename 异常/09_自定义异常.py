"""
自定义异常:
    --捕获程序某些可能出现的情况并进行处理(不一定是bug)
    在Python中,抛出自定义异常的语法为:
        raise 异常类对象(参数列表)

    如 密码长度不足或过长,则报异常
"""


class ShortInputError(Exception):
    def __init__(self, length, min_length):
        self.length = length
        self.min_length = min_length

    # 抛出异常民描述信息
    def __str__(self):
        return f'输入的密码长为{self.length},少于{self.min_length}'


def main():
    try:
        psw = input('输入密码:')
        if len(psw) < 5:
            raise ShortInputError(len(psw), 5)
    except Exception as result:
        print(result)
    else:
        print('密码输入完毕!')


main()