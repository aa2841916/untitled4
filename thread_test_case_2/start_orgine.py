# -*- coding: <encoding name> -*- : # -*- coding: utf-8 -*-
import random
import time


import unittest

from BeautifulReport import BeautifulReport
from selenium import webdriver

from basic_data.basic_url import Basic_Data


class orgine_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = Basic_Data().orgine_basic_url
        self.driver.implicitly_wait(2000)
        self.verificationErrors = []
        self.accept_next_alert = True
        # self.driver.get(self.base_url + '/')
        # self.driver.find_element_by_id('account_id').send_keys('orgine')
        # self.driver.find_element_by_id('user_pwd1').send_keys('yuanqi2019')
        # self.driver.find_element_by_css_selector('div.ant-row>button').click()
        # time.sleep(1)



    def test_orgine_auto_powerrsp_up(self):
        """
        统一预约应用管理一键上传软件包
        """
        """登陆逻辑"""
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element_by_id('account_id').send_keys('orgine')
        driver.find_element_by_id('user_pwd1').send_keys('yuanqi2019')
        driver.find_element_by_css_selector('div.ant-row>button').click()
        time.sleep(1)
        # driver.find_element_by_xpath('//*[@id="left_items_box"]/div[2]/ul/li[6]').click()
        # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div/ul/li[10]/div/span').click()
        # driver.find_element_by_xpath('//*[@id="200535cd7c29424caecac506530ca999$Menu"]/li[10]/div').click()
        """进入统一预约上传页面"""
        driver.get(Basic_Data().orgine_manager_url)
        driver.get(Basic_Data().orgine_manager_upload_url)
        """上传软件包"""
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[7]/span/span/div[1]/span/input').send_keys('/Users/hudi/PycharmProjects/untitled4/thread_test_case/start_day3.py')
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[3]/div/div[1]/div/div/div/div/div/div/div/table/tbody/tr[2]/td[7]/span/span/div[1]/span/input').send_keys('/Users/hudi/PycharmProjects/untitled4/thread_test_case/start_day2.py')

        time.sleep(30)

    def test_orgine_auto_powerrsp_upload(self):
        """

        :return:统一预约应用部署一键上传软件包
        """
        """登陆逻辑"""
        driver = self.driver
        driver.get(self.base_url + '/')
        time.sleep(5)
        driver.find_element_by_id('account_id').send_keys('orgine')
        driver.find_element_by_id('user_pwd1').send_keys('yuanqi2019')
        driver.find_element_by_css_selector('div.ant-row>button').click()
        time.sleep(5)

        """进入应用管理应用部署页面"""
        driver.get(Basic_Data().orgine_deploy_url)
        time.sleep(10)
        soft_bag = 'orgine-cloud_v1.0.02.zip'
        """切割包名，赋予应用部署基础数据"""
        # soft_name = ((soft_bag.split('-'))[2].split('_'))[0]
        # soft_version = (((soft_bag.split('-'))[2]).split('_'))[1]

        """上传软件包"""
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/span/span/span/button').click()
        time.sleep(3)
        driver.find_element_by_css_selector('#soft_ware_package_name').send_keys('poweroc')
        driver.find_element_by_css_selector('#soft_ware_package_version').send_keys('v6.0.1' + '-' + str(random.randint(1,999)))
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[6]/div[2]/div/span/span/div[1]/span/input').send_keys('/Users/hudi/Downloads/最新包/最新包/' + soft_bag)
        time.sleep(2000)
        driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
        driver.save_screenshot('/Users/hudi/PycharmProjects/untitled4/report/powerrsp_upload.png')






    def tearDown(self):
        driver = self.driver
        driver.quit()


if __name__ == '__main__':
    unittest.main()


    # testunit.addTest(orgine("test_orgine"))
    #
    # # fp = open('/Users/hudi/automate_text/auto_test/result.html','wb')
    # '''
    #     filename -> 测试报告名称, 如果不指定默认文件名为report.html
    #     description -> 测试报告用例名称展示
    #     report_dir='.' -> 报告文件写入路径
    #     theme='theme_default' -> 报告主题样式 theme_default theme_cyan theme_candy theme_memories
    # '''
    # result = BeautifulReport(testunit)
    # result.report(filename='测试报告', description='测试deafult报告', report_dir='/Users/hudi/automate_text/auto_test', theme='theme_default')



