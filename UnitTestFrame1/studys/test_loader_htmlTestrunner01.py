# 1,导包
import unittest

from UnitTestFrame1.case.HTMLTestRunnerCN import HTMLTestRunnerCN


def main():
    #2, 实例化套件对象
    suite = unittest.defaultTestLoader.discover('../case', 'test*.py')
    fileN = 'D:/Application_object/project_Python/UnitTestFrame1/TestResults/report12.html'
    #3, 打开文件
    with open(fileN, 'wb') as f:
        #4, 写入内容
        runner = HTMLTestRunnerCN(f,'测试用例','这是用于学习HTMLTestRunner的使用','guolug')
        runner.run(suite)

if __name__ == '__main__':
    main()
