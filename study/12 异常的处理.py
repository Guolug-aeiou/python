#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: project_Python
@File   : 12 异常的处理.py
@Author : guolu
@Date   : 2025/3/2 15:32
@Desc   : 异常的处理
"""


# ========== 标准库导入 ==========
# ========== 第三方库导入 ==========
# ========== 常量定义 ==========
def main():
    try:
        print('这里是有可能发生异常的代码')
        num = int(input('请输入整数:'))
        num = 10 / num
        print(num)
    except Exception as e:
        print(f'异常的说明: {e}')
    else:
        print('没有发生异常我会执行!')
    finally:
        print('无论有没有发生异常都会执行!')
if __name__ == "__main__":
    main()
