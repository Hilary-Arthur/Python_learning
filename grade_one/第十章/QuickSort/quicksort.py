# 传入的data是一个列表
import random
def partition(low,high,data):
    key = data[low]
    while (low<high):
        while(low < high and data[high] >= key):
            high -= 1
        data[low] = data[high]
        while (low < high and data[low] <= key):
            low += 1
        data[high] = data[low]
    data[low] = key
    return low


def quickSort(low,high,data):
    if (low < high):
        mid = partition(low,high,data)
        quickSort(low,mid-1,data)
        quickSort(mid+1,high,data)

if __name__ == '__main__':
    test_list = list()
    list_len = random.randint(1,100)
    for i in range(list_len):
        test_list.append(random.randint(1,1000))
    quickSort(0,list_len-1,test_list)
    for i in test_list:
        print(i,end=" ")