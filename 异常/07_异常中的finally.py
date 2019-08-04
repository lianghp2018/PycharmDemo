try:
    print(1)
except Exception as result:
    print(result)
else:
    print('there are no error!')
# finally 是否有异常都要执行的代码块 如关闭文件
finally:
    print("this's fine")
