import csv
from selenium import webdriver
import time
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

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

# Create a csv file to record data
# Structure: Link,Keyword1,Result,Keyword2,Result,Keyword3,Result,Keyword4,Result

# Feature for opening links
def OpenLinks(elePath):
    # Slide to election news position
    js4 = "arguments[0].scrollIntoView();"
    driver.execute_script(js4, driver.find_element_by_xpath(elePath))
    time.sleep(3)
    # click
    driver.find_element_by_xpath(elePath).click()
    time.sleep(5)
    driver.back()
    time.sleep(3)
    # Click news verp
    # driver.find_element_by_xpath("//*[text()='News']")
    # driver.back()
    # time.sleep(3)

# Feature for turning pages
def TurnPage(buttonPath):
    driver.find_element_by_xpath(buttonPath).click()
    time.sleep(2)

# Feature for clearing cookies
def ClearCookies():
    # Clear cookies
    cookies = driver.get_cookies()
    # print(f"main:cookies = {cookies}")
    driver.delete_all_cookies()

# Feature for writing result to cvs file
def ResultToCVS(searchLink,resultList):
    with open("WriteCSVTest.csv", 'a', newline='') as resfile:
        writer = csv.writer(resfile)
        # write data
        writer.writerows([[searchLink, "en-gb", "news today"]])

# Preparation
def Preparation():
    # Preparation

    driver.get("https://www.bing.com/?mkt=en-us")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element_by_xpath('//div[@id="idCont"]/span[@class="sw_mktsw"]/a[@class="sw_lang"]').click()
    driver.find_element_by_xpath('//div[@id="idCont"]/span[@class="sw_mktsw"]/a[@class="sw_lang"]').click()


