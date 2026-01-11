from my_utils.file_util import *
from my_utils.str_util import *

s_re = str_reverse("Hello World")
print(s_re)

s_list = substr("Hello_World",2,4)
print(s_list)

filename = "../第七章/python.txt"
print_file_info(filename)
append_to_file(filename,"hello C/C++")
print_file_info(filename)