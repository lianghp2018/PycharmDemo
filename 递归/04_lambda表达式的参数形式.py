# 无参数形式
fn1 = lambda: 100
print(fn1())

# 一个参数
fn2 = lambda a: a
print(fn2('Hello World'))

# 默认参数
fn3 = lambda a, b, c=100: a + b + c
print(fn3(10, 20))
print(fn3(100, 200, 300))

# 可变参数: *args 返回值为元组
fn4 = lambda *args: args
print(fn4(100, 200, 'Hello'))
print(fn4(10))

# 可变参数: **kwargs  返回值为字典
fn5 = lambda **kwargs: kwargs
print(type(fn5(time='100', name=200, age=300)))


