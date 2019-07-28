# 需求:洗衣机, 功能: 能洗衣服
# 1.定义洗衣机类


class Washer:
    # 对象方法/实例方法
    def wash(self): # self 是指调用该函数的对象
        print('洗衣服....')
        print(self)

    def print_info(self):
        print(f'类内部获取外部添加的高度属性{self.height}')
        print(f'类内部获取外部添加的宽度属性{self.width}')


# 2. 创建对象
haier = Washer()

# 3. 添加属性 对象名.属性名 = 属性值
haier.height = 500
haier.width = 300

# 获取属性: 对象名.属性名
print(haier.height)
print(haier.width)

haier.print_info()