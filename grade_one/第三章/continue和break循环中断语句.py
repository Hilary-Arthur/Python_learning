for i in range(1,6):
    if i == 3 :
        continue
    print(i)

for i in range(1,6):
    if i == 3 :
        break
    print(i)

# break的嵌套循环
for i in range(1,10):
    for j in range(1,10):
        if i < j :
            break
        print(f"{i}*{j}={i*j} ",end="")
    print()

# continue语句循环
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        continue
        print("语句3")
    print("语句4")
