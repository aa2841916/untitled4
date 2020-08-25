#coding=utf-8
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


import unittest

class Baidu_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True


    #百度搜索用例
    def test_baidu_search(self):
        '''

        百度搜索用例
        '''
        driver = self.driver


        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()


    # 百度设置用例
    def test_baidu_set(self):
        """

        百度设置用例
        """
        driver = self.driver
    # 进入搜索设置页
        driver.get(self.base_url + "/gaoji/preferences.html")

    # 设置每页搜索结果为 100 条
    #     m=driver.find_element_by_name("NR")
    #     m.find_element_by_xpath("//option[@value='100']").click()
    #     time.sleep(2)
    # 保存设置的信息
        driver.find_element_by_xpath("/html/body/form/div/input").click()
        time.sleep(2)
        # driver.switch_to_alert().accept()

    def test_baidu_set2(self):
        """

        百度下拉框用例
        """

        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element_by_link_text('搜索设置').click()
        time.sleep(3)
        se = driver.find_element_by_id('nr')
        Select(se).select_by_value('20')
        time.sleep(5)
        ops = Select(se).all_selected_options
        opq = Select(se).options
        for i,j in zip(ops,opq):
            print(i.text,j.text)
        driver.quit()

    def test_QQ_mail(self):
        """

        :return: qq邮箱iframe登陆用例
        """
        driver = self.driver
        driver.get('http://mail.qq.com')
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').send_keys('47779804')
        driver.find_element_by_id('p').send_keys('hdhd.@2841916')
        driver.find_element_by_css_selector("input[type='submit']").click()
        time.sleep(3)
        # driver.switch_to.frame('actionFrame')
        driver.find_element_by_css_selector('#composebtn').click()
        # driver.switch_to.default_content()
        driver.switch_to.frame('mainFrame')
        driver.find_element_by_css_selector('span#AttachFrame').send_keys('/Users/hudi/PycharmProjects/untitled4/thread_test_case/start_day3.py')
        time.sleep(5)




    def tearDown(self):

        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":  # 定义一个单元测试容器
    unittest.main()


    # testunit = unittest.TestSuite()
    # # 将测试用例加入到测试容器中
    # testunit.addTest(Baidu("test_baidu_search"))
    # testunit.addTest(Baidu("test_baidu_set"))
    # # 定义个报告存放路径，支持相对路径
    # filename = '/Users/hudi/automate_text/inner.html'
    # fp = open(filename, 'wb')
    # # 定义测试报告
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'百度搜索测试报告', description=u'用例执行情况:')
    # # 运行测试用例
    # runner.run(testunit)
