#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: project_Python
@File   : 01 不定长参数.py
@Author : guolu
@Date   : 2025/2/28 20:53
@Desc   : 练习不定长参数的练习
"""
import random
from turtledemo.forest import doit1


# ========== 标准库导入 ==========
# ========== 第三方库导入 ==========
# ========== 常量定义 ==========
def main(*args, **kwargs):
    sum1, sum2 = 0, 0
    """主函数入口"""
    for tmep in args:
        sum1 += tmep
    for temp in kwargs.values():
        sum2 += temp
    return sum1, sum2


def test():
    list1 = [1]
    # 添加操作
    # 默认添加值
    list1.append('add')  # list1 = [1,'add']
    # 在指定位置插入
    list1.insert(0, 'insert')  # list1 = ['insert',1,'add']
    # 添加可迭代值
    list1.extend([1, 2, 3])  # list1 = ['insert',1,'add',1,2,3]
    # 删除操作
    # 从头开始检索某个值后删除
    list1.remove(1)  # list1 = ['insert','add',1,2,3]
    # 删除末尾或某个下标的值
    list1.pop()  # list1 = ['insert','add',1,2]
    list1.pop(0)  # list1 = ['add',1,2]
    # 清空列表
    list1.clear()  # list1 = []
    # 查找和排序
    list2 = [1, 2, 3, 4, 5, 6, 7, 1]
    list3 = [2, 3, 4, 5, 9, 1, 21, 2, 12, 3, 4]
    # 返回下标
    print(list2.index(3))  # 2
    print(list2.index(1, 1))  # 7
    # 统计某个值出现次数
    print(list2.count(2))  # 2
    # 原地排序
    list3.sort()  # 正序
    print(list3)
    list3.sort(reverse=True)  # 倒序
    print(list3)


def list_apply():
    """
    1 到 16 抽取蓝色
    1 到 33 抽取红色
    6 个红，1个蓝
    """
    double_color_ball = []
    count = 0
    while True:
        double_color_ball.append(random.sample(range(1, 34), 6))
        for i in range(0, 1):
            double_color_ball[count].append(random.randint(1, 17))
        count += 1
        if count > 6:
            break
    for i in double_color_ball:
        for j in i[0:5]:
            print(f'\033[031m{j}\t',end='')
        print(f'\033[034m{i[6]}')


    def functions():
        pass
if __name__ == "__main__":
    # print(main(1, 2, 3, 4, 5, 6, 7))  # 不定长参数的传入
    # print(main(*[1, 2, 3, 4, 5]))  # 使用 * 进行拆包后传入
    # print(main(**{'a': 1, 'b': 2, 'c': 3, 'd': 4}))  # 字典的value做为参数传入
    # maxs = lambda number1, number2: number1 if number1 > number2 else number2
    # print(maxs(10, 20))  # 20
    # print(maxs(30, 20))  # 30
    # test()
    list_apply()
