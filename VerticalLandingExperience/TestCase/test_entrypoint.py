from VerticalLandingExperience.PO.BingHP import BingHP
import pytest
import yaml


@pytest.mark.parametrize('market', yaml.safe_load(open('./market_data_test.yaml')))
class TestEntryPoint:


    def test_entry_point(self, market):
        hp = BingHP()
        for i in market:
            assert "https://www.bing.com/news" in hp.go_to_verp(i).get_current_url()
        print()
        print("Did not have settings button in HP:", hp.no_setting_button_market)
        print("Did not have news button in settings:", hp.no_entry_point_market)

    def test_category(self, market):
        # for i in market:
        #     self.hp.go_to_verp(i).check_categorybar(i)
        # print("Market that did not have category bar:", self.nv.no_category_bar_market)
        # print("Market that did not select top stories in category bar:", self.nv.did_not_select_top_stories_market)
        # if len(self.nv.no_category_bar_market) == 0 or len(self.nv.did_not_select_top_stories_market) == 0:
        #     assert True
        print("---------------------")
        return



