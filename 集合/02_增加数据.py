s1 = {10, 20}

# add()
s1.add(100)
print(s1)
# 追加的数据重复,什么事情都不做
s1.add(10)
print(s1)
# 报错: TypeError: unhashable type: 'list'
# s1.add([1, 2])
# print(s1)

# update() 追加的是数据序列
s1.update({'name': 'tom', 'age': 20}.items())
print(s1)
# 报错:TypeError: 'int' object is not iterable
# s1.update(150)
# print(s1)