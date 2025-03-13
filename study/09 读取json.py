#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: project_Python
@File   : 09 读取json.py
@Author : guolu
@Date   : 2025/3/2 14:28
@Desc   : 读取json文件
"""
import json


# ========== 标准库导入 ==========
# ========== 第三方库导入 ==========
# ========== 常量定义 ==========
def main():
    """主函数入口"""
    with open('jsonTest.json','r',encoding='utf-8') as fJson:
        result = json.load(fJson)
        print(result)
        # 获取名称
        print(result.get('name'))
        # 获取年龄
        print(result.get('age'))
        # 获取地址
        print(result.get('address').get('city'))
if __name__ == "__main__":
    main()
