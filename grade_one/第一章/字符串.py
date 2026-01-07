# 单引号定义法
name = '字符串'

# 双引号定义法
name = "字符串"

# 三引号定义法
name = """
    字符串
"""

# 字符串嵌套
# 包含双引号
name = '"字符串"'
print(name)
# 包含单引号
name = "'字符串'"
print(name)
# 使用转移字符\接触引号效用
name =  "\"字符串\""
print(name)
name = '\'字符串\''
print(name)


# 字符串拼接
hello = "hello "
print(hello + name)
# 字面量拼接
print("hello " + "world")

# 字符串无法使用加号和整数进行拼接因此会报错
'''
number = 123456
print(hello + number + name)
'''

# 字符串格式化
number = 123456
message = "hello %s %d" % (name,number)
print(message)

number_1 = 12
name_1 = "Tom"
print(f"{name_1}的年龄为{number_1}")

number_2 = 5
print(f"{name_1} is older than his sister for {number_1 - number_2} years")