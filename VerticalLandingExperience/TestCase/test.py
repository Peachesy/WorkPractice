from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import yaml

# driver = webdriver.Chrome()
# driver.get("http://www.bing.com/news/search?q=Top+stories&nvaug=%5bNewsVertical+Category%3d%22rt_MaxClass%22%5d&FORM=Z9LH3&setmkt=en-us&setlang=en-us")
# # driver.maximize_window()
# sleep(3)
#
# # driver.find_element(By.CSS_SELECTOR, '#nsn-category > li.nsn-category-item.rt_MaxClass.selected.expanded > div > a')
# ele = driver.find_element(By.XPATH, '//div[@class="nsn-body"]//ul[@id="nsn-category"]//a[1]').text
# ele_attr = driver.find_element(By.XPATH, '//div[@class="nsn-body"]//ul[@id="nsn-category"]//a[1]').get_attribute("aria-selected")
# search_text = driver.find_element(By.ID, 'sb_form_q').get_attribute("value")
# print(ele)
# print(ele_attr)
# print(search_text)

class TestYaml:

    @pytest.mark.parametrize('market', yaml.safe_load(open('./market_data_test.yaml')))
    @pytest.mark.parametrize('form_code', yaml.safe_load(open('./form_code.yaml')))
    def test_yaml(self,market,form_code):
        # print("------------Market------------",market)
        print("It is me!")
        print("-----------Form code--------------", form_code)
    # def test_form(form_code):
    #     print("-----------Form code--------------",form_code)

