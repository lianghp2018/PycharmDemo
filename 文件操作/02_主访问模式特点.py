"""
测试目标:
    1.访问模式对文件的影响
    2.访问模式对write()的影响
    3.访问模式是否可以忽略

"""
# r : 如果文件不存在,报错
# FileNotFoundError: [Errno 2] No such file or directory: 'test1.txt'
# f = open('test1.txt', 'r')
# f = open('test.txt', 'r')
# io.UnsupportedOperation: not writable
# f.write('123')
# f.close()

# w : 只写,执行写入操作会覆盖原有内容,文件不存在会新建文件
# f = open('1.txt', 'w')
# f.write('w')
# f.close()

# a : 追加,执行写入操作追加内容, 文件不存在会新建文件
# f = open('1.txt', 'a')
# f.write('dfsghd')
# f.close()

# 访问模式参数可以省略,默认为 'r',前提是文件必须存在
f = open('1.txt')
f.close()