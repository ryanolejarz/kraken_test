import pytest

from time import sleep

from utils.test_data import ASSET_PAIRS
from tests.BaseTest import BaseTest


class TestOHLCData(BaseTest):

    def verify_ohlc_data_response(self, asset_pair, result):
        ohlc_data_keys = result.keys()
        expected_keys = [asset_pair, 'last']
        for key in expected_keys:
            assert key in ohlc_data_keys, f'Expected key {key} not found.'

    @pytest.mark.smoke
    def test_ohlc_data(self):
        """ tests the result of the get ohcla data endpoint """
        asset_pair = 'ADAUSD'
        result = self.get_ohlc_data(asset_pair=asset_pair)
        self.verify_ohlc_data_response(asset_pair=asset_pair, result=result)

    @pytest.mark.skip(reason='EGeneral:Too many requests')
    def test_valid_intervals(self):
        """ tests valid values for the interval query param """
        valid_intervals = [1, 5, 15, 30, 60, 240, 1440, 10080, 21600]
        asset_pair = 'ADAUSD'
        for interval in valid_intervals:
            result = self.get_ohlc_data(asset_pair=asset_pair, interval=interval)
            self.verify_ohlc_data_response(asset_pair=asset_pair, result=result)

    @pytest.mark.errors
    def test_invalid_intervals(self):
        """ tests various values for the interval query param """
        invalid_intervals = [0, 2, 22000]
        asset_pair = 'ADAUSD'
        for interval in invalid_intervals:
            error = self.get_ohlc_data(asset_pair=asset_pair, interval=interval, expect_error=True)
            expected_error = 'EGeneral:Invalid arguments'
            assert len(error) > 0, 'Expected to find errors but found none'
            assert error[0] == expected_error, f'Expected error {expected_error} but got {error[0]}'

    @pytest.mark.regression
    def test_get_ohlc_data_since(self):
        """ tests data returned shortly after a request using the first request's "last"
         value as the value for the since query param returns a smaller amount of data
          NOTE: I'm just making an assumption here that we would never expect a full
          amount of data returned seconds after. """
        asset_pair = 'ADAUSD'
        result_1 = self.get_ohlc_data(asset_pair=asset_pair)
        data_1 = result_1[asset_pair]
        last_1 = result_1['last']
        sleep(1)
        result_2 = self.get_ohlc_data(asset_pair=asset_pair, since=last_1)
        data_2 = result_2[asset_pair]
        last_2 = result_2['last']
        assert last_2 >= last_1
        assert len(data_2) < len(data_1)

