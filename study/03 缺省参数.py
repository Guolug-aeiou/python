#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project: project_Python
@File   : 03 缺省参数.py
@Author : guolu
@Date   : 2025/2/28 21:07
@Desc   : 
"""


# ========== 标准库导入 ==========
# ========== 第三方库导入 ==========
# ========== 常量定义 ==========
def main(name='小白'):
    """主函数入口"""
    print(name)


if __name__ == "__main__":
    main() # 输出小白
    main('小黑') # 输出小黑
