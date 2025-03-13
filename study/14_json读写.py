import json

param = {'id': 10, 'age': 24, 'name': '显示中文'}
with open('14_json读写study.json', 'w', encoding='UTF-8') as f:
    # 写
    # json.dump(param, f) #{"id": 10, "age": 24, "name": "\u663e\u793a\u4e2d\u6587"}
    json.dump(param, f, ensure_ascii=False) # {'id': 10, 'age': 24, 'name': '显示中文'}
with open('14_json读写study.json', encoding='UTF-8') as f:
    dict_json = json.load(f)
    print(dict_json)
    print(type(dict_json))
