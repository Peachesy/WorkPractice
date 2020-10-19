from selenium import webdriver
import time


driver = webdriver.Chrome()
# clear cookies
cookies = driver.get_cookies()
driver.get("https://www.bing.com/?mkt=en-us")
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath('//div[@id="idCont"]/span[@class="sw_mktsw"]/a[@class="sw_lang"]').click()
driver.find_element_by_xpath('//div[@id="idCont"]/span[@class="sw_mktsw"]/a[@class="sw_lang"]').click()


