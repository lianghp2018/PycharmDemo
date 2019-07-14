# 元组拆包
def return_num():
    return 100, 200


n1, n2 = return_num()
print(n1)
print(n2)

# 字典拆包:取出的是字典的key
dict1 = {'name': 'tom', 'age': 20}
a, b = dict1
print(a)
print(b)
print(dict1[a])
print(dict1[b])
