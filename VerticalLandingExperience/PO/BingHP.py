from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from VerticalLandingExperience.PO.Base import Base
from VerticalLandingExperience.PO.NewsVerp import NewsVerp


class BingHP(Base):
    base_url = "https://www.bing.com/?"

    # elements in the page
    # setting_button = '//li[@id="dots_overflow_menu_container"]'
    setting_button = (By.ID, "dots_overflow_menu_container")
    news_entry_button = (By.ID, "news")
    no_setting_button_market = []
    no_entry_point_market = []


    def go_to_verp(self,market):
        new_url = self.base_url + "setmkt=" + market + "&setlang=" + market
        self.driver.get(new_url)
        sleep(3)

        # floating the mouse to the setting button
        try:
            floating_button = self.find(self.setting_button)
        except NoSuchElementException:
            self.no_setting_button_market.append(market)
        else:
            ActionChains(self.driver).move_to_element(floating_button).perform()
            try:
                # click news entry button
                self.find(self.news_entry_button).click()
            except NoSuchElementException:
                self.no_entry_point_market.append(market)


        return NewsVerp(self.driver)