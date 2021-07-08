import Read_data
import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class Check_page:

    no_entry_point = []
    no_query_in_search_box = []
    no_category_bar = []
    show_category_bar = []
    no_top_stories_title = []
    did_not_select_top_stories = []

    def Check_Features(self,market,driver,urllist,setting_button,news_button,search_box,title,category_TopStories):

        try:
            driver.get(urllist)
            time.sleep(5)
            move = driver.find_element_by_xpath(setting_button)
        except NoSuchElementException:
            self.no_entry_point.append(market)
        else:
            try:
                # 悬浮在setting按钮上使其他按钮出现
                ActionChains(driver).move_to_element(move).perform()
                driver.find_element_by_xpath(news_button)
                time.sleep(2)
            except NoSuchElementException:
                # ！！！这里需要验证该market是否已经加入到列表中，如果已加入则不再追加
                self.no_entry_point.append(market)
            else:
                driver.find_element_by_xpath(news_button).click()
                time.sleep(5)
                # 截图
                img_time = time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime(time.time()))
                save_img = driver.save_screenshot('./Screenshots'+ market + img_time + '.png')
                # save_img = driver.get_screenshot_as_file(r'./Screenshots'+ market + img_time + '.png')
                print("截图为：",save_img)
                try:
                    # 开始检查verp page
                    # 1.search box里是否有query
                    driver.find_element_by_xpath(search_box)
                    search_query = driver.find_element_by_xpath(search_box).get_attribute('value')
                    if search_query == '':
                        self.no_query_in_search_box.append(market)
                    else:
                        print("input元素的value值：", search_query)
                    # 2.是否有top stories title
                    driver.find_element_by_xpath(title)
                except NoSuchElementException:
                    self.no_category_bar.append(market)
                    self.no_top_stories_title.append(market)
                else:
                    verp_title = driver.find_element_by_xpath(title).text
                    print("Verp title is:", verp_title)
                    try:
                        # 3.category bar中是否选中top stories---待修正
                        driver.find_element_by_xpath(category_TopStories)
                        ele = driver.find_element_by_xpath(category_TopStories).is_selected()
                        if ele == False:
                            self.did_not_select_top_stories.append(market)
                        self.show_category_bar.append(market)
                    except NoSuchElementException:
                        self.no_category_bar.append(market)

