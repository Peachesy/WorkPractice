from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from VerticalLandingExperience.PO.Base import Base


class NewsVerp(Base):
    base_url = "http://stcav-867/news/?mkt=en-us&setlang=en"

    # Check text
    # 1.para q in URL
    # 2.search box value
    # 3.selected category

    # Recode url and para "q" in url to help to check if the texts of the 3 point are the same.
    verp_url = ""
    paraq_text = ""
    category_text = ''
    search_box_text = ''

    # Record if top stories button of category is selected
    did_not_select_top_stories_market = []
    # Record if the page have categroy bar
    no_category_bar_market = []
    # Record if there is no search keyword in search box
    no_search_text_market = []
    # Record if there is a keyword in URL para q
    no_keyword_of_paraq_market = []

    # The elements need to locate
    search_box_value_ele = (By.ID, 'sb_form_q')
    category_top_stories_button_ele = (By.XPATH, '//div[@class="nsn-body"]//ul[@id="nsn-category"]//a[1]')
    category_bar_ele = (By.CLASS_NAME, 'news verx')

    # Help to assert if action jump from hp to verp is successful
    def get_url_and_texts(self,market):
        for i in market:
            self.verp_url = self.driver.current_url
            self.paraq_text = self.remove_special_charactor(self.verp_url)
            if self.paraq_text == "":
                self.no_keyword_of_paraq_market.append(market)
            # get search keyword
            try:
                self.find(self.search_box_value_ele)
            except NoSuchElementException:
                self.no_search_text_market.append(market)
            else:
                self.search_box_text = self.find(self.search_box_value_ele).get_attribute("value")
            # get category selected text.
            try:
                self.find(self.category_bar_ele)
            except NoSuchElementException:
                self.no_category_bar_market.append(market)
            else:
                self.category_text = self.find(self.category_top_stories_button_ele).text
                category_selected = self.find(self.category_top_stories_button_ele).get_attribute("aria-selected")
                if category_selected == "false":
                    self.did_not_select_top_stories_market.append(market)

        return self.paraq_text, self.search_box_text, self.category_text




    # Add para "form" and refresh
    # the result of refresh should be the same with the page from HP.
    def check_formcode(self, form_code):
        pass