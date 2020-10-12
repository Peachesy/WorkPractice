import csv
from langdetect import detect
from langdetect import detect_langs
from selenium import webdriver
import pandas as pd
import time
from langdetect import DetectorFactory


# 检查不同market的UI和搜索、跳转功能，分为几块：
# 1.读取csv文件
# 2.根据文件中不同的浏览器内容使用不同的浏览器打开链接
# 3.检查搜索、跳转功能
# 4.获取当前页面的语言并填入表格中
# 5.清除浏览器数据并关闭浏览器

# MarketList = csv.reader(open(r'E:\WorkFiles\NewsAnswersForSeveralMarkets\MarketList.csv', 'r+'))
# Columns of MarketList.csv:
# True Market, Region, True Language, Current Language, Region tier, OS, Browser, SerpTestLink

FilePath = r'E:\WorkFiles\NewsAnswersForSeveralMarkets\MarketList.csv'
OperationSystem = []
BrowserList = []
LinkList = []

Datas = pd.read_csv(FilePath,usecols=['OS','Browser','SerpTestLink'])
print(Datas)

def FeatureTest():
    KeyWordsList = ['British royal family','coffee','travel','news today',"How's the weather in NYC?", 'restaurant near me','biden']

    EXP = "https://www.bing.com/search?q=trump&setflight=NAMktPref&mkt=chr-cher-us"
    driver = webdriver.Chrome()
    driver.get(EXP)
    driver.maximize_window()
    time.sleep(2)

    # Search
    for i in KeyWordsList:
        driver.find_element_by_class_name("b_searchbox").clear()
        driver.find_element_by_class_name("b_searchbox").send_keys(i)
        driver.find_element_by_class_name("b_searchboxSubmit").click()
        # Slide page to news answer
        div = driver.find_element_by_xpath('//div[@class="ans_nws"]')
        # 滑动滚动条到某个指定的元素
        js4 = "arguments[0].scrollIntoView();"
        # 将下拉滑动条滑动到当前div区域
        driver.execute_script(js4, div)
        # Page jump
        driver.find_element_by_class_name("itm_img").click()
        time.sleep(2)
        driver.back()
        # Turn page
        driver.find_element_by_class_name("btn next rounded bld").click()

def DetectLang():
    DetectorFactory.seed=0   # Make the result unique.
    ExpText = "¡Beijing le da la bienvenida!"

    print(detect(ExpText))        # Langs
    print(detect_langs(ExpText))  # Langs and its probability

# FeatureTest()
DetectLang()