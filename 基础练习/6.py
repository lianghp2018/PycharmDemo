'''
i = int(input('输入一个数字:'))
if i < 0:
    print(i + 1)
    print(111)
elif i > 0:
    print('andoignodfgnishi')
else:
    print(234)

'''

age = int(input("输入年龄："))

if (age < 18):
    print(f'年龄不满18为:{age}')

#(age >= 18) and (age <= 60) 可以简写为 18 <= age <= 60
elif 18 <= age <= 60:
    print(f'{age}为合法工作年龄')
elif age > 60:
    print(f'{age}为退休年龄')
else:
    print(f'{age}为不合法输入')