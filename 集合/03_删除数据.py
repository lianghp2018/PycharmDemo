s1 = {10, 20, 30, 40, 50, 60, "s", "k"}
# remove()
# s1.remove(10)
# print(s1)
# 删除集合内没有的数据报错:KeyError
# s1.remove(10)

# discard() 删除集合内没有的数据不会报错
# s1.discard(10)
# s1.discard(20)
# print(s1)

# pop() 随机删除集合中某个数据,并返回这个数据
print(s1)
s = s1.pop()
print(s1)
print(s)
