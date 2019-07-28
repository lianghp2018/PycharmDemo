# 需求:洗衣机, 功能: 能洗衣服
# 1.定义洗衣机类


class Washer:
    # 对象方法/实例方法
    def wash(self):  # self 是指调用该函数的对象
        print('洗衣服....')
        print(self)


# 2. 创建对象
haier = Washer()

# 3. 验证
print(haier)
# 使用功能
haier.wash()
# 打印self与haier对象得到的内存地址相同,
# 说明self是指调用该函数的对象
