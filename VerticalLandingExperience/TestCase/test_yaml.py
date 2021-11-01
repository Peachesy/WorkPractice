import pytest
import yaml


class TestYaml:
    @pytest.mark.parametrize('market', yaml.safe_load(open('./market_data.yaml')))
    def test_yaml(self, market):
        print("打印market数据：",market)
        print(type(market))

