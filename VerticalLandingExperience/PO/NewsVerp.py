from VerticalLandingExperience.PO.Base import Base


class NewsVerp(Base):
    base_url = "http://stcav-867/news/?mkt=en-us&setlang=en"

    # Check text
    # 1.para q in URL
    # 2.search box value
    # 3.selected category

    # Help to assert if action jump from hp to verp is successful
    def get_current_url(self):
        return self.driver.current_url

    def check_text(self):
        pass

    # Check if category bar exist
    def check_categroybar(self):
        pass

    # Add para "form" and refresh
    # the result of refresh should be the same with the page from HP.
    def check_formcode(self):
        pass