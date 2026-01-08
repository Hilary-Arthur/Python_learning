a = (1,"hello",True)
b = ()
c = tuple()
e = ("world",)
f = (a,b,c,e,c,b,a)
# index()查找操作
index = f.index(c)
print(f)
print(index)

# count()统计
count = f.count(b)
print(count)

# len()获取长度
length = len(f)
print(length)

# 元组的遍历
print("while遍历:")
i = 0
while i < length:
    if i == length - 1:
        print(f[i])
        break
    print(f[i], end=" ")
    i += 1

print("for循环遍历:")
for i in f:
    print(i)