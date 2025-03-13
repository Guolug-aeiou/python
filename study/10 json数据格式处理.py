#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: project_Python
@File   : 10 json数据格式处理.py
@Author : guolu
@Date   : 2025/3/2 14:47
@Desc   : 
"""

# ========== 标准库导入 ==========
import json


# ========== 第三方库导入 ==========
# ========== 常量定义 ==========
def main():
    with open('jsonTest02.json', 'r', encoding='utf-8') as f:
        fJson = json.load(f)
        data_list = []
        for temp in fJson:
            data_list.append((temp.get("desc"),temp.get('username'),temp.get('password'),temp.get('expect')))
    print(data_list)
if __name__ == "__main__":
    main()
