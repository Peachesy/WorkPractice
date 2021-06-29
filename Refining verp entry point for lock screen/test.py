from selenium.webdriver import ActionChains

import Read_data
import selenium
from selenium import webdriver
import time

class Open_page:
    urls = Read_data.links

    driver = webdriver.Chrome()
    # driver.get("https://www.bing.com")

    cookies = driver.get_cookies()
    driver.delete_all_cookies()

    # lock screen page需要定位的两个元素
    setting_button = '//li[@id="dots_overflow_menu_container"]'
    news_button = '//ul[@class="overflow_menu"]/li[@id="news"]'

    # news verp page需要定位的三个元素
    search_box = '//div[@class="b_searchboxForm"]/input[@id="sb_form_q"]'
    input_para = '//div[@class="b_searchboxForm"]/input[@id="sb_form_q"]/@value'
    title = '//div[@class="newscontainer"]/div[@id="contentid"]/h2[@class=" feed-main-title"]'
    category_TopStories = '//li[@class="nsn-category-item rt_MaxClass selected expanded"]/div[@class="nsn-category-topitem-wrap"]/a[@class="next"]'

    # 检查lock screen page是否有entry point
    def Check_entry_point(self):
        for i in self.urls:
            self.driver.get(i)
            time.sleep(5)
            move = self.driver.find_element_by_xpath(self.setting_button)
            # 悬浮在setting按钮上使其他按钮出现
            ActionChains(self.driver).move_to_element(move).perform()
            self.driver.find_element_by_xpath(self.news_button).click()
            time.sleep(5)
            # 截图
            img_time = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
            save_img = self.driver.save_screenshot('./Screenshots' + img_time + '.png')
            # save_img = driver.get_screenshot_as_file('D:\\Applications\\PycharmProjects\\WorkPractice\\Refining verp entry point for lock screen\\Screenshots'+ market + img_time + '.png')
            print("截图为：", save_img)

            # 开始检查verp page
            # 1.search box里是否有query
            self.driver.find_element_by_xpath(self.search_box)
            search_query = self.driver.find_element_by_xpath(self.search_box).get_attribute('value')
            print("input元素的value值：",search_query)
            # 2.是否有top stories title
            self.driver.find_element_by_xpath(self.title)
            verp_title = self.driver.find_element_by_xpath(self.title).text
            print("Verp title is:", verp_title)
            # 3.category bar中是否选中top stories
            self.driver.find_element_by_xpath(self.category_TopStories)
        return

    # 检查news verp page中的“top stories”的三个条件
    def Check_verp_page(self):
        return


result=Open_page()
result.Check_entry_point()