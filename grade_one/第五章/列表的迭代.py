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