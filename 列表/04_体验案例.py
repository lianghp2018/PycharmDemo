name_list = ['tom', 'Lily', 'Rose']

name = input('请输入名字:')

if name in name_list:
    print(f'{name}用户已存在！！')

# else
elif name not in name_list:
    print(f'{name}可以注册！！')
