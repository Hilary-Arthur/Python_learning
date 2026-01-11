# time时间模块的导入
# import time

# 暂停五秒钟
# print(1)
# time.sleep(5) # 通过.就可以使用模块内部的全部功能
# print(2)

# from 模块名 import 功能名 [as 别名]
# 只导入sleep()功能
# from time import sleep as s
# print(1)
# s(5)
# print(2)

# *导入模块中的全部功能
# from time import *
# print(1)
# sleep(2)
# print(2)

# 使用as给特定功能加上别名
# import time as t
# print(1)
# t.sleep(2)
# print(2)

# 自定义模块
# from 自定义模块 import add
# from 自定义模块_2 import add
# # 此处调用的是后一个
# num = add(1,2)
#
# print(f"自定义模块中加法函数的结果为{num}")

# __main__变量
from  自定义模块 import add

# __all__变量,此时只能导入all内部的模块
from 自定义模块 import *
add(1,2)

