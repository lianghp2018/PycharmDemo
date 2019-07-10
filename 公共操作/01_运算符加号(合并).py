s1 = 'you'
s2 = ' are'
s3 = s1 + s2
print(s3)

l1 = [1, 2, 3]
l2 = [4, 5]
print(l1 + l2)

t1 = ('qwe', 'poi')
t2 = ('asd',)
print(t1 + t2)

dict1 = {'name': 'qwe', 'age': 20}
dict2 = {'gender': '男'}
# 报错,字典不支持加号运算符合并
print(dict1 + dict2)
