import time

import Read_data
import selenium
from selenium import webdriver
import Read_data
from Check_page import *
from Data_process import *

# 检查点：
# 1.是否有category bar
# 2.search box, title, 选中的category bar中的文字，三者是否一致

def main():
    pop_window = []

    dp = Data_process()
    op = Check_page()
    market_dict = Read_data.market_data

    market = list(market_dict.keys())
    original_link = list(market_dict.values())

    driver = webdriver.Chrome("E:\WebDrivers\chromedriver.exe")
    driver.maximize_window()

    # cookies = driver.get_cookies()
    driver.delete_all_cookies()

    # 需要定位的元素
    # 标志有category bar的元素
    category_bar = '//a[@class="nsn-expand-btn"]'

    # 获取search box中的值 driver.find_element_by_tag_name('input').get_attribute('value'):
    search_box_value_ele = '//div[@class="b_searchboxForm"]/input[@class="b_searchbox b_softkey"]'

    # 获取category bar中top stories button的值，获取其text
    top_stories_button_ele = '//div[@class="nsn-category-topitem-wrap"]/a[@class="ntext"]'

    # 获取标题top stories的值，获取其text
    # Note!!!Not all h2 ele have a father ele span!!!
    title_ele1 = '//div[@class="content"]/span[@id="feed-top-stories-title-container"]/h2[@class=" feed-main-title "]'
    title_ele2 = '//div[@class="content"]/h2[@class=" feed-main-title "]'

    # double check 中需要定位的元素
    setting_button = '//li[@id="dots_overflow_menu_container"]'
    news_button = '//ul[@class="overflow_menu"]/li[@id="news"]'

    # 遍历字典，开始执行Check_page方法
    for key, value in market_dict.items(): # key为market-forms，value为需要访问的链接

        # print("key的值：", key)  # key是带form的market
        # 处理cookie弹窗
        try:
            driver.find_element_by_id("bnp_container")
            time.sleep(3)
            driver.find_element_by_xpath(
                '//div[@class="bnp_flex_wrapper"]/button/a[contains(@href,"javascript: void(0)")]').click()
            time.sleep(5)
            pop_window.append("检查cookie弹窗,发现弹窗,已处理")
            op.Check_Features(key, driver, value, category_bar, search_box_value_ele, top_stories_button_ele, title_ele1,title_ele2)
        except NoSuchElementException:
            pop_window.append("检查cookie弹窗,没有发现弹窗")
            op.Check_Features(key, driver, value, category_bar, search_box_value_ele, top_stories_button_ele, title_ele1,title_ele2)

    # 调用数据处理方法，找出需要二次验证的链接和市场
        dp.Check_double_check(key,value,op.ChangedURL)
        # print("需要二次验证的链接：",dp.double_check_link)

        # 处理cookie弹窗
        try:
            driver.find_element_by_id("bnp_container")
            time.sleep(3)
            driver.find_element_by_xpath(
                '//div[@class="bnp_flex_wrapper"]/button/a[contains(@href,"javascript: void(0)")]').click()
            time.sleep(5)
            pop_window.append("检查cookie弹窗,发现弹窗,已处理")
            # 二次验证
            op.double_check(driver, key, value, dp.double_check_link, setting_button, news_button)
        except NoSuchElementException:
            pop_window.append("检查cookie弹窗,没有发现弹窗")
            # 二次验证
            op.double_check(driver, key, value, dp.double_check_link, setting_button, news_button)


    # 二次验证结果
    dp.Double_check_result(key,op.double_checked_url)

    # 把数据保存到CSV
    # dp.Save_data_to_CSV(market,original_link, op.no_category_bar, op.ChangedURL, op.Search_box_value, op.title, op.top_stories_button, dp.comment)



    print("没有category bar的市场：", op.no_category_bar)
    print("变化后的URL列表：", op.ChangedURL)
    print("search box中的值：", op.Search_box_value)
    print("title的值：", op.title)
    print("top stories button的值：", op.top_stories_button)
    print("comment的值：", dp.comment)

    # 处理数据


    # 保存数据



if __name__ == "__main__":
    main()
