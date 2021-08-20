import Read_data
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class Check_page:

    no_category_bar = []

    def Check_Features(self,market,driver,urllist,category_bar):

        try:
            driver.get(urllist)
            time.sleep(5)
            driver.find_element_by_xpath(category_bar)
            self.no_category_bar.append("1")
        except NoSuchElementException:
            self.no_category_bar.append(market)

