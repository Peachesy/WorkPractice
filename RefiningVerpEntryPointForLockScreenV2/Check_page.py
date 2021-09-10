import Read_data
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class Check_page:

    no_category_bar = []
    ChangedURL = []
    Search_box_value = []
    title = []
    top_stories_button = []

    def Check_Features(self,market,driver,urllist,category_bar, search_box_value_ele, top_stories_button_ele, title_ele):

        try:
            driver.get(urllist)
            time.sleep(5)

            # 记录下当前页面的URL
            self.ChangedURL.append(driver.current_url)

            # 判断当前页面搜索框中是否有值
            if driver.find_element_by_tag_name('input').get_attribute('value') :
                self.Search_box_value.append(driver.find_element_by_tag_name('input').get_attribute('value'))
                # print("搜索框中有值！值为：", driver.find_element_by_tag_name('input').get_attribute('value'))
            else:
                self.Search_box_value.append(-1)

            # # 判断title
            # if driver.find_element_by_xpath(title_ele):
            #     self.title.append(driver.find_element_by_xpath(title_ele).text)
            #     # print("title的值为：", driver.find_element_by_xpath(title_ele).text)
            # else:
            #     self.title.append(-1)
            #
            # # 判断top stories button
            # if driver.find_element_by_xpath(top_stories_button_ele):
            #     self.top_stories_button.append(driver.find_element_by_xpath(top_stories_button_ele).text)
            #     # print("top stories button的值为：", driver.find_element_by_xpath(top_stories_button_ele).text)
            # else:
            #     self.top_stories_button.append(-1)

            # 判断title
            try:
                driver.find_element_by_xpath(title_ele)
                self.title.append(driver.find_element_by_xpath(title_ele).text)
            except NoSuchElementException:
                self.title.append(-1)

            # 判断top stories button
            try:
                driver.find_element_by_xpath(top_stories_button_ele)
                self.top_stories_button.append(driver.find_element_by_xpath(top_stories_button_ele).text)
            except:
                self.top_stories_button.append(-1)


            driver.find_element_by_xpath(category_bar)
            self.no_category_bar.append("1")
        except NoSuchElementException:
            self.no_category_bar.append(market)

