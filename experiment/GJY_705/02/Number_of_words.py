#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: project_Python
@File   : Number_of_words.py
@Author : guolu
@Date   : 2025/3/1 23:02
@Desc   : 统计单词数
"""
from itertools import count


def main():
    """主函数入口"""
    sWord = input('请输入一段你喜欢的英文:')
    sList = sWord.split(' ')
    countList = []
    count = 0
    # 获取空元素的下标
    for temp in sList:
        if temp in ['',',','.','/','\\','=','-','!','~','?']:
            countList.append(count)
        count +=1
    # 反转列表后根据下标删除空元素
    countList.reverse()
    for temp in countList:
        sList.pop(int(temp))
    print(len(sList))
if __name__ == "__main__":
    main()
