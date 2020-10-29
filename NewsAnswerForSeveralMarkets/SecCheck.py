import csv
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

# Just check the result from basic check and do not do any operations like open link and turn page.

# Feature for clearing cookies
def ClearCookies():
    # Clear cookies
    cookies = driver.get_cookies()
    # print(f"main:cookies = {cookies}")
    driver.delete_all_cookies()

# Preparation
def Preparation():
    # Preparation
    driver.get("https://www.bing.com/?mkt=en-us")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element_by_xpath('//div[@id="idCont"]/span[@class="sw_mktsw"]/a[@class="sw_lang"]').click()
    driver.find_element_by_xpath('//div[@id="idCont"]/span[@class="sw_mktsw"]/a[@class="sw_lang"]').click()
    time.sleep(2)

# Main test script
def FeatureTest(links):
    length = len(links)
    print("---------------The number of links(markets)----------------")
    print("The number of links:",length)

    for url in links:
        Preparation()
        driver.get(url)
        time.sleep(2)
        print("-------------New maket--------------")
        print(url)

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
                print("Faild!")
            else:
                # find na_cnt item news
                try:
                    # hero card or hero-card-like
                    driver.find_element_by_xpath(
                        '//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]')
                except NoSuchElementException:
                    print("did not trigger news answer!")
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
                            print("Failed!")
                        else:
                            print("Success!")

                    else:
                        # find and click hero card
                        # OpenLinks(r'//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@class="nws_cwrp nws_itm"]/div[@class="b_clearfix b_overflow"]')
                        # find if have normal news
                        try:
                            # find normal news
                            driver.find_element_by_xpath(
                                '//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@class="na_cl bc"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]')
                        except NoSuchElementException:
                            print( "did not have normal news! It is a only hero card news!")
                            print("Success!")
                        else:

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
                    print("triggered election normal news")
                    print("Success!")

            else:
                # find hero card and click
                print("The election news have hero card and normal news!")
                print("Success!")

        # for end
        # Clear cookies
        ClearCookies()
        # driver.quit()

# Feature test end

FilePath = r"D:\PyCharmProject\WorkPractice\NewsAnswerForSeveralMarkets\FailedLink.csv"
with open(FilePath,'r+') as f:
    reader = csv.DictReader(f)
    # print(reader)
    LinkList = [row['SerpTestLink'] for row in reader]
# print(LinkList)

# get webdriver object
chrome_options = Options()
# close bar "Chrome正在受到自动软件的控制"
chrome_options.add_argument("disable-infobars")
# 允许浏览器重定向
chrome_options.add_argument("disable-web-security")
driver = webdriver.Chrome(options=chrome_options)
# clear cookies
cookies = driver.get_cookies()
# print(f"main:cookies = {cookies}")
driver.delete_all_cookies()


FeatureTest(LinkList)
