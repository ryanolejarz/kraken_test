import pytest

from utils.test_data import ASSET_PAIRS
from tests.BaseTest import BaseTest


class TestTradableAssetPairs(BaseTest):

    def verify_asset_pair_object(self, asset_pair):
        asset_pair__keys = asset_pair.keys()
        expected_keys = ['altname', 'wsname', 'aclass_base', 'base', 'aclass_quote', 'quote', 'lot', 'pair_decimals',
                         'lot_decimals','lot_multiplier','leverage_buy','leverage_sell','fees', 'fees_maker',
                         'fee_volume_currency', 'margin_call', 'margin_stop', 'ordermin']
        for key in expected_keys:
            assert key in asset_pair__keys, f'Expected key {key} not found.'

    @pytest.mark.smoke
    def test_single_asset_pair(self):
        """ tests when a single asset_pair is requested """
        asset_pair = 'ADAUSD'
        result = self.get_tradable_asset_pairs(asset_pair=asset_pair)
        assert asset_pair in result.keys(), f'{asset_pair} not found in result.'
        self.verify_asset_pair_object(result[asset_pair])

    @pytest.mark.smoke
    def test_multiple_asset_pairs(self):
        """ tests when multiple asset_pairs are requested """
        asset_pairs = ['ADAUSD', 'DOTUSD']
        result = self.get_tradable_asset_pairs(asset_pairs=asset_pairs)
        for asset_pair in asset_pairs:
            assert asset_pair in result.keys(), f'{asset_pair} not found in result.'
            self.verify_asset_pair_object(result[asset_pair])

    @pytest.mark.smoke
    @pytest.mark.parametrize("asset_pair", ASSET_PAIRS)
    def test_get_assets(self, asset_pair):
        """ tests when all asset pairs are requested """
        result = self.get_all_tradable_asset_pairs()
        assert asset_pair in result.keys(), f'{asset_pair} not found in result.'
        self.verify_asset_pair_object(result[asset_pair])

    @pytest.mark.errors
    def test_invalid_asset_pair(self):
        """ tests when an invalid asset pair is requested """
        asset_pair = 'ABCXYZ'
        error = self.get_tradable_asset_pairs(asset_pair=asset_pair, expect_error=True)
        expected_error = 'EQuery:Unknown asset pair'
        assert len(error) > 0, 'Expected to find errors but found none'
        assert error[0] == expected_error, f'Expected error {expected_error} but got {error[0]}'

