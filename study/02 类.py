#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: project_Python
@File   : 02 类.py
@Author : guolu
@Date   : 2025/2/28 22:20
@Desc   : 
"""


# ========== 标准库导入 ==========
# ========== 第三方库导入 ==========
# ========== 常量定义 ==========
class Cat:
    name = '猫'
    age = 20
    sex = True
    def eat(self):
        print('小猫吃鱼!')

    def drink(self):
        print('小猫摇尾巴!')


def main():
    cat = Cat()
    cat.eat()
    cat.drink()
    cat.age = 20  # 给对象添加属性
    print(cat.age)
    print(cat.name) # 调用对象属性


if __name__ == "__main__":
    main()
