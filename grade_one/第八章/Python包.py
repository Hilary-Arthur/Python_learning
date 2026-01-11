# 创建一个包
# 导入自定义包中的模块，并使用
# import Python_package.my_module
# import Python_package.my_module_2
#
# Python_package.my_module.info_print1()
# Python_package.my_module_2.info_print2()

# from Python_package import my_module_2,my_module
# my_module_2.info_print2()
# my_module.info_print1()

from Python_package.my_module import info_print1
from Python_package.my_module_2 import info_print2
info_print1()
info_print2()

# 通过__all__变量,控制import*,此时只能导入my_module
from Python_package import *
my_module.info_print1()