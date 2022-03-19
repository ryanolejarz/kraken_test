import pytest

from utils.test_data import ASSET_PAIRS
from tests.BaseTest import BaseTest


class TestTicker(BaseTest):

    def verify_ticker_object(self, ticker):
        """ validates the data returned in the ticker response """
        ticker_keys = ticker.keys()
        expected_keys = [
            {'key_name': 'a', 'value_type': list},
            {'key_name': 'b', 'value_type': list},
            {'key_name': 'c', 'value_type': list},
            {'key_name': 'v', 'value_type': list},
            {'key_name': 'p', 'value_type': list},
            {'key_name': 't', 'value_type': list},
            {'key_name': 'l', 'value_type': list},
            {'key_name': 'h', 'value_type': list},
            {'key_name': 'o', 'value_type': str},

        ]
        for key in expected_keys:
            assert key['key_name'] in ticker_keys, f'Expected key {key} not found.'
            assert isinstance(ticker[key['key_name']], key['value_type']), \
                f'Expected {ticker[key["key_name"]]} to be type {key["value_type"]}'
            if key['key_name'] in ['a', 'b', 'c', 'v', 'p', 'l', 'h']:
                for data in ticker[key['key_name']]:
                    assert isinstance(data, str), f'Expected {data} to be type str'
            elif key['key_name'] == 't':
                for data in ticker[key['key_name']]:
                    assert isinstance(data, int), f'Expected {data} to be type int'

    @pytest.mark.smoke
    def test_single_ticker(self):
        """ tests when a single ticker/pair is requested """
        asset_pair = 'ADAUSD'
        result = self.get_ticker_info(asset_pair=asset_pair)
        assert asset_pair in result.keys(), f'{asset_pair} not found in result'
        self.verify_ticker_object(result[asset_pair])

    @pytest.mark.smoke
    def test_multiple_tickers(self):
        """ tests when multiple tickers/pairs are requested """
        asset_pairs = ['ADAUSD', 'DOTUSD']
        result = self.get_ticker_info(asset_pairs=asset_pairs)
        for asset_pair in asset_pairs:
            assert asset_pair in result.keys(), f'{asset_pair} not found in result.'
            self.verify_ticker_object(result[asset_pair])

    @pytest.mark.errors
    def test_invalid_ticker(self):
        """ tests when an invalid ticker/pair is requested """
        asset_pair = 'ABCXYZ'
        error = self.get_ticker_info(asset_pair=asset_pair, expect_error=True)
        expected_error = 'EQuery:Unknown asset pair'
        assert len(error) > 0, 'Expected to find errors but found none'
        assert error[0] == expected_error, f'Expected error {expected_error} but got {error[0]}'

    @pytest.mark.errors
    def test_no_ticker(self):
        """ tests when no ticker is requested an error is returned """
        error = self.get_ticker_info(expect_error=True)
        expected_error = 'EGeneral:Invalid arguments'
        assert len(error) > 0, 'Expected to find errors but found none'
        assert error[0] == expected_error, f'Expected error {expected_error} but got {error[0]}'

    @pytest.mark.smoke
    @pytest.mark.parametrize("asset_pair", ASSET_PAIRS)
    def test_known_tickers(self, asset_pair):
        """ tests all known tickers/pairs """
        result = self.get_ticker_info(asset_pair=asset_pair)
        assert asset_pair in result.keys(), f'{asset_pair} not found in result.'
        self.verify_ticker_object(result[asset_pair])
