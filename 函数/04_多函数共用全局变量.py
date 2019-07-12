# 全局变量
glo_num = 0


def func1():
    # 修改glo_num
    global glo_num
    glo_num = 100
    print(glo_num)


def func2():
    # 修改glo_num
    global glo_num
    glo_num = 200
    print(glo_num)


print(glo_num)
func2()
func1()
func2()
print(glo_num)