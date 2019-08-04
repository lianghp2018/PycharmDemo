"""
如果一个模块文件中有__all__变量,当使用from xxx import * 导入时,只能导入__all__列表中的元素(功能)
"""

"""
模块内代码:
# 使用 from xxx import * 只能导入 testA 功能,无法导入testB 
__all__ = ['testA']

def testA():
    pass
    

def testB():
    pass
        
"""