import json



def get_json_str(path)->dict:
    with open(path) as f:
        data = json.load(f)
    return data
def get_param():
    data = get_json_str('../data.json')
    param_data = []
    for i in data:
        param_data.append((data[i]['num1'],data[i]['num2'],data[i]['expect']))
    return param_data
