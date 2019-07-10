i = 1
while i <=5:
    print(i)
    i += 1
    break
# 循环正常执行完成之后执行的代码 使用break关键字将不执行else
else:
    print('test')


str = 'you are'
for i in str:
    print(i)
    break
else:
    print(str)