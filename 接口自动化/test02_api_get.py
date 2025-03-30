import os

import requests
from dotenv import load_dotenv

load_dotenv('../config/Python.env')


class TestApi:
    url = "https://api.weixin.qq.com/cgi-bin/token"
    datas = {
        "grant_type": "client_credential",
        "appid": os.getenv("APPWEICHAR_ID1"),
        "secret": os.getenv("APPWEICHAR_KEY1")
    }
    # requests.get(url=url,params=param,**kwargs) # **kwargs接收请求头
    request = requests.get(url=url, params=datas)
    print(request.text)
    print(request.json())

