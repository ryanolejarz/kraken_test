import pytest
from time import sleep

from utils.test_data import ASSET_PAIRS
from tests.BaseTest import BaseTest


class TestRecentTrades(BaseTest):

    def verify_recent_trades_response(self, asset_pair, result):
        recent_trades_keys = result.keys()
        expected_keys = [asset_pair, 'last']
        for key in expected_keys:
            assert key in recent_trades_keys, f'Expected key {key} not found.'

    @pytest.mark.smoke
    def test_get_recent_trades_data(self):
        """ tests the result of the get recent trades endpoint """
        asset_pair = 'ADAUSD'
        result = self.get_recent_trades(asset_pair=asset_pair)
        self.verify_recent_trades_response(asset_pair=asset_pair, result=result)
        assert len(result[asset_pair]) > 0, 'Expected to find spreads but found none'

    @pytest.mark.skip('Reason: BUG. Returning EGeneral:Invalid arguments error rather than Unknown asset pair')
    @pytest.mark.errors
    def test_invalid_asset_pair(self):
        """ tests when an invalid ticker/pair is requested """
        asset_pair = 'ABCXYZ'
        error = self.get_recent_trades(asset_pair=asset_pair, expect_error=True)
        expected_error = 'EQuery:Unknown asset pair'
        assert len(error) > 0, 'Expected to find errors but found none'
        assert error[0] == expected_error, f'Expected error {expected_error} but got {error[0]}'

    @pytest.mark.smoke
    @pytest.mark.parametrize("asset_pair", ASSET_PAIRS)
    def test_recent_trades_for_known_asset_pairs(self, asset_pair):
        """ tests all known asset pairs """
        result = self.get_recent_trades(asset_pair=asset_pair)
        assert asset_pair in result.keys(), f'{asset_pair} not found in result.'
        self.verify_recent_trades_response(asset_pair, result)

    @pytest.mark.regression
    def test_get_recent_trades_data_since(self):
        """ tests data returned shortly after a request using the first request's "last"
         value as the value for the since query param returns a smaller amount of data
          NOTE: I'm just making an assumption here that we would never expect a full
          amount of data returned seconds after. """
        asset_pair = 'ADAUSD'
        result_1 = self.get_recent_trades(asset_pair=asset_pair)
        data_1 = result_1[asset_pair]
        last_1 = result_1['last']
        sleep(1)
        result_2 = self.get_recent_trades(asset_pair=asset_pair, since=last_1)
        data_2 = result_2[asset_pair]
        last_2 = result_2['last']
        assert last_2 >= last_1
        assert len(data_2) < len(data_1)



