from VerticalLandingExperience.PO.BingHP import BingHP
import pytest
import yaml


class TestEntryPoint:

    @pytest.mark.parametrize('market', yaml.safe_load(open('./market_data_test.yaml')))
    def test_entry_point(self, market):
        hp = BingHP()
        for i in market:
            assert "https://www.bing.com/news" in hp.go_to_verp(i).get_current_url()
        print()
        print("Did not have settings button in HP:", hp.no_setting_button_market)
        print("Did not have news button in settings:", hp.no_entry_point_market)



