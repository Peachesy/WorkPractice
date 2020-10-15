from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException

def OpenLinks(elePath):
    driver.find_element_by_xpath(elePath).click()
    time.sleep(5)
    driver.back()
    time.sleep(3)


URL = "https://www.bing.com/search?q=trump&setflight=NAMktPref&mkt=chr-cher-us"
keyword = "trump"
marketURL = str(URL).split('&')
print(marketURL)
newURL = "https://www.bing.com/search?q="+keyword+"&"+marketURL[1]+"&"+marketURL[2]
print(newURL)

driver = webdriver.Chrome()
driver.get(newURL)

time.sleep(2)
# driver.find_element_by_xpath('//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]').click()
OpenLinks(r'//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]')
time.sleep(2)

