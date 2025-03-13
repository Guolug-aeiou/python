#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: project_Python
@File   : 12 模块和包.py
@Author : guolu
@Date   : 2025/3/2 15:55
@Desc   : 
"""
# 方式一
import random
# 调用方法
print(random.randint(0, 10))
# 方式二
from random import randint
# 调用方法
print(randint(10, 20))
