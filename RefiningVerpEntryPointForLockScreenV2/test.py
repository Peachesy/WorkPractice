import time
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("E:\WebDrivers\chromedriver.exe")
driver.maximize_window()

# cookies = driver.get_cookies()
driver.delete_all_cookies()

# 需要定位的元素
# 标志有category bar的元素
category_bar = '//a[@class="nsn-expand-btn"]'

# 获取search box中的值 driver.find_element_by_tag_name('input').get_attribute('value'):
search_box_value = '//div[@class="b_searchboxForm"]/input[@class="b_searchbox b_softkey"]'

# 获取category bar中top stories button的值，获取其text
top_stories_button_ele = '//div[@class="nsn-category-topitem-wrap"]/a[@class="ntext"]'

# 获取标题top stories的值，获取其text
title_ele = '//div[@class="content"]/span[@id="feed-top-stories-title-container"]/h2[@class=" feed-main-title "]'

no_category_bar = []
ChangedURL = []
Search_box_value = []
title = []
top_stories_button = []



try:
    driver.get("http://stcav-867/news/search?q=&mkt=en-US&setlang=en-US&form=m4021s")
    time.sleep(5)

    # 记录下当前页面的URL
    ChangedURL.append(driver.current_url)
    # 判断当前页面搜索框中是否有值
    if driver.find_element_by_tag_name('input').get_attribute('value'):
        Search_box_value.append(driver.find_element_by_tag_name('input').get_attribute('value'))
        print("搜索框中有值！值为：", driver.find_element_by_tag_name('input').get_attribute('value'))
    else:
        Search_box_value.append(-1)

    # 判断title
    if driver.find_element_by_xpath(title_ele) :
        title.append(driver.find_element_by_xpath(title_ele).text)
        print("title的值为：", driver.find_element_by_xpath(title_ele).text)
    else:
        title.append(-1)

    # 判断top stories button
    if driver.find_element_by_xpath(top_stories_button_ele) :
        top_stories_button.append(driver.find_element_by_xpath(top_stories_button_ele).text)
        print("top stories button的值为：", driver.find_element_by_xpath(top_stories_button_ele).text)
    else:
        top_stories_button.append(-1)

    driver.find_element_by_xpath(category_bar)
    no_category_bar.append("1")
except NoSuchElementException:
    no_category_bar.append(-1)

print(no_category_bar)
print(ChangedURL)
print("search box中的值：", Search_box_value)
print("title的值：", title)
print("top stories button的值：", top_stories_button)