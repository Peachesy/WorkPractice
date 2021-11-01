from VerticalLandingExperience.PO.BingHP import BingHP
import pytest
import yaml


class TestEntryPoint:

    @pytest.mark.parametrize('market', yaml.safe_load(open('./market_data.yaml')))
    def test_entry_point(self, market):
        hp = BingHP()

        assert "http://stcav-867/news" in hp.go_to_verp(market).get_current_url()



