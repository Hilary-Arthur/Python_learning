# json
import json

data = [{"name":"汤姆","age":19},{"name":"Anny","age":18}]
# 将python数据转化为json数据,如果希望打印中文：则把asc打印关闭
data = json.dumps(data,ensure_ascii=False)
print(f"json的本质上是一个:{type(data)}\n存储的数据是{data}")
# 将json数据转化为python数据
data = json.loads(data)
print(type(data))

data_1 = '[{"name": "汤姆", "age": 19}, {"name": "Anny", "age": 18}]'
data_1 = json.loads(data_1)
print(data_1,type(data_1))

data_2 = '{"name": "汤姆", "age": 19}'
data_2 = json.loads(data_2)
print(data_2,type(data_2))