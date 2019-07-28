class Washer:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    # print打印对象默认输出地址值,该方法定义后将打印return的数据
    def __str__(self):
        return '这是海尔洗衣机'


haier = Washer(10, 20)
print(haier)
