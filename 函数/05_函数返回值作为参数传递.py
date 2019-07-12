def func_result():
    return 10


# 多返回值默认返回的是元组
# 也可以直接返回列表,字典,集合
def func_results():
    # return [1, 2]
    # return {'tom', 20}
    # return {'name': 'Lily', 'age': 20}
    return 10, 20


def func_print(result):
    print(result)


result_of_func = func_result()
results_of_func = func_results()
print(type(results_of_func))
func_print(result_of_func)
func_print(results_of_func)