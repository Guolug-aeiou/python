#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: project_Python
@File   : 06 继承.py
@Author : guolu
@Date   : 2025/3/1 15:43
@Desc   : 继承语法的使用
"""


# ========== 标准库导入 ==========
# ========== 第三方库导入 ==========
# ========== 常量定义 ==========
class Animal:
    def test(self):
        print('Animal Class')


class Dog(Animal):
    def test2(self):
        print('Dog Class')

    pass


class Cat(Animal):
    def test2(self):
        print('Cat Class')

    pass


def main():
    """主函数入口"""
    animal = Animal()
    dog = Dog()
    cat = Cat()
    animal.test()
    dog.test()
    cat.test()
    dog.test2()
    cat.test2()


if __name__ == "__main__":
    main()
