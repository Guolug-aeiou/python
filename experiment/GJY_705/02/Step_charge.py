#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: project_Python
@File   : Step_charge.py
@Author : guolu
@Date   : 2025/3/1 22:10
@Desc   : 阶梯记费
"""
def main():
    """主函数入口"""
    first_gear = 0
    second_gear = 0
    third_gear = 0
    # 用户输入
    count = float(input('请输入本月用电量:'))
    while not count >= 0:
        count = float(input('重新输入本月用电量:'))
    # 一档用电量
    first_gear = 180
    # 二档用电量
    if count - 180 > 0:
        second_gear = 400 - 180
    # 三档用电量
    if count - 400 > 0:
        third_gear = count - 400
    # 三档的值相加
    pay = (first_gear * 0.5) + (second_gear * 0.6) + (third_gear * 0.8)
    print(f'用电量:{count}\n费用:{pay} ')

if __name__ == "__main__":
    main()
