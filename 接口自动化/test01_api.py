import requests

res = requests.get('https://www.baidu.com')
requests.request('get', 'https://www.baidu.com')
# requests.post('https://www.baidu.com')
# requests.request('post','')
# requests.put('https://www.baidu.com')
# requests.request('put','')
# requests.delete('https://www.baidu.com')
# requests.request('delete','')
# # 功能与上面一致
# requests.request('get','https://www.baidu.com')
# 创建会话，token，cookie
requests.session()
# 提取值
print(res.text)  # 返回文本信息
print('=' * 100)
# print(res.json()) # 返回json格式
# print('='*100)
print(res.content)  # 放回字节内容
print('=' * 100)
print(res.status_code)  # 返回状态码
print('=' * 100)
print(res.reason)  # 返回状态信息
print('=' * 100)
print(res.cookies)  # 返回cookies
print('=' * 100)
print(res.encoding)  # 返回编码格式
print('=' * 100)
print(res.headers)  # 返回请求头
print('=' * 100)
print(res.request)  # 返回请求数据
