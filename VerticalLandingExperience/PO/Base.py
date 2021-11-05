from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep


class Base:

    # base_url = "http://stcav-867/?mkt=en-us&setlang=en"

    def __init__(self, base_driver = None):
        if base_driver is None:
            self.driver = webdriver.Chrome()

            # Open BingHP
            # self.driver.get(self.base_url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
        else:
            self.driver: WebDriver = base_driver

    # Encapsulate finding element method.
    def find(self, by, locator = None):
        if locator is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by, value=locator)

    # remove the special charactor of para a and replace it with " "
    def remove_special_charactor(self,verp_url):

        from VerticalLandingExperience.PO.NewsVerpTop import NewsVerp
        nv = NewsVerp()

        temp_list = verp_url.split("&")
        para_q = temp_list[0].split("q=")
        nv.paraq_text = para_q[1].replace("+", " ")

        return nv.paraq_text

    def tear_down(self):
        self.driver.quit()



