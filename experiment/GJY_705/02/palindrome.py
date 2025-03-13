#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: project_Python
@File   : palindrome.py
@Author : guolu
@Date   : 2025/3/1 21:30
@Desc   : 判断回文数作业
"""
# ========== 标准库导入 ==========
# ========== 第三方库导入 ==========
# ========== 常量定义 ==========
def main():
    """主函数入口"""
    sNumber = input('请输入4位数:')
    # one = int(number % 10)
    # ten = int(number % 100 / 10)
    # hundred = int(number % 1000 / 100)
    # thousand = int(number % 10000 / 1000)
    # if one == thousand and ten == hundred:
    #     print(f'{number}是回文数!')
    # else:
    #     print(f'{number}不是回文数!')
    if sNumber[0] == sNumber[3] and sNumber[1] == sNumber[2]:
        print(f'{sNumber}是回文数!')
    else:
        print(f'{sNumber}不是回文数!')
if __name__ == "__main__":
    main()
