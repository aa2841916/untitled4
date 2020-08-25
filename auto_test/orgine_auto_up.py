import unittest

from BeautifulReport import BeautifulReport

"""设置读取目录，使用函数正则遍历提取指定前缀测试用例"""
lisaa = '/Users/hudi/PycharmProjects/untitled4/thread_test_case_2'


def creatsuit():
    testunit = unittest.TestSuite()

    discover = unittest.defaultTestLoader.discover(lisaa,'start*.py',top_level_dir=None)

    """遍历discover，取到start开头的py文件"""
    for test_unit in discover:
        """遍历start开头的文件，找到文件内test开头的测试类"""
        for test_case in test_unit:
            testunit.addTest(test_case)

    return testunit


alltestname = creatsuit()

result = BeautifulReport(alltestname)
result.report(filename='测试报告',description="测试defult报告",report_dir='/Users/hudi/PycharmProjects/untitled4/report',theme='theme_default')






