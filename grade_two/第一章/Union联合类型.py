from typing import Union

my_list: list[Union[int,str]] = [1,2,3,True,"a","b"]

for i in my_list:
    print(type(i))