# 定义一个元组
a = (1,"hello",True)
b = ()
c = tuple()
print(a,b,c)
print(type(a))

# 定义单个元素的元组
d = ("world")
print(type(d))
e = ("world",)
print(type(e))

# 元组的嵌套
f = (a,b,c,e)
print(f)

# 下标索引取元组内容
i = 0
j = 2
print(f"元组f中第{i+1}个元组中的第{j+1}个元素是{f[i][j]}")