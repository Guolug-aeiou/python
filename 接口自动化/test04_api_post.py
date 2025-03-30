import random
import jsonpath
import requests
import responses
from dotenv import load_dotenv
import os


load_dotenv('../config/Python.env')


class TestApi:
    url = "https://api.weixin.qq.com/cgi-bin/token"
    param = {
        "grant_type": "client_credential",
        "appid": os.getenv("APPWEICHAR_ID1"),
        "secret": os.getenv("APPWEICHAR_KEY1")
    }

    def get_token(self):
        result = requests.get(url=self.url, params=self.param).json()
        return jsonpath.jsonpath(result, '$.access_token')


if __name__ == '__main__':
    testapi = TestApi()
    url = "https://api.weixin.qq.com/cgi-bin/tags/create?access_token=" + testapi.get_token()[0]
    datas = {"tag": {"name": "广东" + str(random.randint(1, 10))}}
    res_post = requests.post(url=url, json=datas)
    print(res_post.json())
