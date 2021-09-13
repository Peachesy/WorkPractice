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
    double_checked_url = []
    entry_point = []

    def Check_Features(self,market,driver,urllist,category_bar, search_box_value_ele, top_stories_button_ele, title_ele1,title_ele2):

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


            # 判断title
            try:
                driver.find_element_by_xpath(title_ele1)
                self.title.append(driver.find_element_by_xpath(title_ele1).text)
            except NoSuchElementException:
                try:
                    driver.find_element_by_xpath(title_ele2)
                    self.title.append(driver.find_element_by_xpath(title_ele2).text)
                except NoSuchElementException:
                    self.title.append(-1)

            # 判断top stories button
            try:
                driver.find_element_by_xpath(top_stories_button_ele)
                self.top_stories_button.append(driver.find_element_by_xpath(top_stories_button_ele).text)
            except:
                self.top_stories_button.append(-1)


            driver.find_element_by_xpath(category_bar)
            self.no_category_bar.append("Have category bar")
        except NoSuchElementException:
            self.no_category_bar.append(market)

    def double_check(self,driver,market,urllist,double_check_link, setting_button, news_button): # 逻辑有问题！！！

        # Changed URL为http://stcav-867/ 的，需要重新拼接链接（http://stcav-867/?mkt=en-us&setlang=en-us）到main.py中进行二次验证，
        # 点击entry point中的news之后是否还继续跳转到HP，如果是，就在comment中追加信息“跳回HP，by design”，如果不是，就在comment中追加“跳回HP，是个bug”

        try:
            driver.get(urllist)
            time.sleep(5)

            move = driver.find_element_by_xpath(setting_button)
        except NoSuchElementException:
            self.entry_point.append("No entry point")
            print("double checked url:", double_check_link)
        else:
            try:
                # 悬浮在setting按钮上使其他按钮出现
                ActionChains(driver).move_to_element(move).perform()
                driver.find_element_by_xpath(news_button)
                time.sleep(2)
            except NoSuchElementException:
                self.entry_point.append("No news entry point")
            else:
                driver.find_element_by_xpath(news_button).click()
                time.sleep(5)
                self.double_checked_url.append(driver.current_url)
                print("double checked url:", double_check_link)




