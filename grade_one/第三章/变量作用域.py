A = [5]
# 程序能够运行但是不符合规范
for i in range(5):
    print(i)

print(i)
# 解决方案将i变为全局变量
i = 0
for i in A:
    print(i)

print(i)