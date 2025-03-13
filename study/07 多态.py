#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: project_Python
@File   : 07 多态.py
@Author : guolu
@Date   : 2025/3/1 16:50
@Desc   : 
"""


# ========== 标准库导入 ==========
# ========== 第三方库导入 ==========
# ========== 常量定义 ==========
class Animal:
    def run(self):
        print('动物在跑步')

class Dog(Animal):
    def shout(self):
        print('小狗在叫!')


class Bird(Animal):
    def fly(self):
        print('小鸟在飞!')

def main():
    """主函数入口"""



if __name__ == "__main__":
    main()
