import time

import Read_data
import selenium
from selenium import webdriver
import Read_data
import Record_result
from Check_page import *


def main():
    op = Check_page()
    market_dict = Read_data.market_data
    print("市场列表：", market_dict)

    driver = webdriver.Chrome("E:\WebDrivers\chromedriver.exe")
    driver.maximize_window()

    # cookies = driver.get_cookies()
    driver.delete_all_cookies()

    # lock screen page需要定位的两个元素
    setting_button = '//li[@id="dots_overflow_menu_container"]'
    news_button = '//ul[@class="overflow_menu"]/li[@id="news"]'

    # news verp page需要定位的三个元素
    search_box = '//div[@class="b_searchboxForm"]/input[@id="sb_form_q"]'
    title = '//div[@class="newscontainer"]/div[@id="contentid"]/h2[@class=" feed-main-title"]'
    category_TopStories = '//li[@class="nsn-category-item rt_MaxClass selected expanded"]/div[@class="nsn-category-topitem-wrap"]/a[@class="next"]'

    # 遍历字典，开始执行Check_page方法
    for key, value in market_dict.items():

        # 处理cookie弹窗
        try:
            driver.find_element_by_id("bnp_container")
            time.sleep(3)
            driver.find_element_by_xpath(
                '//div[@class="bnp_flex_wrapper"]/button/a[contains(@href,"javascript: void(0)")]').click()
            time.sleep(5)
            print("检查cookie弹窗,发现弹窗")
            op.Check_Features(key, driver, value, setting_button, news_button, search_box, title, category_TopStories)
        except NoSuchElementException:
            print("检查cookie弹窗,没有发现弹窗")
            op.Check_Features(key, driver, value, setting_button, news_button, search_box, title, category_TopStories)

    print("没有entry point的市场：", op.no_entry_point)
    print("在search box中没有query的市场：", op.no_query_in_search_box)
    print("没有category bar的市场：", op.no_category_bar)
    print("有category bar的市场：", op.show_category_bar)
    print("没有top stories标题的市场：", op.no_top_stories_title)
    print("在category bar中没有选中top stories的市场：", op.did_not_select_top_stories)


if __name__ == "__main__":
    main()
