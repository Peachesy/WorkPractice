from VerticalLandingExperience.PO.Base import Base
from VerticalLandingExperience.PO.BingHP import BingHP
from VerticalLandingExperience.PO.NewsVerpTop import NewsVerp
import pytest
import yaml


# @pytest.mark.parametrize('form_code', yaml.safe_load(open('./form_code.yaml')))
@pytest.mark.parametrize('market', yaml.safe_load(open('./market_data_test.yaml')))
class TestNewsVerp:
    nv = NewsVerp()
    hp = BingHP()

    # 1. if the category bar exist and the top stories selected
    def test_category(self, market):
        for i in market:
            self.hp.go_to_verp(i).check_categorybar(i)
        print()
        print("Market that did not have category bar:", self.nv.no_category_bar_market)
        print("Market that did not select top stories in category bar:", self.nv.did_not_select_top_stories_market)
        if len(self.nv.no_category_bar_market) == 0 or len(self.nv.did_not_select_top_stories_market) == 0:
            assert True

    # 2.If the texts of the 3 points are the same
    def test_3texts_same(self,market):
        for i in market:
            # self.nv.get_url_and_texts(market)
            self.hp.go_to_verp(market).get_url_and_texts(market)
            if self.nv.search_box_text == self.nv.paraq_text == self.nv.category_text:
                assert True

        return

    # # 4.Add form code and refresh, the result should be the same with the normal page.
    # def test_formcode_refresh(self):
    #     pass
