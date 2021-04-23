import pytest
from allpairspy import AllPairs


class TestParameterized(object):

    @pytest.mark.parametrize(("brand, operating_system, browser"), [
        value_list for value_list in AllPairs([
            ["DELL", "ACER"],
            ["98", "NT", "2000"],
            ["CHROME", "FIREFOX", "IE11", "SAFARI"]
        ])
    ])
    def test_with_pw(self, brand, operating_system, browser):
        pass

    @pytest.mark.parametrize("brand", ["X", "Y"])
    @pytest.mark.parametrize("operating_system", ["98", "NT", "2000"])
    @pytest.mark.parametrize("browser", ["CHROME", "FIREFOX", "IE11", "SAFARI"])
    def test_no_pw(self, brand, operating_system, browser):
        pass


def test_metafunc_pairwise_param(limited_param):
    assert not limited_param
