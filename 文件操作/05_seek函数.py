"""
seek(): 用来移动文件指针
    文件对象.seek(偏移量, 起始位置) 0开头1当前2结尾

目标:
    1. r 改变文件指针位置:改变读取数据开始位置或把文件指针放结尾(无法读取数据)
    2. a 改变文件指针位置,做到可以读取数据
"""
f = open('1.txt', 'r+')
f1 = open('1.txt', 'a+')
f.seek(2, 0)
# f.seek(0, 2)    # 无法读取数据
con = f.read()
print(con)
# f1.seek(0, 0)
f1.seek(0)
con1 = f1.read()
print(con1)
f.close()
