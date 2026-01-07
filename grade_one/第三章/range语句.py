A = [1,2,3,4,5]
for i in range(5) :
    print(i)

for i in range(5,10):
    print(i)

for i in range(5,20,2):
    print(i)

# 练习：获取偶数
num = 0
aim = 1000
for i in range(1,aim+1):
    if i % 2 == 0 :
        num += 1

print(f"1到{aim}之间的偶数数为:{num}")