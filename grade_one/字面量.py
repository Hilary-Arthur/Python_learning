import string
from cmath import sqrt

# 数字Number
a = 1
b = sqrt(-1)
c = 3.14E3
d = True

print(a)
print(b)
print(c)
print(d)

# 字符串String,字符串拼接,字符串格式化
e = "hello "
f = "world {}"
g = "Python"
h = "world %s" % g
print(e + f + "\n" + e + g)
print(f.format(g))
print(h)