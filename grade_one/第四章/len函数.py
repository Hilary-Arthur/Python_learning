a = [1,10,5,30,60,70,2,7,9,45,67,61]



print(len(a))

# 使用函数优化过程
# 手动实现len函数
def my_len(data):
    length = 0
    for i in a:
        length += 1
    return length
print(my_len(a))