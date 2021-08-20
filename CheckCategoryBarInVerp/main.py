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

    # 需要定位的元素
    category_bar = '//a[@class="nsn-expand-btn"]'

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
            op.Check_Features(key, driver, value, category_bar)
        except NoSuchElementException:
            print("检查cookie弹窗,没有发现弹窗")
            op.Check_Features(key, driver, value, category_bar)


    print("没有category bar的市场：", op.no_category_bar)



if __name__ == "__main__":
    main()
