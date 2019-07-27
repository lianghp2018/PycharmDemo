# 1.用户输入目标文件
old_name = input('备份文件名:')
# print(old_name)
# print(type(old_name))

# 2. 规划备份文件的名字
# 1) 提取后缀: 查找文件名中的点-->名字和后缀分离-->最右边的点才是后缀-->字符串查找某个子串rfind()
index = old_name.rfind('.')

if index > 0:
    postfix = old_name[index:]
# print(index)
# 2) 组织新名字: 字符串切片
new_name = old_name[:index] + '_copy' + postfix
# print(new_name)

# 3. 备份文件写入数据
# 1) 打开 原文件 和 备份文件
old_file = open(old_name, 'rb')
new_file = open(new_name, 'wb')

# 2) 原文件读取,备份文件写入
# 如果不确定目标文件大小,为避免卡死(内存空间小于文件所占存储空间),
# 采用循环读取的方式读取和写入,读取结束终止循环
while True:
    con = old_file.read(1024)
    if len(con) == 0:
        break
    new_file.write(con)

old_file.close()
new_file.close()

