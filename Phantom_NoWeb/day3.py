from selenium import webdriver

opj = webdriver.ChromeOptions()


opj.setter()

driver = webdriver.Chrome(options=opj)


driver.get('http://www.baidu.com')

print(driver.title)

driver.close()




