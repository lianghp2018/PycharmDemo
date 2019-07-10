list1 = [1, 2, 3, 4, 5]
set1 = {100, 200, 300}
tuple1 = ('a', 'b', 'c')

# tuple() 转换成元组
print(tuple(list1))
print(tuple(set1))
# list()
print(list(set1))
print(list(tuple1))
# set()
print(set(list1))
print(set(tuple1))