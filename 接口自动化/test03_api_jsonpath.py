
import jsonpath
import requests
from dotenv import load_dotenv
import os

load_dotenv('../config/Python.env')


class TestApi:

    def test1(self, url, param):
        self.url = url
        self.param = param
        # requests.get(url=url,params=param,**kwargs) # **kwargs接收请求头
        return requests.get(url=self.url, params=self.param)

    def test2(self):
        result = self.test1("https://api.weixin.qq.com/cgi-bin/token", {
            "grant_type": "client_credential",
            "appid": os.getenv("APPWEICHAR_ID1"),
            "secret": os.getenv("APPWEICHAR_KEY1")
        }).json()
        # 使用jsonpath表达式将token截取出来
        print(result)
        access_token = jsonpath.jsonpath(result, '$.access_token')
        print(access_token)

        datas2 = {
            "access_token": access_token
        }
        request2 = requests.get(url="https://api.weixin.qq.com/cgi-bin/tags/get", params=datas2)
        print(request2.text)
        print(request2.json())


if __name__ == '__main__':
    testapi = TestApi()
    testapi.test2()
