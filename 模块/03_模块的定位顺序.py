""""
python 解释器对模块位置的搜索顺序是:
    1. 当前目录
    2. shell变量 PYTHONPATH 下的每个目录
    3. 查看默认路径,Unix下一般为 /sur/local/lib/python/

模块搜索路径存储在system模块的sys.path变量中.
PYTHONPATH 由安装过程决定的默认目录

PS: 1.文件名不和已有模块名重复,否则导致模块功能无法使用
    2.使用 from 模块名 import 功能 的时候,功能名重复,调用最后定义或导入的功能

"""

# from my_module import random
# num = random.randint(1, 5)

from time import sleep


#  使用 from 模块名 import 功能 的时候,功能名重复,调用最后定义或导入的功能
# def sleep():
#     print(111)
#
#
# sleep(2)

# 拓展: 名字重复
# 问题: import 模块名 是否担心 功能名重复问题 -- 不需要
import time
print(time)  # <module 'time' (built-in)>

time = 1
# time.sleep(2)
print(time)  # 1

# 问题: 为什么变量也能覆盖模块?
# 答: 在Python中, 数据是通过 引用 传递的
#     上面第二个 time 的数据将原来 time 模块的数据 覆盖了
