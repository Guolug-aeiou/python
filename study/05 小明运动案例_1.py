#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: project_Python
@File   : 05 小明运动案例_1.py
@Author : guolu
@Date   : 2025/3/1 14:24
@Desc   : 需求：
            1.小明体重75.0公斤
            2.小明每次跑步会减 0.5公斤
            3.小明每次吃东西体重增加 1 公斤
"""
from time import sleep


# ========== 标准库导入 ==========
# ========== 第三方库导入 ==========
# ========== 常量定义 ==========
class Person:
    def __init__(self):
        self.name = '小明'
        self.weight = 75.0
    def run(self):
        self.weight -= 0.5
        print(f'{self.name}开始跑步',end='')
        sleep(1)
        print('.',end='')
        sleep(1)
        print('.',end='')
        sleep(1)
        print('.',end='')
        sleep(1)
        print('.',end='')
        sleep(1)
        print('.')
        print(f'{self.name}跑步结束!')
    def eat(self):
        self.weight += 1.0
        print(f'{self.name}开始吃东西',end='')
        sleep(1)
        print('.',end='')
        sleep(1)
        print('.',end='')
        sleep(1)
        print('.',end='')
        sleep(1)
        print('.',end='')
        sleep(1)
        print('.')
        print(f'{self.name}吃东西结束!')
    def __str__(self):
        return f'{self.name}的体重是{self.weight}kg'
def main():
    person = Person()
    person.run()
    print(person)
    person.eat()
    print(person)


if __name__ == "__main__":
    main()
