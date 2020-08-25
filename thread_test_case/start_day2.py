import unittest

from selenium import webdriver


class orgine_test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.basic_url = 'http://www.baidu.com'





    def tearDown(self):

        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
