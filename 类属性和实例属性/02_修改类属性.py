# 定义类属性
class Dog(object):
    tooth = 10



# 创建对象
wangcai = Dog()
xiaohei = Dog()

# 修改类属性
Dog.tooth = 20

# 此处相当与创建了一个实例属性
wangcai.tooth = 12

# 访问类型属性
print(Dog.tooth)  # 20
print(wangcai.tooth)  # 12
print(xiaohei.tooth)  # 20