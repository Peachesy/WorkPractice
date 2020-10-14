from selenium import webdriver
import time

URL = "https://www.bing.com/search?q=trump&setflight=NAMktPref&mkt=chr-cher-us"
keyword = "trump"
marketURL = str(URL).split('&')
print(marketURL)
newURL = "https://www.bing.com/search?q="+keyword+"&"+marketURL[1]+"&"+marketURL[2]
print(newURL)

driver = webdriver.Chrome()
driver.get(newURL)

time.sleep(2)
driver.find_element_by_xpath('//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]').click()
time.sleep(2)

try:
    # find hero card
    driver.find_element_by_xpath(
        '//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@class="na_ti"]')
except NoSuchElementException:
    print("News answer with no hero card!")

    try:
        # find normal news
        driver.find_element_by_xpath(
            '//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]')
    except NoSuchElementException:
        print("There must be a bug!")
    else:
        # Slide to election news position
        js4 = "arguments[0].scrollIntoView();"
        driver.execute_script(js4, driver.find_element_by_xpath('//div[@class="ans_nws"]'))
        time.sleep(3)

        # find normal news and click
        driver.find_element_by_xpath(
            '//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]').click()
        time.sleep(5)
        driver.back()
        time.sleep(3)

        # Turn page
        driver.find_element_by_xpath(
            '//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn next rounded bld"]').click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn prev rounded bld"]').click()
        time.sleep(2)
else:
    time.sleep(2)

    # Slide to election news position
    js4 = "arguments[0].scrollIntoView();"
    driver.execute_script(js4, driver.find_element_by_xpath('//div[@class="ans_nws"]'))
    time.sleep(3)

    # find hero card and click
    driver.find_element_by_xpath(
        '//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@class="na_ti"]').click()
    time.sleep(5)
    driver.back()
    time.sleep(3)
    # find normal news and click
    driver.find_element_by_xpath(
        '//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]').click()
    time.sleep(5)
    driver.back()
    time.sleep(3)

    # Turn page
    driver.find_element_by_xpath(
        '//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn next rounded bld"]').click()
    time.sleep(2)
    driver.find_element_by_xpath(
        '//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn prev rounded bld"]').click()
    time.sleep(2)