# Main test script
def FeatureTest(links):
    length = len(links)
    print("---------------The number of links(markets)----------------")
    print("The number of links:",length)

    for url in links:
        Preparation()
        SearchList["Sourcelink"] = url
        driver.get(url)
        time.sleep(2)
        # Search
        print("-------------New maket--------------")
        print(url)
        for i in range(4): # 0,1,2,3 loop 4 times

            try:
                # find election news
                driver.find_element_by_xpath('//div[@class="elec-modRoot-data"]')
            except NoSuchElementException:
                print("did not trigger ele news answer!")
                try:
                    # find ans_nws
                    driver.find_element_by_xpath('//div[@class="ans_nws"]')
                except NoSuchElementException:
                    print("did not trigger news answer!")
                    SearchList['Result'] = "Failed"
                    print("Faild!")
                else:
                    # find na_cnt item news
                    try:
                        # hero card or hero-card-like
                        driver.find_element_by_xpath(
                            '//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]')
                    except NoSuchElementException:
                        print("did not trigger news answer!")
                        SearchList['Result'] = "Failed"
                        print("Faild!")
                    else:
                        # find hero card
                        try:
                            driver.find_element_by_xpath(
                                '//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@class="nws_cwrp nws_itm"]/div[@class="b_clearfix b_overflow"]')
                        except NoSuchElementException:
                            # No hero card, So it is a only normal news news
                            print("it is a only normal news news")
                            try:
                                # find normal news
                                driver.find_element_by_xpath('//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@class="na_cl bc"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]')
                            except NoSuchElementException:
                                print( "did not trigger news!")
                                SearchList['Result'] = "Failed"
                                print("Failed!")
                            else:
                                OpenLinks(r'//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]')
                                TurnPage(r'//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn next rounded bld"]')
                                # TurnPage(r'//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn next rounded bld"]')
                                TurnPage(r'//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn prev rounded bld"]')
                                SearchList['Result'] = "Success"  # Only normal news
                                print("Success!")

                        else:
                            # find and click hero card
                            OpenLinks(r'//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@class="nws_cwrp nws_itm"]/div[@class="b_clearfix b_overflow"]')
                            # find if have normal news
                            try:
                                # find normal news
                                driver.find_element_by_xpath(
                                    '//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@class="na_cl bc"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]')
                            except NoSuchElementException:
                                print( "did not have normal news! It is a only hero card news!")
                                SearchList['Result'] = "Success!"   # Only hero card news
                                print("Success!")
                            else:
                                # Slide to election news position
                                # find normal news and click
                                OpenLinks(r'//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]')
                                # Turn page
                                TurnPage(r'//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn next rounded bld"]')
                                # TurnPage(r'//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn next rounded bld"]')
                                TurnPage(r'//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn prev rounded bld"]')
                                SearchList['Result'] = "Success!"  # hero card and normal news
                                print("Success!")
            else:
                time.sleep(3)
                # Election news triggered

                try:
                    # find hero card
                    driver.find_element_by_xpath('//div[@class="elec-modRoot-data"]/div[@class="elec-newsMod-hero"]')
                except NoSuchElementException:
                    print("No hero card in this election news!")
                    # And then find normal news of election news
                    try:
                        # find normal news
                        driver.find_element_by_xpath('//div[@class="elec-modRoot-data"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]')
                    except NoSuchElementException:
                        print("No election news trigger!!!")
                    else:
                        # find normal news and click
                        OpenLinks(r'//div[@class="elec-modRoot-data"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]')
                        # Turn page
                        TurnPage(r'//div[@class="elec-modRoot-data"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn next rounded bld"]')
                        # TurnPage(r'//div[@class="elec-modRoot-data"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn next rounded bld"]')
                        TurnPage(r'//div[@class="elec-modRoot-data"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn prev rounded bld"]')
                        print("triggered election normal news")
                        SearchList['Result'] = "Success!"
                        print("Success!")

                else:
                    # find hero card and click
                    OpenLinks(r'//div[@class="elec-modRoot-data"]/div[@class="elec-newsMod-hero"]')
                    # find normal news and click
                    OpenLinks(r'//div[@class="elec-modRoot-data"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]')

                    # Turn page
                    TurnPage(r'//div[@class="elec-modRoot-data"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn next rounded bld"]')
                    TurnPage(r'//div[@class="elec-modRoot-data"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn prev rounded bld"]')
                    print("The election news have hero card and normal news!")
                    SearchList['Result'] = "Success!"
                    print("Success!")
            # Record data
            DataRecord.append(SearchList)

            randomnum = random.randint(0, Klength - 1)
            # print(randomnum)
            print("**Search key word is :",KeyWordsList[randomnum])
            # Resplice urls
            marketURL = url.split('&')
            # print("length of marketURL",length(marketURL))
            newURL = "https://www.bing.com/search?q=" + KeyWordsList[randomnum] + "&" + marketURL[1] + "&" + marketURL[2]
            print("---Search URL is :",newURL)
            driver.get(newURL)

            SearchList['link'] = newURL
            SearchList['Keyword'] = KeyWordsList[randomnum]


        # Clear cookies
        ClearCookies()
    print(DataRecord)
# Feature test end

# Record original link,keywords and result
DataRecord = []
# Record search keywords link, keywords and result
SearchList = {}
FilePath = r"D:\PyCharmProject\WorkPractice\NewsAnswerForSeveralMarkets\TestData.csv"
with open(FilePath,'r+') as f:
    reader = csv.DictReader(f)
    # print(reader)
    LinkList = [row['SerpTestLink'] for row in reader]
# print(LinkList)

# get webdriver object
# chrome_options = Options()
# # close bar "Chrome正在受到自动软件的控制"
# chrome_options.add_argument("disable-infobars")
# # 允许浏览器重定向
# chrome_options.add_argument("disable-web-security")
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Firefox()
# clear cookies
cookies = driver.get_cookies()
# print(f"main:cookies = {cookies}")
driver.delete_all_cookies()
KeyWordsList = ['British royal family','coffee','travel','news today', 'biden','Google','local news','facebook','election2020']
Klength = len(KeyWordsList)


FeatureTest(LinkList)
