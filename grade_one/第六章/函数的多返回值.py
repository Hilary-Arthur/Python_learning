def return_num():
    return 1
    return 2

result = return_num()
print(result)

def return_num_1():
    return 1,2

result_1,result_2 = return_num_1()

print(f"函数返回的第一个值为{result_1},第二个值为{result_2}")