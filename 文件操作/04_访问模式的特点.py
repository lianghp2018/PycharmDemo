"""
测试目标
    1. r+, w+, a+的区别:
        r+: 文件不存在会报错,文件指针在开头,所以能读取数据
        w+: 没有文件会新建文件,文件指针在开头,用新内容覆盖原内容
        a+: 没有文件会新建文件,文件指针在结尾,无法读取(文件指针后没有数据)
    2. 文件指针对数据的影响
"""
# r+
# f = open('1.txt', 'r+')
# con = f.read()
# print(con)

# w+
# f = open('2.txt', 'w+')
# con = f.read()
# print(con)

# a+
f = open('1.txt', 'a+')
con = f.read()
print(con)
f.close()
