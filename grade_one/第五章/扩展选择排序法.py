import random

ori_len = random.randint(1,10)
ori_list = list()

for i in range(ori_len):
    ori_list.append(random.randint(0,i*i))

print(f"初始化列表完成:{ori_list},准备进行选择排序:")
list_len = len(ori_list)

for i in range(0,list_len-1):
    for j in range(i+1,list_len):
        if ori_list[i] > ori_list[j]:
            tmp = ori_list[i]
            ori_list[i] = ori_list[j]
            ori_list[j] = tmp

print(f"选择排序完成，结果为{ori_list}")