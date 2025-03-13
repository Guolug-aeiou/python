#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: project_Python
@File   : 01 不定长参数.py
@Author : guolu
@Date   : 2025/2/28 20:53
@Desc   : 练习不定长参数的练习
"""


# ========== 标准库导入 ==========
# ========== 第三方库导入 ==========
# ========== 常量定义 ==========
def main(*args,**kwargs):
    sum1,sum2 = 0,0
    """主函数入口"""
    for tmep in args:
        sum1 += tmep
    for temp in kwargs.values():
        sum2 +=temp
    return sum1,sum2

if __name__ == "__main__":
    print(main(1, 2, 3, 4, 5, 6, 7))  # 不定长参数的传入
    print(main(*[1, 2, 3, 4, 5]))  # 使用 * 进行拆包后传入
    print(main(**{'a': 1, 'b': 2, 'c': 3, 'd': 4}))  # 字典的value做为参数传入
    maxs = lambda number1, number2: number1 if number1 > number2 else number2
    print(maxs(10, 20))  # 20
    print(maxs(30, 20))  # 30