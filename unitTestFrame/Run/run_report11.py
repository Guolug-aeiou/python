import unittest

from config.HTMLTestRunnerCN import HTMLTestRunnerCN


def main():
    # 加载用例
    suite_loader = unittest.TestLoader().discover('../Test_Case/', 'test*.py')
    file_path = "../report/report-1.html"
    with open(file_path, 'wb') as f:
        HTMLTestRunnerCN(f,'report 标题','report 描述','测试人员').run(suite_loader)


if __name__ == '__main__':
    main()
