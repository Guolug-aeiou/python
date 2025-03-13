#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: project_Python
@File   : 11 json的写入.py
@Author : guolu
@Date   : 2025/3/2 15:01
@Desc   : json的写入操作练习
"""
import json


# ========== 标准库导入 ==========
# ========== 第三方库导入 ==========
# ========== 常量定义 ==========
def main():
    dataList = [
        {
            "desc": "正确的用户名密码",
            "username": "admin",
            "password": "123456",
            "expect": "登录成功"
        },
        {
            "desc": "错误的用户名密码",
            "username": "admin",
            "password": "123123",
            "expect": "登录失败"
        }
    ]
    with open('jsonTest03.json','w',encoding='utf-8') as f:
        json.dump(dataList,f,ensure_ascii=False,indent=2)
        # ensure_ascii 是否显示 ASCII 码的方式
        # indent 缩进值
if __name__ == "__main__":
    main()
