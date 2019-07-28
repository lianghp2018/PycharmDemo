class Washer:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    # 删除对象时,解释器会默认调用_del_()方法
    def __del__(self):
        print(f'{self}对象已被删除')


haier = Washer(10, 20)