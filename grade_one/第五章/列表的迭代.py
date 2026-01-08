import random

arr = [1,2,3,4,'aaa',True]

# while循环
i = 0
while i < len(arr):
    global element
    element = arr[i]
    print(f"列表元素：{element}")
    i += 1

print(element)
print("打印完成")

# for循环
print("for循环")
for i in arr:
    print(i)

# 练习：取出偶数
# 注意：空列表不能直接使用下标，而应该是追加元素
a = []
for i in range(1,11):
    a.append(random.randint(i,i*100))

print(a)
print("得到奇数:")
i = 0
while i < len(a):
    if i % 2 != 0:
        print(i)
    i += 1

print("得到偶数:")
for i in a :
    if i % 2 == 0:
        print(i)