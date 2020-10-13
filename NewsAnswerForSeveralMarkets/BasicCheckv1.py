import csv
from langdetect import detect
from langdetect import detect_langs
from selenium import webdriver
import pandas as pd
import time
from langdetect import DetectorFactory
import random


# 检查不同market的UI和搜索、跳转功能，分为几块：
# 1.读取csv文件
# 2.根据文件中不同的浏览器内容使用不同的浏览器打开链接
# 3.检查搜索、跳转功能
# 4.获取当前页面的语言并填入表格中
# 5.清除浏览器数据并关闭浏览器

# MarketList = csv.reader(open(r'E:\WorkFiles\NewsAnswersForSeveralMarkets\MarketList.csv', 'r+'))
# Columns of MarketList.csv:
# True Market, Region, True Language, Current Language, Region tier, OS, Browser, SerpTestLink
# Datas = pd.read_csv(FilePath,usecols=['OS','Browser','SerpTestLink'])
# print(Datas)


FilePath = r'E:\WorkFiles\NewsAnswersForSeveralMarkets\MarketList.csv'
with open(FilePath,'r+') as f:
    reader = csv.DictReader(f)
    print(reader)
    LinkList = [row['SerpTestLink'] for row in reader]
# print(LinkList)


def FeatureTest(links):
    KeyWordsList = ['British royal family','coffee','travel','news today',"How's the weather in NYC?", 'restaurant near me','biden','Google','local news','facebook','trump','election2020']
    length = len(KeyWordsList)

    driver = webdriver.Chrome()
    for i in links[1:2]:
        driver.get(i)
        driver.maximize_window()
        time.sleep(2)
        # [random.randint(0, length) for _in range(3)]  # produce 3 random integers one time
        # Search
        print(i)
        for i in range(3):
            print(KeyWordsList[i])
            driver.find_element_by_class_name("b_searchbox").clear()
            driver.find_element_by_class_name("b_searchbox").send_keys(KeyWordsList[i])
            driver.find_element_by_class_name("b_searchboxSubmit").click()

            # Slide page to news answer
            div = driver.find_element_by_xpath('//div[@class="ans_nws"]')
            # Slide to specific place
            js4 = "arguments[0].scrollIntoView();"
            # Slide to previous div area
            driver.execute_script(js4, div)

            # Page jump
            # 3 kinds news answer:
            # 1.smab na_overlay_softopt
            # 2.
            # 3.
            div.find_element_by_xpath('//div[@class="smab na_overlay_softopt"]/./././div[@class="b_overlay"]').click()
            time.sleep(5)
            driver.back()
            time.sleep(2)
            # Turn page
            driver.find_element_by_xpath('//div[@class="b_overlay"]/div[@class="btn next rounded bld"]').click()
# def DetectLang():
#     DetectorFactory.seed=0   # Make the result unique.
#     ExpText = "¡Beijing le da la bienvenida!"
#
#     print(detect(ExpText))        # Langs
#     print(detect_langs(ExpText))  # Langs and its probability

FeatureTest(LinkList)
