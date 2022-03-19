import pytest
from time import sleep

from utils.test_data import ASSET_PAIRS
from tests.BaseTest import BaseTest


class TestRecentSpreads(BaseTest):

    def verify_recent_spreads_response(self, asset_pair, result):
        """ validates the data returned in the recent spreads response """
        recent_spreads_keys = result.keys()
        expected_keys = [
            {'key_name': asset_pair, 'value_type': list},
            {'key_name': 'last', 'value_type': int},
        ]
        for key in expected_keys:
            assert key['key_name'] in recent_spreads_keys, f'Expected key {key} not found.'
            assert isinstance(result[key['key_name']], key['value_type']), \
                f'Expected {result[key["key_name"]]} to be type {key["value_type"]}'
        for pair in result[asset_pair]:
            assert isinstance(pair[0], int), f'Expected {pair[0]} to be type int'
            assert isinstance(pair[1], str), f'Expected {pair[1]} to be type str'
            assert isinstance(pair[2], str), f'Expected {pair[2]} to be type str'

    @pytest.mark.smoke
    def test_get_recent_spreads_data(self):
        """ tests the result of the get recent spreads endpoint """
        asset_pair = 'ADAUSD'
        result = self.get_recent_spreads(asset_pair=asset_pair)
        self.verify_recent_spreads_response(asset_pair=asset_pair, result=result)
        assert len(result[asset_pair]) > 0, 'Expected to find spreads but found none'

    @pytest.mark.errors
    def test_invalid_asset_pair(self):
        """ tests when an invalid ticker/pair is requested """
        asset_pair = 'ABCXYZ'
        error = self.get_recent_spreads(asset_pair=asset_pair, expect_error=True)
        expected_error = 'EQuery:Unknown asset pair'
        assert len(error) > 0, 'Expected to find errors but found none'
        assert error[0] == expected_error, f'Expected error {expected_error} but got {error[0]}'

    @pytest.mark.smoke
    @pytest.mark.parametrize("asset_pair", ASSET_PAIRS)
    def test_recent_spreads_for_known_asset_pairs(self, asset_pair):
        """ tests all known asset pairs """
        result = self.get_recent_spreads(asset_pair=asset_pair)
        assert asset_pair in result.keys(), f'{asset_pair} not found in result.'
        self.verify_recent_spreads_response(asset_pair, result)

    @pytest.mark.regression
    def test_get_recent_spreads_data_since(self):
        """ tests data returned shortly after a request using the first request's "last"
         value as the value for the since query param returns a smaller amount of data
          NOTE: I'm just making an assumption here that we would never expect a full
          amount of data returned seconds after. """
        asset_pair = 'ADAUSD'
        result_1 = self.get_recent_spreads(asset_pair=asset_pair)
        data_1 = result_1[asset_pair]
        last_1 = result_1['last']
        sleep(1)
        result_2 = self.get_recent_spreads(asset_pair=asset_pair, since=last_1)
        data_2 = result_2[asset_pair]
        last_2 = result_2['last']
        assert last_2 >= last_1, f'Expected {last_2} to be greater than or equal to {last_1}'
        assert len(data_2) < len(data_1), f'Expected {len(data_2)} to be less than {len(data_1)}'

