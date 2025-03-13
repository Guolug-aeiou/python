#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: project_Python
@File   : 04 魔法方法.py
@Author : guolu
@Date   : 2025/3/1 14:03
@Desc   : 
"""

# ========== 标准库导入 ==========
# ========== 第三方库导入 ==========
# ========== 常量定义 ==========
class Cat:
    # def __init__(self):
    #     self.name = '猫'
    #     self.age = 20
    #     self.sex = True
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __str__(self):
        return f'小猫的名字叫{self.name},年龄是{self.age},性别是{self.sex}'
    def eat(self):
        print('小猫吃鱼!')

    def drink(self):
        print('小猫摇尾巴!')


def main():
    cat = Cat('黑猫',10,False)
    cat.eat()
    cat.drink()
    print(cat.age)
    print(cat.name) # 调用对象属性
    print(cat.sex)
    print(cat)

if __name__ == "__main__":
    main()
