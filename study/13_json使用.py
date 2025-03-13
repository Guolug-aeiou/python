import json

data_str = {
    'id': 1,
    'test': 2,
    'test1': 3
}
json_str = '{"id":1,"test":2,"test1":3}'
# 字典转 json字符串
json_s = json.dumps(data_str)
print(json_str)
print(type(json_str))
# json 字符串转字典
data_dict = json.loads(json_str)
print(data_dict)
print(type(data_dict))
