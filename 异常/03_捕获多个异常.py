try:
    print(1/0)
# 捕获多个异常时,将异常类型放到except后,并以元组的方式进行书写
except (NameError, ZeroDivisionError):
    print('here have a error')
