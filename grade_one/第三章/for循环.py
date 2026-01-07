# 区分有序数组{}和无序数组[]
a = [1,10,5,30,60,70,2,7,9,45,67,61]
aim = 67
index = 0
# 练习，确定数字67的位置
for i in a:
    print("数据 %d : %d" % (index+1,i))
    index += 1
    if i == aim :
        print("%d 位置为 %d" % (aim,index))
        break

# 统计字符l的数量
letter = "hello world"
times = 0
for i in letter:
    if i == 'l':
        times += 1

print("'l'的数量为%d" % times)

#