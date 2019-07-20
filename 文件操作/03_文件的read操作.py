f = open('1.txt', 'r')
# 文件内容如果换行,底层有\n,占用1个字节
# read(num) : num表示从文件中读取数据的长度(单位是字节),
#             如果不写 num,则读取文件全部数据
# s = f.read(13)
# print(s)
# print(type(s))  # <class 'str'>

# readlines() : 按照 行 的方式把整个文件中的内容进行一次性读取,
#               并返回一个列表,每行数据作为一个元素
# line = f.readlines()
# print(line)
# print(type(line))   # <class 'list'>

# readline() : 每次读取一行数据
# l1 = f.readline()
# print(l1)
# l1 = f.readline()
# print(l1)

f.close()