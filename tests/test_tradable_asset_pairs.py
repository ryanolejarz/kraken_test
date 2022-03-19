import pytest

from utils.test_data import ASSET_PAIRS
from tests.BaseTest import BaseTest


class TestTradableAssetPairs(BaseTest):

    def verify_tradale_asset_response(self, asset_pair):
        """ validates the data returned in the tradable asset response """
        asset_pair_keys = asset_pair.keys()
        expected_keys = [
            {'key_name': 'altname', 'value_type': str},
            {'key_name': 'wsname', 'value_type': str},
            {'key_name': 'aclass_base', 'value_type': str},
            {'key_name': 'base', 'value_type': str},
            {'key_name': 'aclass_quote', 'value_type': str},
            {'key_name': 'quote', 'value_type': str},
            {'key_name': 'lot', 'value_type': str},
            {'key_name': 'pair_decimals', 'value_type': int},
            {'key_name': 'lot_decimals', 'value_type': int},
            {'key_name': 'lot_multiplier', 'value_type': int},
            {'key_name': 'leverage_buy', 'value_type': list},
            {'key_name': 'leverage_sell', 'value_type': list},
            {'key_name': 'fees', 'value_type': list},
            {'key_name': 'fees_maker', 'value_type': list},
            {'key_name': 'fee_volume_currency', 'value_type': str},
            {'key_name': 'margin_call', 'value_type': int},
            {'key_name': 'margin_stop', 'value_type': int},
            {'key_name': 'ordermin', 'value_type': str}]
        for key in expected_keys:
            assert key['key_name'] in asset_pair_keys, f'Expected key {key} not found.'
            assert isinstance(asset_pair[key['key_name']], key['value_type']), \
                f'Expected {asset_pair[key["key_name"]]} to be type {key["value_type"]}'

    @pytest.mark.smoke
    def test_single_asset_pair(self):
        """ tests when a single asset_pair is requested """
        asset_pair = 'ADAUSD'
        result = self.get_tradable_asset_pairs(asset_pair=asset_pair)
        assert asset_pair in result.keys(), f'{asset_pair} not found in result.'
        self.verify_tradale_asset_response(result[asset_pair])

    @pytest.mark.smoke
    def test_multiple_asset_pairs(self):
        """ tests when multiple asset_pairs are requested """
        asset_pairs = ['ADAUSD', 'DOTUSD']
        result = self.get_tradable_asset_pairs(asset_pairs=asset_pairs)
        for asset_pair in asset_pairs:
            assert asset_pair in result.keys(), f'{asset_pair} not found in result.'
            self.verify_tradale_asset_response(result[asset_pair])

    @pytest.mark.smoke
    @pytest.mark.parametrize("asset_pair", ASSET_PAIRS)
    def test_get_assets(self, asset_pair):
        """ tests when all asset pairs are requested """
        result = self.get_all_tradable_asset_pairs()
        assert asset_pair in result.keys(), f'{asset_pair} not found in result.'
        self.verify_tradale_asset_response(result[asset_pair])

    @pytest.mark.errors
    def test_invalid_asset_pair(self):
        """ tests when an invalid asset pair is requested """
        asset_pair = 'ABCXYZ'
        error = self.get_tradable_asset_pairs(asset_pair=asset_pair, expect_error=True)
        expected_error = 'EQuery:Unknown asset pair'
        assert len(error) > 0, 'Expected to find errors but found none'
        assert error[0] == expected_error, f'Expected error {expected_error} but got {error[0]}'

