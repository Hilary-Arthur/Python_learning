# 九九乘法表
for i in range(1,10):
    for j in range(1,10):
        if j <= i:
            print(f"{i}*{j}={i*j} ",end="")
        else :
            print("")
            break
print()
# 方法2
for i in range(1,10):
    for j in range(1,10):
        if i <= j :
            print(f"{i}*{j}={i * j} ", end="")
        if j == 9 :
            print("")