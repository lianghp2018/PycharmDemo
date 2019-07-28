# 需求1:把当前文件夹所有文件重命名
# 需求2: 删除字符串重命名：　1.构造条件的数据 2.书写if
import os

# 构造条件数据
flag = 1

# 1.获取所有文件:当前文件夹的目录列表
file_list = os.listdir()
print(file_list)

new_name = ''
# 2. 构造名字
for i in file_list:
    if flag == 1:
        new_name = 'python_' + i
        # 3. 重命名
        os.rename(i, new_name)
    elif flag == 2:
        # 删除前缀
        new_name = i[len('python_'):]
        os.rename(i, new_name)
