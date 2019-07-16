"""
Python中,值是靠引用传递的
    id()可以用来判断是否是同一引用
"""

# 不可变类型
a = 1
b = a
print(id(a))
print(id(b))

a = 2
print(b)
print(id(a))
print(id(b))


# 可变类型
aa = [100, 200]
bb = aa
print(id(aa))
print(id(bb))
aa.append(300)
print(bb)
print(id(aa))
print(id(bb))
