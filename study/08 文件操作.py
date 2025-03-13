#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: project_Python
@File   : 08 文件操作.py
@Author : guolu
@Date   : 2025/3/1 18:38
@Desc   : 操作文件练习
"""


# ========== 标准库导入 ==========
# ========== 第三方库导入 ==========
# ========== 常量定义 ==========
def main():
    # 打开一个文件
    files1 = open('touch.txt', 'w', encoding='utf-8')
    files2 = open('touch1.txt', 'a', encoding='utf-8')
    files3 = open('touch1.txt', 'r', encoding='utf-8')
    # 操作文件
    if files1.writable() and files2.writable():
        files1.write('test1\n')
        files2.write('test2\n')
    if files3.readable():
        print(files3.read(12))
        print('-'*20)
        print(files3.read(12))
    # 关闭文件
    files1.close()
    files2.close()
    with open('touch.txt', 'w', encoding='utf-8') as f:
        if f.writable():
            f.write('test100')
if __name__ == "__main__":
    main()
