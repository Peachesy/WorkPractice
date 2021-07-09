import time

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("E:\WebDrivers\chromedriver.exe")
driver.maximize_window()

cookies = driver.get_cookies()
driver.delete_all_cookies()

driver.get('http://stcav-867/?mkt=de-at&setlang=de-at')
time.sleep(5)
# print(driver.find_element_by_id("b_container"))
if driver.find_element_by_id("bnp_container"):
    time.sleep(2)
    driver.find_element_by_id("bnp_btn_accept").click()
time.sleep(2)
move = driver.find_element_by_xpath('//li[@id="dots_overflow_menu_container"]')
# 悬浮在setting按钮上使其他按钮出现
ActionChains(driver).move_to_element(move).perform()
driver.find_element_by_xpath('//ul[@class="overflow_menu"]/li[@id="news"]')
time.sleep(3)
driver.find_element_by_xpath('//ul[@class="overflow_menu"]/li[@id="news"]').click()
time.sleep(5)
