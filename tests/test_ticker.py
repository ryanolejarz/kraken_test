import pytest

from utils.test_data import ASSET_PAIRS
from tests.BaseTest import BaseTest


class TestTicker(BaseTest):

    def verify_ticker_object(self, ticker):
        ticker_keys = ticker.keys()
        expected_keys = ['a', 'b', 'c', 'v', 'p', 't', 'l', 'h', 'o' ]
        for key in expected_keys:
            assert key in ticker_keys, f'Expected key {key} not found.'

    @pytest.mark.smoke
    def test_single_ticker(self):
        """ tests when a single ticker/pair is requested """
        asset_pair = 'ADAUSD'
        result = self.get_ticket_info(asset_pair=asset_pair)
        assert asset_pair in result.keys(), f'{asset_pair} not found in result'
        self.verify_ticker_object(result[asset_pair])

    @pytest.mark.smoke
    def test_multiple_tickers(self):
        """ tests when multiple tickers/pairs are requested """
        asset_pairs = ['ADAUSD', 'DOTUSD']
        result = self.get_ticket_info(asset_pairs=asset_pairs)
        for asset_pair in asset_pairs:
            assert asset_pair in result.keys(), f'{asset_pair} not found in result.'
            self.verify_ticker_object(result[asset_pair])

    @pytest.mark.errors
    def test_invalid_ticker(self):
        """ tests when an invalid ticker/pair is requested """
        asset_pair = 'ABCXYZ'
        error = self.get_ticket_info(asset_pair=asset_pair, expect_error=True)
        expected_error = 'EQuery:Unknown asset pair'
        assert len(error) > 0, 'Expected to find errors but found none'
        assert error[0] == expected_error, f'Expected error {expected_error} but got {error[0]}'

    @pytest.mark.errors
    def test_no_ticker(self):
        """ tests when no ticker is requested an error is returned """
        error = self.get_ticket_info(expect_error=True)
        expected_error = 'EGeneral:Invalid arguments'
        assert len(error) > 0, 'Expected to find errors but found none'
        assert error[0] == expected_error, f'Expected error {expected_error} but got {error[0]}'

    @pytest.mark.smoke
    @pytest.mark.parametrize("asset_pair", ASSET_PAIRS)
    def test_known_tickers(self, asset_pair):
        """ tests all known tickers/pairs """
        result = self.get_ticket_info(asset_pair=asset_pair)
        assert asset_pair in result.keys(), f'{asset_pair} not found in result.'
        self.verify_ticker_object(result[asset_pair])
