# 全局变量
i = 1


def test_a():
    # 局部变量
    j = 50
    print(f'局部变量 j = {j}')

    # 使用global关键字使用全局变量
    global i
    print(f'global声明的函数变量 i = {i}')
    i = 200
    print(f'在函数内部修改过的变量 i = {i}')


print(f'全局变量 i = {i}')
test_a()
print(f'全局变量 i = {i}')
